import numpy as np
import matplotlib.pyplot as plt
from mylib import my_stem_plot, myDFT

SAMPLE_NR = 10

t = np.linspace(0, 2*np.pi, SAMPLE_NR, endpoint=False) 
samples = np.cos(1*t)* 2/5 + np.sin(4*t) * 4/5
my_stem_plot(samples, f'samples', y_range=(-6, 7))

real, imag = myDFT(samples)
my_stem_plot(real, 'real', y_range=(-6, 7))
my_stem_plot(imag, 'imag', y_range=(-6, 7))

fft = np.fft.fft(samples)
my_stem_plot(fft.real, 'fft real', y_range=(-6, 7))
my_stem_plot(fft.imag, 'fft imag', y_range=(-6, 7))