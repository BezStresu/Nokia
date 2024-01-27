import numpy as np
import matplotlib.pyplot as plt
pi = np.pi
t = np.linspace(0, 2*pi,30, endpoint=False)
Ref = np.sin(t)
phase_list = []
dot_list = []
phase = np.linspace(0, 3, 10)

for i in phase:
    phase_list.append(i)
    Shifted = np.sin(t+i)
    dot_product = np.dot(Ref, Shifted)
    dot_list.append(dot_product)

plt.plot(phase_list, dot_list, '-p')
plt.title('Relationship between dot product and phase shift')
plt.xlabel('Phase shift')
plt.ylabel('Dot product')
plt.grid()
plt.show()
