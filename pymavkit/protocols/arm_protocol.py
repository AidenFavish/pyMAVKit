from pymavkit.mav_protocol import MAVProtocol
from pymavkit.messages import Arm
from pymavkit.messages.command_ack_msg import CommandAck

class ArmProtocol(MAVProtocol):
    """
    Arms device.
    """
    def __init__(self, target_system: int = 1, target_component: int = 0):
        super().__init__()
        self.target_system = target_system
        self.target_component = target_component

        self.arm_msg = Arm()
        self.ack_msg = CommandAck()

    def run(self, sender, receiver):
        sender.send_msg(self.arm_msg)
        receiver.wait_for_msg(self.ack_msg)
