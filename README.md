# pyMAVKit

## Set Up Environment
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## How to Use
1. Create a `MAVDevice` object to connect to the drone
```python
from pymavkit import MAVDevice

udp_device = MAVDevice("udp:127.0.0.1:14550")
serial_device = MAVDevice("/dev/ttyACM0")
```

2. Add listeners to monitor telemetry
```python
from pymavkit.messages import Heartbeat, LocalPositionNED

# Monitors heartbeat and local position
heartbeat = device.add_listener(Heartbeat())
local_pos = device.add_listener(LocalPositionNED())

while True:
    print(heartbeat)
    print(local_pos.vx)
```

3. Run protocols
```python
from pymavkit.protocols import HeartbeatProtocol, SetModeProtocol
from pymavkit.messages import FlightMode

# Sends periodic heartbeats from device and sets mode
hb_protocol = device.run_protocol(HeartbeatProtocol())  # will auto send at 1 hz
set_guided = device.run_protocol(SetModeProtocol(FlightMode.GUIDED))
```


## How to Develop

### Create a MAVMessage:
1. Create a class for your message in the `messages` folder
2. Inherit from the `MAVMessage` class
3. In the `super().__init__` make sure to pass in the name of the message that is the same it appears in the mavlink documentation all caps seperated by _
4. If you want this message to be able to be recieved from the flight controller, override the `decode` function
5. If you want this message to be able to be sent to the flight controller, override the `encode` function
6. (Optional) Override the `__repr__` function to assist in debugging

### Create a MAVProtocol:
Not necessary if you are only receiving a particular message, but neccessary if you want to send something
1. Create a class for your protocol in the `protocols` folder. For convention append "Protocol" to the end of the name.
2. Override the `run` function using `sender.send_msg` and `receiver.wait_for_msg` with `MAVMessage` to build your protocol

## ✅ Guaranteed bug-free
Developed entirely at Ballmer’s Peak 🏔️. No testing necessary, bugs can’t survive up here.
