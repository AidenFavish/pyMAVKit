import pymavlink.dialects.v20.all as dialect
from enum import Enum
from typing import Any, Callable

from pymavkit.mav_message import MAVMessage

MAV_TYPE_GCS = 6
MAV_AUTOPILOT_INVALID = 8  # Not a valid autopilot, e.g. a GCS
MAV_MODE_CUSTOM = 0
NO_FLAGS = 0

class MAVState(Enum):
    UNKNOWN = -1
    UNINITIALIZED = 0
    BOOTING_UP = 1
    CALIBRATING = 2
    STANDBY = 3
    ACTIVE = 4
    CRITICAL = 5
    EMERGENCY = 6
    POWEROFF = 7
    FLIGHT_TERMINATION = 8

class Heartbeat(MAVMessage):
    def __init__(self, callback_func: Callable[[Any], None] = lambda x: None):
        super().__init__("HEARTBEAT", repeat_period=1.0, callback_func=callback_func)
        self.type_id = -1
        self.state = "UNKNOWN"
        self.src_sys = -1
        self.src_comp = -1

    def encode(self, system_id, component_id):
        return dialect.MAVLink_heartbeat_message(
            type=MAV_TYPE_GCS, 
            autopilot=MAV_AUTOPILOT_INVALID, 
            base_mode=MAV_MODE_CUSTOM, 
            custom_mode=NO_FLAGS, 
            system_status=MAVState.UNINITIALIZED.value, 
            mavlink_version=2
        )

    def decode(self, msg):
        self.type_id = msg.type
        self.state = MAVState(msg.system_status)
        self.src_sys = msg.get_srcSystem()
        self.src_comp = msg.get_srcComponent()

    def __repr__(self) -> str:
        return f"(HEARTBEAT) timestamp: {self.timestamp} ms, type: {self.type_id}, state: {self.state.name}, system: {self.src_sys}, component: {self.src_comp}"
