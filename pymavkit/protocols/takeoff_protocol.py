from pymavkit.mav_protocol import MAVProtocol
from pymavkit.messages import Takeoff, CommandAck

class TakeoffProtocol(MAVProtocol):
    """
    Allows to set takeoff to altitude at certain rate. All in local frame meters and m/s.
    Must be in guided mode.
    Ascent rate < 0 uses WPNAV_SPEED_DN
    """
    def __init__(self, altitude: float, ascent_rate: float, target_system: int = 1, target_component: int = 0):
        super().__init__()
        self.altitude = altitude
        self.ascent_rate = ascent_rate
        self.target_system = target_system
        self.target_component = target_component

        self.takeoff_msg = Takeoff(self.target_system, self.target_component, self.altitude, self.ascent_rate)
        self.ack_msg = CommandAck()

    def run(self, sender, receiver):
        sender.send_msg(self.takeoff_msg)
        receiver.wait_for_msg(self.ack_msg)
