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
numN = 10
NOISE_DEVIATION_list = np.linspace(0, 2, numN)
SYMBOL_NR = 8
NOISE_DEVIATION = 1
t = np.linspace(0, 2*np.pi,TIME_VECTOR_SIZE, endpoint=False)
Carrier = np.sin(t) 
Ref     = Carrier
# TRANSMISION-RECEPTION
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

print(f'\n SYMBOL_NR = {SYMBOL_NR}\n\n noise dev : error nr')
for i in range(0, numN):
    print(f' {round(NOISE_DEVIATION_list[i], 2)} : {int(error_num_list[i])}')