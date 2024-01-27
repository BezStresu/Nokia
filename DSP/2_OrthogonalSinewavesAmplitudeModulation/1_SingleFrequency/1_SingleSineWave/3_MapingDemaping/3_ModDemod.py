import numpy as np
import matplotlib.pyplot as plt
pi = np.pi
# PARAMETERS
TIME_VECTOR_SIZE = 60
AMPL_VECTOR = (1.2, -3.4, 4.5, -1.2, 3.4)
# CALCULATION
t = np.linspace(0, 2*pi,TIME_VECTOR_SIZE, endpoint=False)
Carrier = np.sin(t)
Tx = np.array([])
# modulation
for amp in AMPL_VECTOR:
    Tx = np.append(Tx, amp*Carrier)
# channel
Rx=Tx # ideal one    
# demodulation
RxPeriods = np.reshape(Rx,(5,60))
amplitudes_1 = np.array([])
for RxPeriod in RxPeriods:
    Ref  = np.sin(t)     
    dot  = np.dot(Ref, RxPeriod)
    ampl = dot / (TIME_VECTOR_SIZE/2)   
    amplitudes_1 = np.append(amplitudes_1, ampl)
# PRESENTATION  
# Tx plot
plt.plot(Rx)
plt.xlim(0, 320)
plt.axhline(y=0,color='black')
plt.grid(axis='y')
plt.show()
#  
print(f'received amplitudes: {amplitudes_1}')


