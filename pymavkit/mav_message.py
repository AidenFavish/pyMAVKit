from typing import Any, Callable

class MAVMessage:
    def __init__(self, name:str, timestamp:float=0.0, priority=0, repeat_period:float=0.0, callback_func: Callable[[Any], None] = lambda msg: None):
        self.name = name
        self.timestamp = timestamp
        self.priority = priority
        self.repeat_period = repeat_period
        self.callback_func = callback_func

    def process(self):
        self.callback_func(self)

    def encode(self, system_id, component_id) -> Any:
        pass

    def decode(self, msg):
        pass

    def __repr__(self) -> str:
        return f"({self.name}) timestamp: {self.timestamp} ms"
