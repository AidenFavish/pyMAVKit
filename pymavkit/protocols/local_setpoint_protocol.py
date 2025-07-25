from pymavkit.mav_protocol import MAVProtocol
from pymavkit.messages import SetpointLocal, CommandAck, LocalPositionNED
import time

class LocalSetpointProtocol(MAVProtocol):
    """
    Navigates to a list of waypoints. Does not yaw through them. 
    Waypoints are in local ned coords xyz, in meters.
    Must be in guided mode.
    """
    def __init__(self, current_pos: LocalPositionNED, waypoints: list[tuple[float, float, float]], radius: float, boot_time_ms: int, target_system: int = 1, target_component: int = 0):
        super().__init__()
        self.current_pos = current_pos
        self.waypoints = waypoints
        self.radius = radius
        self.boot_time_ms = boot_time_ms
        self.target_system = target_system
        self.target_component = target_component

        self.setpoint_msg = SetpointLocal(self.target_system, self.target_component, self.boot_time_ms, 0.0, 0.0, 0.0)
        self.ack_msg = CommandAck()

    def run(self, sender, receiver):

        for waypoint in self.waypoints:
            while self.dist(waypoint, self.current_pos.get_pos()) > self.radius:
                self.setpoint_msg.load(waypoint)
                sender.send_msg(self.setpoint_msg)
                time.sleep(1)

    @staticmethod
    def dist(first: tuple[float, float, float], second: tuple[float, float, float]) -> float:
        return sum([(first[i] - second[i]) ** 2 for i in range(3)]) ** 0.5
