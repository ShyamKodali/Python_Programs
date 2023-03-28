import numpy as np

arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])

ver_concat = np.concatenate((arr1,arr2), axis=0)

hor_concat = np.concatenate((arr1,arr2), axis=1)
 

print(arr1)
print("**********") 
print(arr2)
print("**********") 
print(ver_concat)
print("**********") 
print(hor_concat)
print("**********") 


# Stack method to concatenate along new axis

s1 = np.stack((arr1, arr2), axis=0)
s2 = np.stack((arr1, arr2), axis=1)

print(s1)
print("**********") 
print(s2)
print("**********") 


# hstack --> Along Rows

a1 = np.array([1, 2, 3])
a2 = np.array([4, 5, 6])
h = np.hstack((a1, a2))

# vstack --> Along Cols

v = np.vstack((a1, a2))

# dstack --> Along Depth(Height)

d = np.dstack((a1, a2))


print('Horizontal Stack along Rows: ' + str(h))
print("**********") 
print('Vertical Stack along Columns: ' + str(v))
print("**********") 
print('Depth Stack along Height' + str(d))

