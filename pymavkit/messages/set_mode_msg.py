import pymavlink.dialects.v20.all as dialect
from enum import Enum

from pymavkit.mav_message import MAVMessage


class MAVMode(Enum):
    """Common ArduPilot modes and their value."""
    STABILIZE=0
    ACRO=1
    ALT_HOLD=2
    AUTO=3
    GUIDED=4
    LOITER=5
    RTL=6
    CIRCLE=7
    LAND=9
    DRIFT=11
    SPORT=13
    FLIP=14
    AUTO_TUNE=15
    POS_HOLD=16
    BRAKE=17

class SetMode(MAVMessage):
    def __init__(self, target_system:int, target_component:int, mode:MAVMode):
        super().__init__("CUSTOM_SET_MODE")
        self.target_system = target_system
        self.target_component = target_component
        self.mode = mode

    def encode(self, system_id, component_id):
        return dialect.MAVLink_command_long_message(
            target_system=self.target_system,
            target_component=self.target_component,
            command=176,  # MAV_CMD_DO_SET_MODE (176)
            confirmation=0,
            param1=1.0,
            param2=float(self.mode.value),
            param3=0.0,
            param4=0.0,
            param5=0.0,
            param6=0.0,
            param7=0.0
        )
        