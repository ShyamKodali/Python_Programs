import matplotlib.pyplot as plt
import numpy as np

x = np.random.randint(20, size=(20))
y = np.random.randint(20, size=(20))
colors = np.random.randint(20, size=(20))
sizes = 10 * np.random.randint(20, size=(20))

plt.subplot(2,2,1)
plt.scatter(x, y, c=colors, s=sizes, alpha=0.5, cmap='ocean')
plt.colorbar()
plt.title('Ocean Colormap', loc='left')


plt.subplot(2,2,2)
plt.scatter(x, y, c=colors, s=sizes, alpha=0.5, cmap='summer')
plt.colorbar()
plt.title('Summer Colormap', loc='left')


plt.subplot(2,2,3)
plt.scatter(x, y, c=colors, s=sizes, alpha=0.5, cmap='rainbow')
plt.colorbar()
plt.title('Rainbow Colormap', loc='left')


plt.subplot(2,2,4)
plt.scatter(x, y, c=colors, s=sizes, alpha=0.5, cmap='twilight')
plt.colorbar()
plt.title('Twilight Colormap', loc='left')

plt.suptitle('COLOR MAPS along with its COLORBARS')
plt.show()