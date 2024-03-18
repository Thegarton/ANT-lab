import RPi.GPIO as GPIO
import time 
leds = [9,10,22,27,17,4,3,2]
aux = [21,20,26,16,19,25,23,24]
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(leds, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(aux, GPIO.IN)
while(True):
    for i in range(len(leds)):
        if GPIO.input(aux[i]) == 0:
            GPIO.output(leds[i], GPIO.LOW)
        else:
            GPIO.output(leds[i], GPIO.HIGH)


