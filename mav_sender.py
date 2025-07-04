import threading

from mav_message import MAVMessage
from mav_receiver import Receiver

class Sender:
    def __init__(self, receiver: Receiver, sys_id: int, component_id: int, connection):
        self.receiver = receiver
        self.sys_id = sys_id
        self.component_id = component_id
        self.connection = connection
        self._lock = threading.Lock()
        self._owner = None

    def acquire(self):
        self._lock.acquire()
        self._owner = threading.get_ident()

    def release(self):
        if not self._is_owned():
            raise RuntimeError("Current thread does not own the lock")
        self._owner = None
        self._lock.release()

    def _is_owned(self):
        """Checks if the current thread owns the lock"""
        return threading.get_ident() == self._owner

    def send_msg(self, msg: MAVMessage, system_id=None, component_id=None):
        """
        Sends a mavlink message. Must have aquired the lock (automatic if using run protocol). 
        Optional specified system and component ids otherwise connection defaults used.
        """
        if not self._is_owned():
            raise RuntimeError("Current thread does not own the lock")
        mav_msg = msg.get_mav_msg(self.sys_id if not system_id else system_id, self.component_id if not component_id else component_id)
        self.connection.mav.send(mav_msg)
