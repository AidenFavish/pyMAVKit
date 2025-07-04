import time

from mav_device import MAVDevice


device = MAVDevice("udp:127.0.0.1:14550")

while True:
    print(device.receiver.history_dict)
    print("", flush=True)
    time.sleep(1)
