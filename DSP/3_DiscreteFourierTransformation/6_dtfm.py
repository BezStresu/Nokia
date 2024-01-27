import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import read

# loads samples from .wav file with exemplary DTFM signal
# adapt file path 
samples = read(r'wav\a.wav')
samplig_freq = samples[0]
samples = samples[1]
samples = samples[:1024]
plt.plot(samples)

# use commenst to swith between myDTF and numpy DTF (FFT)
fft = np.fft.fft(samples)
real = fft.real
imag = fft.imag
# real, imag = myDFT(samples)

plt.plot(real,label='real')
plt.plot(imag,label='imag')
plt.grid()
plt.legend()

#culd be usefool for zooming
# plt.xlim(0,100)
# plt.ylim(-20_000,2_0000)






