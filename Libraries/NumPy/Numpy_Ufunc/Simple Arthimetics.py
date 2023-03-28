import numpy as np 

arr1 = [1,2,3,4]
arr2 = [7,8,9,10]

add = np.add(arr1,arr2)
sub = np.subtract(arr1,arr2)
mul = np.multiply(arr1,arr2)
div = np.divide(arr1,arr2)
power = np.power(arr1,arr2)
remainder = np.remainder(arr1,arr2)
quo = np.divmod(arr1,arr2)
absolute = np.absolute([-1,-22,43,-87])

print(add)
print(sub)
print(mul)
print(div)
print(power)
print(remainder)
print(quo)
print(absolute)