import pymavlink.dialects.v20.all as dialect

from pymavkit.mav_message import MAVMessage

MAV_RESULT = ["ACCEPTED", "TRY AGAIN LATER", "DENIED", "UNSUPPORTED", "FAILED", "IN PROGRESS", 
              "CANCELLED", "COMMAND LONG ONLY", "COMMAND INT ONLY", "UNSUPPORTED MAV FRAME"]

class CommandAck(MAVMessage):
    def __init__(self):
        super().__init__("COMMAND_ACK")
        self.command_id = -1
        self.result = "UNKNOWN"

    def decode(self, msg):
        self.command_id = msg.command
        self.result = MAV_RESULT[msg.result]

    def __repr__(self):
        return f"(COMMAND_ACK) timestamp: {self.timestamp} ms, command_id: {self.command_id}, result: {self.result}"
