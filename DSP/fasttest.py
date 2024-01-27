import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(0, 9, 500)

y = -x/(9 - pow(x, 2))

plt.plot(x, y)
plt.ylim(-100, 100)
plt.grid()
plt.show()