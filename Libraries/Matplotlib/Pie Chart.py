import matplotlib.pyplot as plt
import numpy as np

x = np.array([35, 25, 25, 15])
e = [0.2,0,0,0.1]
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
mycolors = ['red','green','blue','yellow']

plt.pie(x, labels = mylabels, colors = mycolors, shadow = True, startangle = 90, explode = e)
plt.legend(title = "Four Fruits:")
plt.show() 