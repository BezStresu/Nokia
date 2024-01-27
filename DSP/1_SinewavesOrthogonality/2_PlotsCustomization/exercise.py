import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

t = np.linspace(0, 10, 24, endpoint=False)
A1 = 1.4
p1 = np.pi
sin = A1 * np.sin(t*np.pi/3 + p1)
A2 = 2.8
p2 = 0
T = 0.5
tri = A2 * signal.sawtooth(t+p2, T)
sum = sin + tri
plt.plot(t,sum,'--', label='sum', color='brown')
plt.plot(t,tri,'-p', label='triangle', color='green')
plt.plot(t,sin, 'p', label='sinusoid', color='blue')
plt.title()
plt.xlabel('time[s]')
plt.ylabel('amplitude[a.u.]')
plt.xlim(0,10)
plt.ylim(-6,6)
plt.axhline(y=0,color='red')
plt.grid()
plt.legend(loc = 'upper right')
plt.show()
