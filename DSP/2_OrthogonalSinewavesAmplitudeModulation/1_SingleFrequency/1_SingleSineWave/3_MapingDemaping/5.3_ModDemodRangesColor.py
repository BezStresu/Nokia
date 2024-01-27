# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 00:59:16 2023

@author: User
"""
import numpy as np
import matplotlib.pyplot as plt
pi = np.pi
# PARAMETERS
TIME_VECTOR_SIZE = 80
AMPL_VECTOR = (1, 1.43, 1.85, 2.27, 2.69, 3.11, 3.53, 4)
# CALCULATION
t = np.linspace(0, 2*pi,TIME_VECTOR_SIZE, endpoint=False)
Carrier = np.sin(t)
Rx_amps = np.array([])
Tx_amps = np.array([])
Error_amps = np.array([])
NOISE_DEVIATION = 0.5
for i in range(TIME_VECTOR_SIZE):
    amp = AMPL_VECTOR[i%len(AMPL_VECTOR)]
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
plt.plot(Rx_amps[0::len(AMPL_VECTOR)], marker= 'p', linewidth=0, color='red')
plt.plot(Rx_amps[1::len(AMPL_VECTOR)], marker= 'p', linewidth=0, color='orange')
plt.plot(Rx_amps[2::len(AMPL_VECTOR)], marker= 'p', linewidth=0, color='green')
plt.plot(Rx_amps[3::len(AMPL_VECTOR)], marker= 'p', linewidth=0, color='blue')
plt.plot(Rx_amps[4::len(AMPL_VECTOR)], marker= 'p', linewidth=0, color='cyan')
plt.plot(Rx_amps[5::len(AMPL_VECTOR)], marker= 'p', linewidth=0, color='brown')
plt.plot(Rx_amps[6::len(AMPL_VECTOR)], marker= 'p', linewidth=0, color='yellow')
plt.plot(Rx_amps[7::len(AMPL_VECTOR)], marker= 'p', linewidth=0, color='purple')
plt.axhline(y=0,color='black')
plt.grid(axis='y')
plt.show()

print(Tx_amps)