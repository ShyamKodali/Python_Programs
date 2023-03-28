import numpy as np

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

# Requires 'n' for loops to iterate each element and print 
for x in arr:
    for y in x:
        for z in y:
            print(z)

# nditer() --> Method use to reduce no of for loops
# Other Parameters like flags = ['buffered'] --> To Inplace the change of datatype in same array
#                       op_dtype=['S'] --> To change the datatype of Array while Iterating

for i in np.nditer(arr,flags=['buffered'], op_dtypes=['S']):
    print(i)
    

# Enumerate Method to print both Index and Element while Iterating 

arr1 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

for idx, x in np.ndenumerate(arr):
  print('Index and Element' + str(idx), str(x))