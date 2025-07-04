import queue
import threading
import time

from mav_message import MAVMessage

MAX_QUEUE_SIZE = 500
HISTORY_SIZE = 10

class Receiver:
    def __init__(self, listeners: list[MAVMessage]):
        self.history_dict: dict[str, list] = {}
        self.queue: queue.Queue[MAVMessage] = queue.Queue()
        self.listeners = listeners
        self.waiting: list[MAVMessage] = []
        self.receiving = False
    
    def start_receiving(self):
        self.receiving = True
        self._thread = threading.Thread(target=self.process, daemon=True)
        self._thread.start()
        
    def stop_receiving(self):
        self.receiving = False

    def process(self):
        while self.receiving:
            msg = self.queue.get()
            msg.process()

            # Check if waiting for this message
            for wait_msg in self.waiting:
                if wait_msg.name == msg.name:
                    wait_msg.update_data(msg)

            # Update listeners
            if msg.name in self.listeners:
                self.listeners[msg.name].update_data(msg)

            # Manage message history
            if msg.name in self.history_dict:
                self.history_dict[msg.name].insert(0, msg)

                # Manage history length
                if len(self.history_dict[msg.name]) > HISTORY_SIZE:
                    self.history_dict[msg.name].pop()
            else:
                # Brand new message type
                self.history_dict[msg.name] = [msg]

    def wait_for_msg(self, msg: MAVMessage):
        self.waiting.append(msg)
        while msg.timestamp == 0:
            time.sleep(.001)
        return msg
        

