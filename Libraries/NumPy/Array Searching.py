import numpy as np

arr = np.array([1, 2, 3, 4, 5, 4, 4])
x = np.where(arr == 4)
y = np.where(arr%2 == 0)

# Binary Search --> searchsorted() : Searched Left to Right
arr1 = np.array([6, 7, 8, 9])
z = np.searchsorted(arr1, 7)
# To Search from Right to Left : parameter - side with argument 'right' should be passed 
z1 = np.searchsorted(arr1, [7,8], side='right')

print(x)
print('**********************')
print(y)
print('**********************')
print(z)
print('**********************')
print(z1)