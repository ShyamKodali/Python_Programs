import numpy as np
import matplotlib.pyplot as plt

y1 = np.array([3, 8, 1, 10])
y2 = np.array([6, 2, 7, 11])

# Default x1,x2,x3,x4...... as 0,1,2,3,4.....
plt.plot(y1, ls='--',color='hotpink',linewidth=10)
plt.plot(y2, ls=':',color='cyan',linewidth=15)

plt.show()