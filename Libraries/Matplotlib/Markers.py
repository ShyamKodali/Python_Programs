import numpy as np 
import matplotlib.pyplot as plt

xpoints = np.array([0,23])
ypoints = np.array([0,44])

plt.plot(xpoints, ypoints, marker='*', ms=12,  mec = 'r', mfc='k')

# Default xpoints taken as 0,1,2,3,4..... till yn
plt.plot(ypoints, 'o-.k', marker='^', ms=15,  mec = 'c', mfc='m')

plt.show()