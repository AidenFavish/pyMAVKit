import pymavlink.dialects.v20.all as dialect
import time
from pymavkit.mav_message import MAVMessage

class SetpointVelocity(MAVMessage):
    """
    A position setpoint in local NED frame. Measured in meters.
    Boot time ms is the time since system boot in ms.
    """
    def __init__(self, target_system: int, target_component: int, boot_time_ms: int, vx: float, vy: float, vz: float, yaw: float):
        super().__init__("CUSTOM_SETPOINT_LOCAL")
        self.target_system = target_system
        self.target_component = target_component
        
        self.boot_time_ms = boot_time_ms
        self.vx = vx
        self.vy = vy
        self.vz= vz
        self.yaw = yaw

    def encode(self, system_id, component_id):
        return dialect.MAVLink_set_position_target_local_ned_message(
            time_boot_ms=int(time.time() * 1000 - self.boot_time_ms),
            target_system=int(self.target_system),
            target_component=int(self.target_component),
            coordinate_frame=int(8),  # MAV_FRAME_BODY_NED
            type_mask=int(3015),  # ignore all but x/y/z position
            x=float(0.0),
            y=float(0.0),
            z=float(0.0),
            vx=float(self.vx),
            vy=float(self.vy),
            vz=float(self.vz),
            afx=float(0.0),
            afy=float(0.0),
            afz=float(0.0),
            yaw=float(self.yaw),
            yaw_rate=float(0.0)
        )
