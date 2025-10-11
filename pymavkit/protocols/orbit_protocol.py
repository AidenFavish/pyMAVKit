from pymavkit.mav_protocol import MAVProtocol
from pymavkit.messages import SetpointVelocity, LocalPositionNED
import time
import numpy as np

class OrbitProtocol(MAVProtocol):
    """
    Orbits given a radius.
    """
    def __init__(self, current_pos: LocalPositionNED, radius: float, boot_time_ms: int, target_system: int = 1, target_component: int = 0):
        super().__init__()
        self.current_pos = current_pos
        self.radius = radius
        self.boot_time_ms = boot_time_ms
        self.target_system = target_system
        self.target_component = target_component

        self.setpoint_msg = SetpointVelocity(self.target_system, self.target_component, self.boot_time_ms, 0.0, 0.0, 0.0)

    def run(self, sender, receiver):
        step = 0.5
        angular_vel = 0.2
        t = 0.0

        while True:
            theta = angular_vel * t
            x = self.radius * np.cos(theta)
            y = self.radius * np.sin(theta)

            vx = -self.radius * angular_vel * np.sin(theta)
            vy = self.radius * angular_vel * np.cos(theta)

            self.setpoint_msg.vx = vx
            self.setpoint_msg.vy = vy

            sender.send_msg(self.setpoint_msg)
            
            time.sleep(step)
            t += step

    @staticmethod
    def dist(first: tuple[float, float, float], second: tuple[float, float, float]) -> float:
        return sum([(first[i] - second[i]) ** 2 for i in range(3)]) ** 0.5
