import numpy as np
import matplotlib.pyplot as plt

def my_stem_plot(y,title,y_range=None):
    x = np.arange(len(y))    
    plt.stem(x,y,'-p')

    plt.xticks(x)
    
    if y_range:
        plt.ylim(y_range)
        plt.yticks(np.arange(*y_range))
    
    plt.grid()
    plt.title(title)
    fig = plt.gcf()
    fig.set_size_inches(4, 3.6)
    plt.show()
    
def myDFT(samples):
    N = len(samples)
    dft = list()
    for f in range(N):
        dft.append(np.dot(samples, np.exp(-2j * np.pi * f * np.arange(N) / N)))   
        
    real = np.real(dft)
    imag = np.imag(dft)
   
    return real, imag
    