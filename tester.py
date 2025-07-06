import time

from pymavkit import MAVDevice
from pymavkit import Heartbeat
from pymavkit.protocols.heartbeat_protocol import HeartbeatProtocol
from pymavkit.messages.local_position_ned_msg import LocalPositionNED
from pymavkit.protocols.set_mode_protocol import MAVMode, SetModeProtocol
from pymavkit.protocols.status_text_protocol import StatusTextProtocol, MAVSeverity

device = MAVDevice("udp:127.0.0.1:14445")

heartbeat = device.run_protocol(HeartbeatProtocol())
local_pos = device.add_listener(LocalPositionNED())
fc_heartbeat = device.add_listener(Heartbeat())

set_mode_protocol = SetModeProtocol(MAVMode.STABILIZE, target_system=1, target_component=1)
device.run_protocol(set_mode_protocol)
mode_ack = set_mode_protocol.ack_msg

status_text = device.run_protocol(StatusTextProtocol("PYMAVKit starting...", MAVSeverity.NOTICE))

while True:
    print(time.ctime())
    test_info = device.run_protocol(StatusTextProtocol("blud...", MAVSeverity.INFO))
    print(f"{heartbeat}\n{local_pos}\n{fc_heartbeat}\n", flush=True)
    time.sleep(1)
