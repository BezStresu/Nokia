import numpy as np
import matplotlib.pyplot as plt
from mylib import my_stem_plot

SAMPLE_NR = 10
FREQ = 3 

t = np.linspace(0, 2*np.pi, SAMPLE_NR, endpoint=False)

samples =  np.sin(t*FREQ) #+ np.cos(t)
# my_stem_plot(...,f'samples, sin_f={FREQ}',y_range=(-6,7))

# fft = np.fft.fft(...)
# my_stem_plot(...,'real',y_range=(-6,7))
# my_stem_plot(...,'imag',y_range=(-6,7))

