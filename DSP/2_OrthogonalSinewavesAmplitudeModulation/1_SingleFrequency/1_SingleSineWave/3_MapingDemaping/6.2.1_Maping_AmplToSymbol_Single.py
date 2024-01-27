# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 00:42:16 2023

@author: User
"""

import numpy as np
import matplotlib.pyplot as plt
from mapper_lib import ampl_to_symbol
pi = np.pi
SYMBOL_NR = [2, 4, 8]
Tx_amps = np.linspace(-1.5, 1.5, 100)
for symbol_nr in SYMBOL_NR:
    symbol_list = np.array([])
    for tx in Tx_amps:
        symbol = ampl_to_symbol(symbol_nr, tx)
        symbol_list = np.append(symbol_list, symbol)
    plt.plot(Tx_amps,symbol_list,'p-', label = f'symbol nr = {symbol_nr}')   
plt.grid()
plt.ylabel('Symbol')
plt.xlabel('Amplitude')
plt.show()