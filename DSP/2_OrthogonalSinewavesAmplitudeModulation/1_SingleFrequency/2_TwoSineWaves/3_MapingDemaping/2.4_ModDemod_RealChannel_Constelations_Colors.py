import numpy as np
import matplotlib.pyplot as plt
pi = np.pi

# PARAMETERS
TIME_VECTOR_SIZE = 60

AMPL_VECTOR_SIN = (1,-1, 1,-1)
AMPL_VECTOR_COS = (1, 1,-1,-1)


# CALCULATION
t = np.linspace(0, 2*pi,TIME_VECTOR_SIZE, endpoint=False)
carrier_sin = ref_sin = np.sin(t) 
carrier_cos = ref_cos = np.cos(t) 
amplitudes_sin = list()
amplitudes_cos = list()
NOISE_DEVIATION = 6
TRANSMISON_NR = 10

for i in range(TRANSMISON_NR):
    for j, (ampl_sin, ampl_cos) in enumerate(zip(AMPL_VECTOR_SIN, AMPL_VECTOR_COS)):
        
        # modulation
        Tx = (ampl_sin*carrier_sin) + (ampl_cos*carrier_cos)     
        
        # real channel
        Rx = Tx + np.random.normal(0, NOISE_DEVIATION, len(Tx))
            
        # demodulation
        ampl_sin_rx = (np.dot(Rx,ref_sin)/TIME_VECTOR_SIZE)*2  
        amplitudes_sin.append(ampl_sin_rx)
        
        ampl_cos_rx = (np.dot(Rx,ref_cos)/TIME_VECTOR_SIZE)*2  
        amplitudes_cos.append(ampl_cos_rx)

        plt.scatter(ampl_cos_rx, ampl_sin_rx, color=('red','orange','green','blue')[j%4])
        
plt.title('RX amplitudes')
plt.xlim(-4, 4)
plt.ylim(-4, 4)
plt.xlabel('cos ampl')
plt.ylabel('sin ampl')
plt.axvline(0, color = 'black')
plt.axhline(0, color = 'black')
plt.grid()
plt.show()
