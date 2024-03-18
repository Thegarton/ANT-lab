import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(9, GPIO.OUT)
p= GPIO.PWM(9, 1000)
p.start(0)

GPIO.setup(21, GPIO.OUT)
p_2 = GPIO.PWM(21, 1000)
p_2.start(0)
try:
    while True:
        dc = int(input('type value between 0 - 100: '))
        p.ChangeDutyCycle(dc)
        p_2.ChangeDutyCycle(dc)
        time.sleep(0.1)
        print(("{:.3f}V".format(3.3/100*dc)))
finally:
    GPIO.cleanup()
    p.stop()