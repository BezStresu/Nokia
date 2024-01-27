import numpy as np
import matplotlib.pyplot as plt
pi = np.pi

# parameters
PERIOD_VECTOR_SIZE = 60
PERIOD_NUMBER = 5
# loading Rx vector from file and..
Rx = np.load('TxSignal.npy')
# .. ploting it
plt.plot(Rx)
plt.grid()
plt.show()
# spliting vector into time slots coresponding to single periods
RxPeriods = np.reshape(Rx,(5,60))
# decoding amplitudes of Rx time slots
# create amplitude list
Tx = np.array([])
for RxPeriod in RxPeriods:
    t = np.linspace(0, 2*pi,PERIOD_VECTOR_SIZE, endpoint=False)
    Ref  = np.sin(t)     
    dot  = np.dot(Ref, RxPeriod)
    new_period = PERIOD_VECTOR_SIZE / 2
    ampl = dot / new_period   
    Tx = np.append(Tx, ampl)
print(Tx)  # print list
    



