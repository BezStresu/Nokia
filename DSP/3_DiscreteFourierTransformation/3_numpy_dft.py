import numpy as np
import matplotlib.pyplot as plt
from mylib import my_stem_plot

SAMPLE_NR = 10
FREQ = 3 
FREQ2 = 1

t = np.linspace(0, 2*np.pi, SAMPLE_NR, endpoint=False)
A1 = 1
A2 = 1/5
samples =  A1 * np.cos(t*FREQ) + A2*np.sin(t*FREQ2)
my_stem_plot(samples, f'samples, sin_f={FREQ}, a_sin={A1}, a_cos={A2}',y_range=(-6,7))

fft = np.fft.fft(samples)

my_stem_plot(fft.real,'dft_real',y_range=(-6,7))
my_stem_plot(fft.imag,'dft_imag',y_range=(-6,7))

