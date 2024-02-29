import numpy as np
import matplotlib.pyplot as plt
from mylib import myDFT
from scipy.io.wavfile import read

# loads samples from .wav file with exemplary DTFM signal
# adapt file path 
f_freq, samples = read(r'wav\d.wav')
samples = samples[:1024]
f = np.linspace(0, f_freq, len(samples), endpoint=False)

# use commenst to swith between myDTF and numpy DTF (FFT)
# fft = np.fft.fft(samples)
# real = fft.real
# imag = fft.imag
real, imag = myDFT(samples)

plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)
plt.plot(samples)
plt.title('Time Domain Signal')

plt.subplot(2, 1, 2)
plt.plot(f[1:], real[1:], label='Real part')
plt.plot(f[1:], imag[1:], label='Imaginary part')
plt.title('Frequency Domain')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')
plt.grid()
plt.legend()

# Adjust the axis to focus on the part of interest
# plt.xlim(0, sampling_freq/2)
# plt.ylim(-20000, 20000)

plt.tight_layout()
plt.show()

