from pymavkit.mav_protocol import MAVProtocol
from pymavkit.mav_sender import Sender
from pymavkit.mav_receiver import Receiver
from pymavkit.messages.heartbeat_msg import Heartbeat

class HeartbeatProtocol(MAVProtocol):
    def __init__(self):
        super().__init__()
        self.heartbeat_msg = Heartbeat()

    def run(self, sender: Sender, receiver: Receiver):
        sender.send_msg(self.heartbeat_msg)

    def __repr__(self) -> str:
        return str(self.heartbeat_msg)
