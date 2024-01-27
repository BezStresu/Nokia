# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 02:19:31 2023

@author: User
"""
import numpy as np
import matplotlib.pyplot as plt
pi = np.pi
# PARAMETERS
TIME_VECTOR_SIZE = 100
AMPL_VECTOR = (1.2, -3.4, 4.5, -1.2)
# CALCULATION
t = np.linspace(0, 2*pi,TIME_VECTOR_SIZE, endpoint=False)
Carrier = np.sin(t)
Rx_amps = np.array([])
Tx_amps = np.array([])
Error_amps = np.array([])
NOISE_DEVIATION = 0.5
for i in range(TIME_VECTOR_SIZE):
    amp = AMPL_VECTOR[i%4]
# modulation
    Tx = amp*Carrier
    Tx_amps = np.append(Tx_amps, Tx)
# channel
    # normal distribution noise 
    noise = np.random.normal(0, NOISE_DEVIATION, len(Tx))
    Rx = Tx + noise
# demodulation
    Ref  = np.sin(t)     
    dot  = np.dot(Ref, Rx)
    ampl = dot / (TIME_VECTOR_SIZE/2)   
    Rx_amps = np.append(Rx_amps, ampl)
# PRESENTATION  
# Tx plot
plt.scatter(t, Rx_amps, marker= 'p')
plt.axhline(y=0,color='black')
plt.grid(axis='y')
plt.show()
