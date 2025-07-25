import pymavlink.dialects.v20.all as dialect

from pymavkit.mav_message import MAVMessage


class LocalPositionNED(MAVMessage):
    """
    Gets the local position in NED frame. Origin is at ardupilot origin which is often at first gps fix. 
    In meters for distances and m/s for velocities.
    """
    def __init__(self):
        super().__init__("LOCAL_POSITION_NED")
        self.time_boot_ms = -1
        self.x = 0.0
        self.y = 0.0
        self.z = 0.0
        self.vx = 0.0
        self.vy = 0.0
        self.vz = 0.0

    def decode(self, msg):
        self.time_boot_ms = msg.time_boot_ms
        self.x = msg.x
        self.y = msg.y
        self.z = msg.z
        self.vx = msg.vx
        self.vy = msg.vy
        self.vz = msg.vz

    def get_pos(self) -> tuple[float, float, float]:
        return (self.x, self.y, self.z)
    
    def get_vel(self):
        return (self.vx, self.vy, self.vz)

    def __repr__(self) -> str:
        return f"(LOCAL_POSITION_NED) timestamp: {self.timestamp} ms, time_since_boot {self.time_boot_ms} ms, \
            position: {self.get_pos()}, velocity: {self.get_vel()}"
