import numpy as np

# To know the shape of an Array
# To reshape the old array 

arr = np.array([[1,2,3,4],[5,6,7,8]])
print('2D arr is : ' + str(arr))
print('Shape of arr is : ' + str(arr.shape))


new_arr = arr.reshape(4,2)
print('new_arr is : ' + str(new_arr))
print('Shape of new_arr is : ' + str(new_arr.shape))

# 3D

arr1 = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
print('arr1 is : ' + str(arr1))
print('Shape of arr1 : ' + str(arr1.shape))

new_arr1 = arr1.reshape(2,3,2)
print('new_arr1 is : ' + str(new_arr1))
print('Shape of new_arr1 is : ' + str(new_arr1.shape))

# Flattening Array : Convertng MultiDimensional Arrays into 1D Array

flat_arr = arr.reshape(-1)
print('Shape of Original Array : ' + str(arr.shape))
print('Shape of Flattened Array : ' + str(flat_arr.shape))