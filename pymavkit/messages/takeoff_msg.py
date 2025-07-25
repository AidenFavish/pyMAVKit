import pymavlink.dialects.v20.all as dialect
from enum import Enum

from pymavkit.mav_message import MAVMessage
from pymavkit.messages.heartbeat_msg import FlightMode

class MAVFrame(Enum):
    GLOBAL = 0  # Altitude in MSL
    LOCAL_NED = 1  # Altitude in AGL
    GLOBAL_RELATIVE_ALTITUDE = 3  # Altitude in AGL

class Takeoff(MAVMessage):
    """
    Takeoff message. Simplified so altitude in relative (AGL) meters.
    """
    def __init__(self, target_system:int, target_component:int, alt:float):
        super().__init__("CUSTOM_TAKEOFF")
        self.target_system = target_system
        self.target_component = target_component

        self.alt = alt

    def encode(self, system_id, component_id):
        return dialect.MAVLink_command_int_message(
            target_system=int(self.target_system),
            target_component=int(self.target_component),
            frame=int(3),  # safer than hardcoding 3
            command=int(22),  # MAV_CMD_NAV_TAKEOFF
            current=int(0),
            autocontinue=int(0),
            param1=float(0.0),
            param2=float(0.0),
            param3=float(0.0),
            param4=float(0.0),
            x=int(0),  # required to be int
            y=int(0),  # required to be int
            z=float(self.alt)  # required to be float
        )
    
    def __repr__(self):
        return f"(CUSTOM_TAKEOFF) timestamp: {self.timestamp}, altitude: {self.alt}"
        