import time

from pymavkit import MAVDevice
import pymavkit.messages as messages
import pymavkit.protocols as protocols

#  33.02101538740278, -117.10290244624352

waypoints = [(20.0, 0.0, -25.0), (0.0, 20.0, -25.0), (-20.0, 0.0, -25.0)]

device = MAVDevice("udp:127.0.0.1:14550")

boot_time_ms = int(time.time() * 1000)

heartbeat = device.run_protocol(protocols.HeartbeatProtocol())
local_pos = messages.LocalPositionNED()
device.add_listener(local_pos)
fc_heartbeat = device.add_listener(messages.Heartbeat())

set_mode_protocol = protocols.SetModeProtocol(messages.FlightMode.GUIDED, target_system=1, target_component=1)
device.run_protocol(set_mode_protocol)
mode_ack = set_mode_protocol.ack_msg

arm = device.run_protocol(protocols.ArmProtocol())

takeoff = device.run_protocol(protocols.TakeoffProtocol(20.0))

time.sleep(15)

setpoint = device.run_protocol(protocols.LocalSetpointProtocol(local_pos, waypoints, 1.0, boot_time_ms))

set_mode_protocol = protocols.SetModeProtocol(messages.FlightMode.RTL)
device.run_protocol(set_mode_protocol)
