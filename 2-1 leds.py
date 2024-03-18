import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
leds = [9,10,22,27,17,4,3,2]
leds.reverse()
GPIO.setup(leds, GPIO.OUT, initial = GPIO.LOW)
for j in range(3):
    for i in range(len(leds)):
        GPIO.output(leds[i], GPIO.HIGH)
        time.sleep(0.2)
        GPIO.output(leds[i], GPIO.LOW)
        time.sleep(0.2)
GPIO.output(leds, GPIO.OUT, initial = GPIO.LOW)
GPIO.cleanup()
