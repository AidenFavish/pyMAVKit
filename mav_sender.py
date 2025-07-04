import threading

from mav_message import MAVMessage
from mav_receiver import Receiver

class Sender:
    def __init__(self, receiver: Receiver):
        self.receiver = receiver
        self._lock = threading.Lock()
        self._owner = None

    def acquire(self):
        self._lock.acquire()
        self._owner = threading.get_ident()

    def release(self):
        if not self.is_owned():
            raise RuntimeError("Current thread does not own the lock")
        self._owner = None
        self._lock.release()

    def is_owned(self):
        return threading.get_ident() == self._owner

    def send_msg(self, msg: MAVMessage):
        if not self.is_owned():
            raise RuntimeError("Current thread does not own the lock")
        
        

    