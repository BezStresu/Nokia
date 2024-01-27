import numpy as np
import matplotlib.pyplot as plt
pi = np.pi

# PARAMETER
PHASE_SHIFT = 3.3

# VECTORS
t = np.linspace(0, 2*pi,30, endpoint=False)

Ref = np.sin(t)
Shifted = np.sin(t+ PHASE_SHIFT)
Ref_mult_Shifted = Ref * Shifted
dot_product = np.dot(Ref, Shifted) 

# PLOTS (HINT: use separate plots, not one with grid)
# components
plt.plot(t, Ref, '-p')
plt.plot(t, Shifted, '-p', color = 'g')
plt.title('Components')
plt.legend(['Ref', 'Shifted'], loc = 'upper right')
plt.grid()
plt.show()
# multiplication, HINT: use "stem" function for ploting

markerline, stemlines, baseline = plt.stem(t, Ref_mult_Shifted, markerfmt='o', label='Ref_mult_Shifted')
plt.setp(markerline, 'color', 'orange')
plt.ylim(-1, 1)
plt.legend(loc = 'lower left')
plt.grid()
plt.show()

# print phase shift and dot product value

#print('Phase shift=', round(PHASE_SHIFT,2), '\nDot product=', round(dot_product,2))
print('Dot product=', round(dot_product,2))


