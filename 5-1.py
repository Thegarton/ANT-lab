import RPi.GPIO as GPIO
import time

def todecimal(a):
    return [int(x) for x in bin(a)[2:].zfill(8)]

def abc(num):
    return num/256 * 3.3

DAC  = [8, 11, 7, 1, 0, 5, 12 ,6]
comparator = 14
troyka = 13 
GPIO.setmode(GPIO.BCM)

GPIO.setup(comparator, GPIO.IN)
GPIO.setup(troyka, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup(DAC, GPIO.OUT, initial=GPIO.LOW)

try:
    while(True):
            for i in range(256):
                signal = todecimal(i)
                value = GPIO.output(DAC, signal)
                time.sleep(0.05)
                read_comp = GPIO.input(comparator)
                if read_comp == 1:
                    print("entered value {:^3} -> valtage {:.2f}, DAC signal {}".format(i, abc(i), signal))
                    break
finally:
    GPIO.cleanup()
    GPIO.setup(DAC, GPIO.OUT, initial=GPIO.LOW)