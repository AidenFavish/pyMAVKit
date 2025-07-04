import time

from mav_device import MAVDevice


device = MAVDevice("udp:127.0.0.1:14550")

while True:
    print(time.ctime())
    for msg_name, payload in device.receiver.history_dict.items():
        if len(payload) > 1:
            delta_sum = 0
            for i in range(len(payload) - 1):
                delta_sum += payload[i][0] - payload[i+1][0]
            period = delta_sum / 1000 / (len(payload) - 1)
            freq = 1/period
        else:
            freq = -1
        print(f"{msg_name:<25} stored messages: {len(payload):<10} freq: {freq:.4f} hz")
    print("", flush=True)
    time.sleep(1)
