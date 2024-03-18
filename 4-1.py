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
try:
    while True:
        num = input('type value between 0 - 255: ')
        if num == 'q':
            break
        if isFloat(num) and isPositive(num):
            num = round(float(num))        
        elif isInt(num) and isPositive(num):
            num = int(num)

        if not(isinstance(num, (str))):
            if  num > 255:
                print('Input error, type value between 0 - 255')
                continue    
            GPIO.output(dac, todecimal(num))
            time.sleep(0.1)
            print(("{:.3f}V".format(3.3/256*num)))

finally:
    GPIO.output(dac, GPIO.LOW)
    GPIO.cleanup()
