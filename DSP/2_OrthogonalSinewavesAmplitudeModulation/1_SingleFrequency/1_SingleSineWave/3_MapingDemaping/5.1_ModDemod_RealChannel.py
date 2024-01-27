# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 02:02:58 2023

@author: User
"""
import numpy as np
import matplotlib.pyplot as plt
pi = np.pi
# PARAMETERS
TIME_VECTOR_SIZE = 60
AMPL_VECTOR = (1.2, -3.4, 4.5, -1.2)
# CALCULATION
t = np.linspace(0, 2*pi,TIME_VECTOR_SIZE, endpoint=False)
Carrier = np.sin(t)
Rx_amps = np.array([])
Tx_amps = np.array([])
Error_amps = np.array([])

for amp in AMPL_VECTOR:
# modulation
    Tx = amp*Carrier
    Tx_amps = np.append(Tx_amps, Tx)
# channel
    # normal distribution noise 
    noise = np.random.normal(0, 0.3, len(Tx))
    Rx = Tx + noise
# demodulation
    Ref  = np.sin(t)     
    dot  = np.dot(Ref, Rx)
    ampl = dot / (TIME_VECTOR_SIZE/2)   
    Rx_amps = np.append(Rx_amps, ampl)
# errors
    error = amp - ampl
    Error_amps = np.append(Error_amps, error)
# PRESENTATION  
# Tx plot
plt.plot(Rx)
plt.axhline(y=0,color='black')
plt.grid(axis='y')
plt.show()
#  
print(f'received amplitudes: {Rx_amps}')
print(f'error amplitudes: {Error_amps}')
