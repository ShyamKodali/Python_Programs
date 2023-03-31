import numpy as np 
import matplotlib.pyplot as plt

x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2, 2, 1)
plt.title('Sales', loc='left')
plt.plot(x,y)
plt.grid()

x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(2, 2, 2)
plt.title('Income', loc='left')
plt.plot(x,y)
plt.grid()

x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2, 2, 3)
plt.title('Expenditure', loc='left')
plt.plot(x,y)
plt.grid()

x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(2, 2, 4)
plt.title('Stock', loc='left')
plt.plot(x,y)
plt.grid()


plt.suptitle('MY SHOP')
plt.show()