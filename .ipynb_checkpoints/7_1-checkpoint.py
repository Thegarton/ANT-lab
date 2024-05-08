import RPi.GPIO as GPIO
import time
import numpy
import matplotlib.pyplot as plt
import datetime

def todecimal(a):
    return [int(x) for x in bin(a)[2:].zfill(8)]
    
def abc(num):
    return num/256 * 3.3

def num(l):
    s = (''.join(map(str,l)))
    return int(str(s),2)

def leds_sig(a):
    n = int(a/3.3*8)
    arr = [0, 0, 0, 0, 0, 0, 0, 0]
    while(n >= 0):
        arr[n]=1
        n-=1
    #print(arr)
    return arr[::-1]
DAC  = [8, 11, 7, 1, 0, 5, 12 ,6]
LED = [2,3,4,17,27,22,10,9]
comp = 14
troyka = 13 
GPIO.setmode(GPIO.BCM)

GPIO.setup(comp, GPIO.IN)
GPIO.setup(troyka, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup(DAC, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(LED, GPIO.OUT, initial=GPIO.LOW)

flag = False
begin = datetime.now()
end = datetime.now()
# counter of data field
cnt = 0
print('start of experement', begin)
try:
    with open('data.txt', 'w+') as f:
        while(True):
            signal = [0, 0, 0, 0, 0, 0, 0, 0]
            for i in range(8): 
                signal_temp = [g for g in signal]
                signal_temp[i] = 1
                value = GPIO.output(DAC, signal_temp)
                read_comp = GPIO.input(comp)
                if read_comp == 0:
                    signal = signal_temp
            print("entered value {:^3} -> valtage {:.2f}, DAC signal {}".format(num(signal), abc(num(signal)), signal))    
            if num(signal) <= 212:
                cnt += 1
                f.write(str(num(signal))+'\n')
                flag = True
            else:
                GPIO.setup(troyka, GPIO.OUT, initial = GPIO.LOW)
            if flag and num(signal) <= 160:
                cnt += 1    
                end = datetime.now()
                break
        GPIO.output(LED, leds_sig(abc(num(signal))))
finally:
    GPIO.cleanup()

#постройка схематичного графика
y = []
with open('data.txt') as f:
    temp = f.readline()
    y.append(int(temp))
x = np.arange(0,len(y),1)
plt.plot(x,y)

#запись данных конфигурации 
time_of_experement = end - begin
seconds = time_of_experement.total_seconds()
T = seconds/cnt
frec = 1/T
step = 3.3/256

with open('settings.txt', 'w+') as f:
    f.write(str(frec) + '\n')
    f.write(str(step) + '\n')

# вывод в данных в консоль
print('duration', seconds)
print('period', T)
print('frec', frec)
print('step', step)


