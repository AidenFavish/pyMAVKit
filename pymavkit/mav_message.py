from typing import Any

class MAVMessage:
    def __init__(self, name:str, timestamp:float=0.0, priority=0, repeat_period:float=0.0):
        self.name = name
        self.timestamp = timestamp
        self.priority = priority
        self.repeat_period = repeat_period

    def process(self):
        pass

    def encode(self, system_id, component_id) -> Any:
        pass

    def decode(self, msg):
        pass

    def __repr__(self) -> str:
        return f"({self.name}) timestamp: {self.timestamp} ms"
