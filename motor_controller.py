import serial
import time


class Arduino():
    def __init__(self):
        self.arduino = serial.Serial("/dev/ttyACM0", baudrate=9600)
        time.sleep(2)
        print("Init DOne")
        
    def send_message(self, msg):
        print(msg)
        msg = msg + '\n'
        while True:
            self.arduino.write(msg.encode('utf-8'))
            print("Message sent")
            # time.sleep(0.2)
            rec_msg = self.rec()

            if rec_msg == f"ACK{msg.strip()}":  
                print("✅ ACK received: ", rec_msg)
                break
            else:
                print("❌ ", rec_msg)
                # time.sleep(0.5)
    def rec(self):
        print("Message reader started")
        msg_decoded = self.arduino.readline().decode('utf-8').strip() 
        print(f"Message received: {msg_decoded}")
        return msg_decoded




if __name__ == '__main__':
    ardu = Arduino()
    ardu.send_message("MOTORSTART")
    time.sleep(10)
    ardu.send_message("MOTORSTOP")
    ardu.send_message("SETDIR 0")
    time.sleep(2)
    ardu.send_message("MOTORSTART")
    time.sleep(10)
    ardu.send_message("MOTORSTOP")
"""
OLD CODE BELOW
"""

# arduino = serial.Serial(port="/dev/ttyACM0", baudrate=9600)

# def send(msg):
#     msg = msg + '\n'
#     while True:
#         arduino.write(msg.encode('utf-8'))
#         # time.sleep(0.2)
#         rec_msg = rec()

#         if rec_msg == f"ACK{msg.strip()}":
#             print("✅ ACK received: ", rec_msg)
#             break
#         else:
#             print("❌ ", rec_msg)
#             # time.sleep(0.5)

# def rec():
#     msg_decoded = arduino.readline().decode('utf-8').strip() 
#     return msg_decoded


# time.sleep(2)
# print("🔗 Connection established")

# # send("SETFREQ 500")
# # time.sleep(2)
# send("MOTORSTART")
# time.sleep(5)
# send("MOTORSTOP")
# time.sleep(2)
# send("MOTORSTART")
# time.sleep(2)
# send("SETFREQ 500")
# time.sleep(2)
# send("SETFREQ 10000")
# time.sleep(5)
# send("MOTORSTOP")
# time.sleep(2)
# send("MOTORSTART")
# time.sleep(3)
# send("MOTORSTOP")
