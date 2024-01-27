import numpy as np
import matplotlib.pyplot as plt

INFINIT_SAMPLE_RATE = 100 # infinity sample rate imitation (analog signal)
FINIT_SAMPLE_RATE = 10    # real (finit) sample rate

SIN_FREQ = 1 

t_ideal    = np.linspace(0, 2*np.pi, ..., endpoint=False)
t_sampled  = np.linspace(0, 2*np.pi, ..., endpoint=False)

sin_ideal   =  np.sin(...)
sin_sampled =  np.sin(...)

plt.plot(...)
plt.plot(...)
plt.axhline(0,color='black', linewidth=1)
plt.title(f'sine frequency = {SIN_FREQ}')
plt.legend()





