import numpy as np
import matplotlib.pyplot as plt
from mylib import my_stem_plot

SAMPLE_NR = 10
SIN_FREQ = 3 

t = np.linspace(0, 2*np.pi, SAMPLE_NR, endpoint=False)
A = 1
samples =  A * np.cos(t*SIN_FREQ)

print(len(samples))
my_stem_plot(samples,f'samples, f_sig={SIN_FREQ}', y_range=(-6,7))

real = list()
for f in range(SAMPLE_NR):
    real.append(np.dot(samples, np.cos(t*f)))   
    
my_stem_plot(real,'my DFT real',y_range=(-6,7))



