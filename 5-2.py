import RPi.GPIO as GPIO
import time
import numpy

def todecimal(a):
    return [int(x) for x in bin(a)[2:].zfill(8)]

def abc(num):
    return num/256 * 3.3

def num(l):
    s = (''.join(map(str,l)))
    return int(str(s),2)

DAC  = [8, 11, 7, 1, 0, 5, 12 ,6]
comp = 14
troyka = 13 
GPIO.setmode(GPIO.BCM)

GPIO.setup(comp, GPIO.IN)
GPIO.setup(troyka, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup(DAC, GPIO.OUT, initial=GPIO.LOW)

try:
    while(True):
        signal = [0, 0, 0, 0, 0, 0, 0, 0]
        for i in range(8): 
            signal_temp = [g for g in signal]
            signal_temp[i] = 1
            # print(signal)
            # print(signal_temp)
            value = GPIO.output(DAC, signal_temp)
            time.sleep(0.001)
            read_comp = GPIO.input(comp)
            if read_comp == 0:
                signal = signal_temp
                # print(num(signal))
                # print("entered value {:^3} -> valtage {:.2f}, DAC signal {}".format(num(signal), abc(num(signal)), signal))
        print("entered value {:^3} -> valtage {:.2f}, DAC signal {}".format(num(signal), abc(num(signal)), signal))    
finally:
    GPIO.cleanup()
