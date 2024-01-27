import numpy as np
from mylib import rotate_vector as r_v

dot_product = 0
blue = [0, 1]
for i in range(0, 361, 10):
    green = [0, 1]
    green_rotated = r_v(green, i)
    dot_product = np.dot(green_rotated, blue)
    print(f'{i:03d}: {dot_product :+0.3f}')


