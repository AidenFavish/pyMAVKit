import pymavlink.dialects.v20.all as dialect
from enum import Enum

from pymavkit.mav_message import MAVMessage


class MAVResult(Enum):
    UNKNOWN = -1
    ACCEPTED = 0
    TRY_AGAIN_LATER = 1
    DENIED = 2
    UNSUPPORTED = 3
    FAILED = 4
    IN_PROGRESS = 5
    CANCELLED = 6
    COMMAND_LONG_ONLY = 7
    COMMAND_INT_ONLY = 8
    UNSUPPORTED_MAV_FRAME = 9

class CommandAck(MAVMessage):
    def __init__(self):
        super().__init__("COMMAND_ACK")
        self.command_id = -1
        self.result = MAVResult.UNKNOWN

    def decode(self, msg):
        self.command_id = msg.command
        self.result = MAVResult(msg.result)

    def __repr__(self):
        return f"(COMMAND_ACK) timestamp: {self.timestamp} ms, command_id: {self.command_id}, result: {self.result.name}"
