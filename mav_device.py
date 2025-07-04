
class MAVDevice:
    def __init__(self, link:str, attempt_reconnect=True):
        self.mission = None
    
    def _connect(self, link:str, attempt_reconnect:bool):
        pass

    def add_listener(self, listener):
        pass

    def get_parameter(self, name:str):
        pass

    def set_parameter(self, name:str, value):
        pass

    def _main_loop(self):
        pass