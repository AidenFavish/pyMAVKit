import pymavlink.dialects.v20.all as dialect

from pymavkit.mav_message import MAVMessage


class GlobalPosition(MAVMessage):
    def __init__(self):
        super().__init__("GLOBAL_POSITION_INT")
        self.time_boot_ms = -1
        self.lat = 0.0
        self.lon = 0.0
        self.alt_msl = 0.0
        self.alt_relative = 0.0
        self.vx = 0.0
        self.vy = 0.0
        self.xz = 0.0
        self.heading = 0.0

    def decode(self, msg):
        self.time_boot_ms = msg.time_boot_ms
        self.lat = msg.lat
        self.lon = msg.lon
        self.alt_msl = msg.alt
        self.alt_relative = msg.relative_alt
        self.vx = msg.vx
        self.vy = msg.vy
        self.xz = msg.vz
        self.heading = msg.hdg

    def get_pos(self):
        return (self.lat, self.lon, self.alt_relative)
    
    def get_vel(self):
        return (self.vx, self.vy, self.vz)

    def __repr__(self) -> str:
        return f"(GLOBAL_POSITION_INT) timestamp: {self.timestamp} ms, time_since_boot {self.time_boot_ms} ms, \
            position: {self.get_pos()}, velocity: {self.get_vel()}, heading: {self.heading}"
