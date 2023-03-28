import numpy as np

a = [1,2,3,4,5]
b = (10,20,30,40,50)
arr1 = np.array(a)
arr2 = np.array(b)
print("Array formed by List(a) : " + str(arr1))
print("Array formed by Tupple(b) : " + str(arr2))

# ndarray : Array Object in Numpy 

a1 = type(arr1)
print("Type of array formed by List :" + str(a1))
b1 = type(arr1)
print("Type of array formed by Tupple :" + str(b1))

# Dimensions in Array : Array Depth (Nested Array : Arrays that have Arrays as their elements)

# Zero Dimensional Array : 0D or Scalars are elements 
ZeroD = np.array(42)
print("This Array has : " + str(ZeroD.ndim))
print("Zero Dimensional Array: " + str(ZeroD))


# One Dimensional Array [UniDimensional Array] : Array that has 0D arrays as its elements
OneD = np.array([22,33,44,55,66])
print("This Array has : " + str(OneD.ndim))
print("One Dimensional Array: " + str(OneD))

# Two Dimensional Array [Matrix Array] : Array that has 1D arrays as its elements
# len of 1st list and 2nd list in TwoD are Equally given 
TwoD = np.array([[123,456,789,901,234],[567,890,123,456,789]])
print("This Array has : " + str(TwoD.ndim))
print("Two Dimensional Array: ")
print(TwoD)

# Three Dimensional Array [Matrix Array] : Array that has 1D arrays as its elements
ThreeD = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print("This Array has : " + str(ThreeD.ndim))
print("Three Dimensional Array: ")
print(ThreeD)

# Higher Dimensions can be defined 

c = np.array([6,7,8,9,0], ndmin=6) # Defined 6D Array
print("Six Dimensional Array (Defined ndmin=6): ")
print(c)

