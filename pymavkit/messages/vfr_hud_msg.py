import pymavlink.dialects.v20.all as dialect

from pymavkit.mav_message import MAVMessage


class VFRHUD(MAVMessage):
    def __init__(self):
        super().__init__("VFR_HUD")
        self.airspeed = 0.0
        self.groundspeed = 0.0
        self.climbspeed = 0.0
        self.heading_int = 0
        self.throttle = 0.0
        self.alt_msl = 0.0

    def decode(self, msg):
        self.airspeed = msg.airspeed
        self.groundspeed = msg.groundspeed
        self.climbspeed = msg.climb
        self.heading_int = msg.heading
        self.throttle = msg.throttle
        self.alt_msl = msg.alt

    def __repr__(self) -> str:
        return f"(VFR_HUD) timestamp: {self.timestamp} ms, throttle: {self.throttle}"
