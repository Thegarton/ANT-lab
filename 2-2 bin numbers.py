import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
DAC = [6, 12,5,0,1,7,11,8]
DAC.reverse()
number = [1,1,1,1,1,1,1,1]
GPIO.setup(DAC, GPIO.OUT, initial = GPIO.LOW)
GPIO.output(DAC, number)
time.sleep(15)
GPIO.setup(DAC, GPIO.OUT, initial = GPIO.LOW)
GPIO.cleanup()