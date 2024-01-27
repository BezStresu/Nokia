import numpy as np
from mylib import rotate_vector as r_v
import matplotlib.pyplot as plt

v = [0, 1]

angle_list = []
dot_list = []

    
for angle in range(0, 361, 10):    
    
    angle_list.append(angle) 
    v_rot = r_v(v, angle)
    dot = np.dot(v, v_rot)
    dot_list.append(dot)
    
plt.plot(angle_list, dot_list, '-p')
plt.xlabel('Angle')
plt.ylabel('Dot product')
plt.grid()
plt.show()



