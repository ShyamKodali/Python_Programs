import numpy as np

# =============================================================================
# Data Types in NumPy: 
#     i - integer
#     u - unsigned integer
#     f - float
#     c - complex float
#     S - string
#     U - unicode string
#     b - bool
#     m - timedelta
#     M - datetime
#     O - object
# =============================================================================

# To know what is the datatype of Array
arr = np.array([1.0,2.0,3.0,4.0])
print(arr.dtype)

# Converting datatype on Existing Array 
# by defining dtype as string 
arr = np.array([1.0,2.0,3.0,4.0], dtype='S')
print(arr.dtype)

# by defining dtype as string 
arr = np.array([1.0,2.0,3.0,4.0])
arr = arr.astype('i')
print(arr.dtype)

# =============================================================================
# Copy owns data, changes made to Copy doesnot affect original data : Copy method
# View does not owns data, changes made to View affet original data : View method
# =============================================================================

copy_arr = arr.copy()
view_arr = arr.view()

# changing first element of Array
arr[0] = 43

# To check if Array owns its data by "base" attribute
# If base attribute == None --> It owns a data

print(copy_arr.base)
print(view_arr.base)