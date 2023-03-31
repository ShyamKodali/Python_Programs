import matplotlib.pyplot as plt
import numpy as np

# Drawing a Line between two points 
# Defining two points as : x1 = 0, y1=0, x2 = 0, y2 = 250
xpoints = np.array([0,6])
ypoints = np.array([0,250])

# Plotting x & y points to Draw a Line  
plt.plot(xpoints, ypoints)

# Plotting x & y points to Plot ONLY the points 
plt.plot(xpoints, ypoints, 'o')


# Displaying Line and Points on the screen 
plt.show()