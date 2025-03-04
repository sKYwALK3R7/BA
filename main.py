from lcr_meter import LCR
import time
from load_cell import LoadCell
from arduino_com import Arduino
import datetime
import sys 
import select

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Welcome to this measurement environment\n\n")
time.sleep(0.2)
print("Please do not touch anything. Components will be initalized")
hioki = LCR()
time.sleep(2)
print("LCR INITALIZED")
load_cell = LoadCell()
time.sleep(2)
print("LOAD CELL INITALIZED")
ardu_one = Arduino()
time.sleep(2)
print("MOTOR CONTROLLER INITALIZED")

file = open(r"/home/wenzler/BA_Wenzler/measurement_data.tsv", "a")
file.write("TimeStamp\tImpedance_Z\tResistance_Rp\tCapacity_Cp\tPhase\tForce\n")
print("DATA FILE OPENED..")
def make_measurement():
    time_stamp = datetime.datetime.now()
    str_time_stamp = time_stamp.strftime("%Y-%m-%d_%H-%M-%S.%f")[:-3]
    measure = []
    measure.append(hioki.make_measurement())
    formatted_values = measure[0].replace(" ", "").split(',')
    lcr_str = "\t".join(formatted_values) + '\t'
    force = load_cell.getForce()
    print(f"{str_time_stamp}\t{lcr_str}\t{force:.5f}")
    file.write(f"{str_time_stamp}\t{lcr_str}\t{force:.5f}\n")
    file.flush()


if __name__ == "__main__":
    print("Press ENTER to start the motor to get it into the right position. \nPress ENTER again to stop it\n")
    enter = input()
    if enter == "":
        ardu_one.send_message("SETFREQ 500")
        time.sleep(1)
        ardu_one.send_message("MOTORSTART")
    else: 
        print("Wrong input")
    enter = input()
    if enter == "":
        ardu_one.send_message("MOTORSTOP")
    else: 
        print("Wrong input")
    print("Please place the DUT and press ENTER when finished.")
    enter = input()
    if enter == "":
        pass
    else: 
        print("Wrong input")
    print("Now the calibration of the loadCell will start, dont touch anything!\nPress ENTER to start.")
    enter = input()
    if enter == "":
        print("Calibrating Load Cell")
        load_cell.calibrate()
    else: 
        print("Wrong input")
    print("Load Cell Calibrated")
    print("Ready to start measurement")
    print("Press ENTER to start")
    print("Press ENTER again to stop")
    enter = input()
    if enter =="":
        # ardu_one.send_message("SETFREQ 10000")
        time.sleep(1)
        ardu_one.send_message("MOTORSTART")
        time.sleep(0.5)
        run = True
        while run: 
            make_measurement()
            # time.sleep(0.1)
            i, o , e = select.select([sys.stdin], [], [], 0.1)
            if i:
                enter = sys.stdin.readline().strip()
                if enter == "":
                    run = False
                    ardu_one.send_message("MOTORSTOP")
                    file.close()
                
            else:
                continue
    else:
        print("Wrong input")
    file.close()
    print("Measurement Done")
    print(f"MAX FORCE: {load_cell.getMaxForce()}")
