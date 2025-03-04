from arduino_com import Arduino
import time

ardu_one = Arduino()
time.sleep(2)
ardu_one.send_message("SETFREQ 500")
time.sleep(1)
ardu_one.send_message("MOTORSTART")
enter = input()
if enter == "":
    ardu_one.send_message("MOTORSTOP")