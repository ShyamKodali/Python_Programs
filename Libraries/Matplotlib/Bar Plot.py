import numpy as np
import matplotlib.pyplot as plt

x = np.random.randint(20, size=20)
y = np.random.randint(20, size=20)

plt.subplot(1, 2, 1)
plt.bar(x, y, color= 'red' , width=1)
plt.title('Bar Plot', loc='left')
plt.grid()



plt.subplot(1, 2, 2)
plt.barh(y, x, color= 'yellow' , height=1)
plt.title('Barh(Horizontal) Plot', loc='left')
plt.grid()


plt.suptitle('BAR PLOTTING')
plt.show()