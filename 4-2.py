import RPi.GPIO as GPIO
import time
def todecimal(a):
    return [int(x) for x in bin(a)[2:].zfill(8)]
GPIO.setmode(GPIO.BCM)
dac = [8, 11,7,1,0,5,12,6]
GPIO.setup(dac, GPIO.OUT)

def isInt(value):
    try:
        num = int(value)
        return(True)
    except ValueError:
        print('not int')
        return False

def isFloat(value):
    try:
        if ('.' or ',') in value:
            num = float(value)
            return(True)
    except ValueError:
        print('not float')
        return False

def isPositive(value):
        if (isInt(value) or isFloat(value)) and not('-' in value):
            print('Positive')
            return(True)
        if '-' in value:
            print('Negativ')
            return False


period = float(input('type period: '))
# try:
#     while True:
#         for vertex in [0,1, 3, 7, 15, 31, 63,127,255]:
#             GPIO.output(dac, todecimal(vertex))
#             time.sleep(period/14)
#         for vertex in reversed([0,1, 3, 7, 15, 31, 63,127]):
#             GPIO.output(dac, todecimal(vertex))
#             time.sleep(period/14)
try:
    while True:
        for vertex in range(0,256):
            GPIO.output(dac, todecimal(vertex))
            time.sleep(period/255)
        for vertex in reversed(range(1,255)):
            GPIO.output(dac, todecimal(vertex))
            time.sleep(period/255)
finally:
    GPIO.output(dac, GPIO.LOW)
    GPIO.cleanup()
