
class MAVMessage:
    def __init__(self, name:str, timestamp, priority=0):
        self.name = name
        self.timestamp = timestamp
        self.priority = priority

    def process(self):
        pass

    def update_data(self, other):
        if type(other) is not type(self):
            raise TypeError(f"Attempting to copy attributes from {type(other)} to {type(self)}")
        for key, value in vars(other).items():
            setattr(self, key, value)

    def get_msg(self, system_id, component_id):
        pass
