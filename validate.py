from pymavlink import mavutil

# Connect to SITL (default UDP port)
mav = mavutil.mavlink_connection('udp:127.0.0.1:14550')

# Wait for a heartbeat from the copter
print("Waiting for heartbeat...")
mav.wait_heartbeat()
print(f"Heartbeat from system (system {mav.target_system} component {mav.target_component})")

# Example: Request vehicle mode
mode = mav.flightmode
print(f"Vehicle mode: {mode}")

# Add your own validation logic below, e.g. upload a mission, check params, etc.
# Example: Print attitude if available
try:
    msg = mav.recv_match(type='ATTITUDE', blocking=True, timeout=10)
    if msg:
        print(f"ATTITUDE: roll={msg.roll}, pitch={msg.pitch}, yaw={msg.yaw}")
    else:
        print("No ATTITUDE message received.")
except Exception as e:
    print(f"Error: {e}")
