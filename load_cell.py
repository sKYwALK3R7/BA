import time
import sys
from  hx711py.hx711 import HX711

class LoadCell():
    def __init__(self):
        print("Hello")
        self.hx = HX711(5, 6)
        print("Hello2")
        self.hx.set_reading_format("MSB", "MSB")
        print("Hello3")
        self.hx.set_reference_unit(1)
        print("Hello4")
        self.hx.reset()
        print("Hello5")
        self.denominator = -4502.847332
        self.forceMax = 0
        self.offset = -99999999

    def calibrate(self):
        print("Beginning")
        self.hx.reset()
        self.hx.reset()
        sum = 0
        for _ in range (50):
            print(_)
            sum += self.hx.read_long()
            self.hx.power_down()
            self.hx.power_up()
            time.sleep(0.1)
        self.offset = sum/50
        # time.sleep(2)

    def getForce(self):
        force = (self.hx.read_long() - self.offset)/ self.denominator
        self.hx.power_down()
        self.hx.power_up()
        time.sleep(0.1)
        if force > self.forceMax: self.forceMax = force
        return force
    
    def getMaxForce(self):
        return self.forceMax
    
    def cleanAndExit():
        sys.exit()
    


"""
OLD CODE BELOW
"""

if __name__ == "__main__":
    lc = LoadCell()
    print("Initalized")
    lc.calibrate()
    print("Calibrated")
    for _ in range (100):
        force = lc.getForce()
        print(force)




# def cleanAndExit():
#     print("Cleaning...")
        
#     print("Bye!")
#     sys.exit()

# hx = HX711(5, 6)
# hx.set_reading_format("MSB", "MSB")

# referenceUnit = 1
# hx.set_reference_unit(referenceUnit)

# hx.reset()
# hx.tare()
# print("Tare done! Add weight now...")

# # denominator to convert to Newton
# denominator = -4502.847332 
# array = []
# cnt = 0
# summe = 0
# force_max = 0
# while True:
#     try:
#         # These three lines are usefull to debug wether to use MSB or LSB in the reading formats
#         # for the first parameter of "hx.set_reading_format("LSB", "MSB")".
#         # Comment the two lines "val = hx.get_weight(5)" and "print val" and uncomment these three lines to see what it prints.
        
#         # np_arr8_string = hx.get_np_arr8_string()
#         # binary_string = hx.get_binary_string()
#         # print(binary_string + " " + np_arr8_string)
        
#         # Prints the weight. Comment if you're debbuging the MSB and LSB issue.
#         # val = hx.get_weight(5)
#         # print(val)
#         val = hx.read_long()  
#         if (cnt <= 20):
#             summe += val
#             cnt += 1
#             print(val)
#             hx.power_down()
#             hx.power_up()
#             time.sleep(0.1) 
#         else:
#             mid = summe / cnt
#             val = val - mid
#             array.append(val)
#             force = val/denominator
#             if force > force_max:
#                 force_max = force
#             print(f"MEAN:\t\t{(sum(array)/len(array))}")
#             print(f"VALU:\t\t{val}")
#             print(f"FORCE:\t\t{val/denominator:.5f} N")
#             print(f"FORCE MAX:\t{force_max:.5f}")
#             hx.power_down()
#             hx.power_up()
#             time.sleep(0.1) 
        

#         # To get weight from both channels (if you have load cells hooked up 
#         # to both channel A and B), do something like this
#         #val_A = hx.get_weight_A(5)
#         #val_B = hx.get_weight_B(5)
#         #print "A: %s  B: %s" % ( val_A, val_B )

#         hx.power_down()
#         hx.power_up()
#         time.sleep(0.1)

#     except (KeyboardInterrupt, SystemExit):
#         cleanAndExit()
