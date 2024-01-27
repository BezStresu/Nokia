# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 02:25:43 2023

@author: User
"""
import numpy as np
import matplotlib.pyplot as plt
from mapper_lib import symbol_to_ampl, ampl_to_symbol 

# PARAMETERS
TIME_VECTOR_SIZE = 60
TRANSMISIONS_NR = 1000
numN = 15
NOISE_DEVIATION_list = np.linspace(0, 2, numN)
t = np.linspace(0, 2*np.pi,TIME_VECTOR_SIZE, endpoint=False)
Carrier = np.sin(t) 
Ref     = Carrier
for SYMBOL_NR in 2,4,8:
    symbols_tx = np.random.randint(0,SYMBOL_NR,TRANSMISIONS_NR)
    error_num_list = list()   
    for NOISE_DEVIATION in NOISE_DEVIATION_list: 
        symbols_rx = list()
        for symbol in symbols_tx:        
            # modulation
            ampl = symbol_to_ampl(SYMBOL_NR, symbol)
            Tx = ampl*Carrier        
            # real channel
            noise = np.random.normal(0, NOISE_DEVIATION, TIME_VECTOR_SIZE)
            Rx = Tx + noise  
            # demodulation
            ampl = (np.dot(Rx,Ref)/TIME_VECTOR_SIZE)*2  
            symbol = ampl_to_symbol(SYMBOL_NR, ampl)
            symbols_rx.append(symbol)
            
        symbols_rx = np.array(symbols_rx)
        errors = symbols_rx != symbols_tx
        error_num = sum(symbols_rx != symbols_tx)
        error_num_list = np.append(error_num_list, error_num)     
    plt.plot(error_num_list, 'p-', label = f'symbol nr = {SYMBOL_NR}')
plt.xlabel('noise deviation')
plt.ylabel('error nr')
plt.legend()
plt.grid()
plt.show()