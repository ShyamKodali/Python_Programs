import matplotlib.pyplot as plt
import numpy as np

x = np.random.normal(170, 10, 250)
font1 = {'family':'serif', 'color':'red', 'size':12}
font2 = {'family':'serif', 'color':'purple', 'size':20}


plt.xlabel('xlabel', fontdict=font1)
plt.ylabel('ylabel', fontdict=font1)
plt.title('HISTOGRAM', fontdict=font2)
plt.hist(x)
plt.show() 