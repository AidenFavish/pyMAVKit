from pymavlink import mavutil
mav = mavutil.mavlink_connection('tcp:127.0.0.1:5770')
print("Waiting for heartbeat...")
mav.wait_heartbeat()
print("Heartbeat received!")