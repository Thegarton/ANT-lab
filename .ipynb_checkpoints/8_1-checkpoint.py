import numpy as np 
import matplotlib.pyplot as plt 

y = []

#чтение данных
with open('data.txt') as f:
    for line in f:
        y.append(int(line[:-1]))
# чтение файла конфигурации
step = 0
period = 0

with open('settings.txt') as f:
    step = float(f.readline()[:-1])
    period = float(f.readline()[:-1])

y = np.array(y)
y = y * step
fig = plt.figure()
x = np.arange(0,len(y), 1) * period
ax = fig.add_axes([0.01, 0.1, 0.8, 0.8])
ax.set_title('График заряда и разряда конденсатора в RC')
#fig.set_dpi(300)
plt.minorticks_on()
ax.grid(which = 'major')
ax.grid(ls = 'dashed', alpha = 0.5, which = 'minor')
ax.set_ylabel(r'$U, \text{ Вольт}$',  fontsize = 12)
ax.set_xlabel(r'$t, \text{ c}$',  fontsize = 12)
plt.plot(x,y,label = 'U(t)')
plt.plot(x,y,"o", ms=5, markevery = 50)
ax.legend()
ax.text(5.1,2.2,'Время зарядки = 4,21 с')
ax.text(5.1,1.8,'Время разрядки = 5,65 с')
plt.xlim(0, 10)
plt.ylim(0, 4)
plt.show()