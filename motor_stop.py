from arduino_com import Arduino
import time

ardu_one = Arduino()
time.sleep(2)
ardu_one.send_message("MOTORSTOP")

