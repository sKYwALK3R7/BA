from usb_rs import Usb_rs as USB_HIOKI
import numpy as np
import time

class LCR():
    def __init__(self):
        self.lcr = USB_HIOKI()
        self.lcr.open("/dev/ttyACM1", 9600)
        time.sleep(2)
        # set device to LCR-meter mode
        self.lcr.SendQueryMsg(':MODE LCR', 1)
        print("MODE LCR set ...")
        # set trigger to internal mode
        self.lcr.SendQueryMsg(':TRIGger INTernal', 1)
        print("MODE Trigger set ... ")
        # set Measurement Signal Level to voltage
        self.lcr.SendQueryMsg(':LEVel V', 1)
        print("Level V set ... ")
        # set  the open-circuit voltage level to 1.0 V
        self.lcr.SendQueryMsg(':LEVel:VOLTage 1.000', 1)
        print("Level Voltage 1 set ...")
        # set  DC bias function to enable / on
        self.lcr.SendQueryMsg(':DCBias ON', 1)
        print("DC Bias set ... ")
        # set  DC bias level to 2.5V
        self.lcr.SendQueryMsg(':DCBias:LEVel 2.500', 1)
        print("DC Bias Level set ...")
        # FREQUENCY 100E3 = 100 kHz
        self.lcr.SendQueryMsg(':FREQUENCY 100000', 1)
        print("Frequency set ...")
        # set parameter1: Z
        self.lcr.SendQueryMsg(':PARameter1 Z', 1)
        print("Z set ..")
        # set parameter2: RP
        self.lcr.SendQueryMsg(':PARameter2 RP', 1)
        print("Rp set ... ")
        # set parameter3: CP
        self.lcr.SendQueryMsg(':PARameter3 CP', 1)
        print("Cp set ...")
        # set parameter4: Phase
        self.lcr.SendQueryMsg(':PARameter4 Phase', 1)
        print("Phase set ...")

        # return True
    
    def make_measurement(self):
        return self.lcr.SendQueryMsg(':MEASURE?', 1)
                


# if __name__ == "__main__":
#     lcr = LCR()
#     time.sleep(1)
#     while True:
#         measure = []
#         measure.append(lcr.make_measurement())
#         formatted_values = measure[0].replace(" ", "").split(',')
#         lcr_str = "\t".join(formatted_values) + '\t'
#         print(lcr_str)