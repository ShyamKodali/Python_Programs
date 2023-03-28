import numpy as np 

x = [1,2,3,4,5]
y = [6,7,8,9,10]

# Adding two lists Using Iteartive method 
# zip() : To unzip two lists 

z1 = []
for i,j in zip(x,y):
    z1.append(i+j)
    
print('Sum of two lists using Iterative Method for postional sum is : ' + str(z1))

# Adding two lists using Numpy Ufuncs method
# add() : To add lists

z2 = np.add(x,y)

print('Sum of two lists using add builtin method for postional sum is : ' + str(z2))