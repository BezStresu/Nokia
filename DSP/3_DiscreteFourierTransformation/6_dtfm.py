import numpy as np
import matplotlib.pyplot as plt
from mylib import myDFT
from scipy.io.wavfile import read

# loads samples from .wav file with exemplary DTFM signal
# adapt file path 
samples = read(r'wav\d.wav')
samplig_freq = samples[0]
samples = samples[1]
samples = samples[:1024]
plt.plot(samples)

# use commenst to swith between myDTF and numpy DTF (FFT)
fft = np.fft.fft(samples)
real = fft.real
imag = fft.imag

real, imag = myDFT(samples)
plt.plot(real,label='myDFT real')
plt.plot(imag,label='myDFT imag')

# plt.plot(real,label='fft real')
# plt.plot(imag,label='fft imag')
plt.title('4 d.wav')
plt.grid()
plt.legend()

#could be usefull for zooming
# plt.xlim(0,100)
# plt.ylim(-20_000,2_0000)






