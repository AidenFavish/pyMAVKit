import pymavlink.dialects.v20.all as dialect
from enum import Enum

from pymavkit.mav_message import MAVMessage
from pymavkit.messages import FlightMode

class MAVFrame(Enum):
    GLOBAL = 0  # Altitude in MSL
    LOCAL_NED = 1  # Altitude in AGL

class Takeoff(MAVMessage):
    """
    Takeoff message. Simplified so altitude in AGL meters. ascent rate in m/s.
    """
    def __init__(self, target_system:int, target_component:int, alt:float, ascent_rate: float):
        super().__init__("CUSTOM_TAKEOFF")
        self.target_system = target_system
        self.target_component = target_component

        self.frame = MAVFrame.LOCAL_NED
        self.alt = alt
        self.ascent_rate = ascent_rate

    def encode(self, system_id, component_id):
        return dialect.MAVLink_command_int_message(
            target_system=self.target_system,
            target_component=self.target_component,
            frame = self.frame.value,
            command=24,  # MAV_CMD_NAV_TAKEOFF_LOCAL (24)
            param1=0.0,
            param2=0.0,
            param3=self.ascent_rate,
            param4=0.0,
            x = 0,
            y = 0,
            z = self.alt
        )
    
    def __repr__(self):
        return f"(CUSTOM_TAKEOFF) timestamp: {self.timestamp}, altitude: {self.alt}, ascent rate: {self.ascent_rate}"
        