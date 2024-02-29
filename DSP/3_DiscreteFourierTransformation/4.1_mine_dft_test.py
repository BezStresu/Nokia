import numpy as np
import matplotlib.pyplot as plt
from mylib import my_stem_plot, myDFT

SAMPLE_NR = 10
SIN_FREQ = 3 

t = np.linspace(0, 2*np.pi, SAMPLE_NR, endpoint=False) 
samples =  np.cos(t*SIN_FREQ)
my_stem_plot(samples,f'samples, f_sig={SIN_FREQ}', y_range=(-6,7))

real, imag = myDFT(samples)

my_stem_plot(real,'my DFT real',y_range=(-6,7))
my_stem_plot(imag,'my DFT imag',y_range=(-6,7))



