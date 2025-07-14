import pymavlink.dialects.v20.all as dialect
from enum import Enum

from pymavkit.mav_message import MAVMessage


class MAVSeverity(Enum):
    EMERGENCY = 0
    ALERT = 1
    CRITICAL = 2
    ERROR = 3
    WARNING = 4
    NOTICE = 5
    INFO = 6
    DEBUG = 7

class StatusText(MAVMessage):
    def __init__(self, text: str, severity: MAVSeverity, cb=lambda x: None):
        super().__init__("STATUSTEXT", callback_func=cb)
        self.text = text
        self.severity = severity

    def encode(self, system_id, component_id):
        return dialect.MAVLink_statustext_message(
            severity = self.severity.value,
            text = self.text.encode('utf-8')
        )
    
    def decode(self, msg):
        self.text = str(msg.text)
        self.severity = MAVSeverity(msg.severity)

    def __repr__(self):
        return f"(STATUSTEXT) timestamp: {self.timestamp}, severity: {self.severity.name}, text: '{self.text}'"
