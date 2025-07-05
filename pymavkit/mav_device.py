import pymavlink.mavutil as utility
import pymavlink.dialects.v20.all as dialect
import threading
import time

from .mav_protocol import MAVProtocol
from .mav_receiver import Receiver
from .mav_sender import Sender
from .mav_message import MAVMessage

class MAVDevice:
    def __init__(self, device_address:str, baud_rate:int=115200, source_system:int=255, source_component:int=0, attempt_reconnect:bool=True):
        self.attempt_reconnect = attempt_reconnect
        self.listeners = []
        self.receiver = Receiver(self.listeners)
        self.connection: utility.mavudp | utility.mavserial = self._connect(device_address, baud_rate, source_system, source_component)
        self.sender = Sender(self.receiver, self.connection.target_system, self.connection.target_component, self.connection)

        self.receiver.start_receiving()

        self.reading = True
        self.thread = threading.Thread(target=self._main_loop, daemon=True)
        self.thread.start()
    
    def _connect(self, device_address:str, baud_rate:int, source_system:int, source_component:int) -> utility.mavudp | utility.mavserial:
        """
        device_address follows by pymavlink standards: 'udp:127.0.0.1:14550' or '/dev/ttyACM0'
        """
        connection = utility.mavlink_connection(device=device_address, baud=baud_rate, source_system=source_system, source_component=source_component)
        return connection

    def stop_reading(self):
        self.reading = False

    def add_listener(self, listener: MAVMessage) -> MAVMessage:
        self.listeners.append(listener)
        return listener

    def run_protocol(self, protocol: MAVProtocol):
        self.sender.acquire()
        protocol.run(self.sender, self.receiver)
        self.sender.release()

    def _main_loop(self):
        while self.reading:
            msg = self.connection.recv_match(blocking=True, timeout=1)
            if msg:
                timestamp_ms = time.time() * 1000
                self.receiver.queue.put((timestamp_ms, msg))
