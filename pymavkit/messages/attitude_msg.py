import pymavlink.dialects.v20.all as dialect

from pymavkit.mav_message import MAVMessage


class Attitude(MAVMessage):
    """
    Reads ATTITUDE mavlink message. only reads pitch and roll.
    """
    def __init__(self):
        super().__init__("ATTITUDE")
        self.pitch = 0.0
        self.roll = 0.0

    def decode(self, msg):
        self.pitch = msg.pitch
        self.roll = msg.roll

    def __repr__(self) -> str:
        return f"(ATTITUDE) timestamp: {self.timestamp} ms, pitch: {self.pitch}, roll: {self.roll}"
