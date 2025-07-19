import pymavlink.dialects.v20.all as dialect
from enum import Enum

from pymavkit.mav_message import MAVMessage

class BatteryFunction(Enum):
    UNINITIALIZED = -1
    UNKNOWN = 0
    ALL = 1
    PROPULSION = 2
    AVIONICS = 3
    PAYLOAD = 4

class BatteryType(Enum):
    UNINITIALIZED = -1
    UNKNOWN = 0
    LIPO = 1
    LIFE = 2
    LION = 3
    NIMH = 4

class BatteryStatus(MAVMessage):
    """
    Reads BATTERY_STATUS function. Uses BatteryType and BatteryFunction enums accordingly.
    """
    def __init__(self):
        super().__init__("BATTERY_STATUS")
        self.bat_id = -1
        self.bat_func = BatteryFunction(-1)
        self.bat_type = BatteryType(-1)
        self.temp = -1
        self.voltages = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        self.current = -1
        self.current_consumed = -1
        self.energy_consumed = -1
        self.soc = -1


    def decode(self, msg):
        self.bat_id = msg.id
        self.bat_func = BatteryFunction(msg.battery_function)
        self.bat_type = BatteryType(msg.type)
        self.temp = msg.temperature
        self.voltages = msg.voltages
        self.current = msg.current_battery
        self.current_consumed = msg.current_consumed
        self.energy_consumed = msg.energy_consumed
        self.soc = msg.battery_remaining

    def __repr__(self) -> str:
        return f"(BATTERY_STATUS) timestamp: {self.timestamp} ms, voltages: {self.voltages}, soc: {self.soc}%, func: {self.bat_func.name}, type: {self.bat_type.name}"
