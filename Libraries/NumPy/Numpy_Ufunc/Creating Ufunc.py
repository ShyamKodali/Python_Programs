import numpy as np 

# =============================================================================
# To Create a own ufunc : 
#     1. We have to define a function same as normal function in python
#     2. Then Add the defined function to Numpy ufunc Library using 'frompyfunc()' method
# =============================================================================

# 1. Creating a Simple function[fn] to return addition of params

def fn(x,y):
    return x+y

# 2. Converting defined function[fn] to ufunc 

fn = np.frompyfunc(fn, 2, 1)  # 2 = no of parameters 1 = output i.e; in a single output
print(fn([1, 2, 3, 4], [5, 6, 7, 8]))


# Checking if function is ufunc or not 

print('The defined function[fn] ' + str(type(fn)) + ' is a ufunc')
print('The sum function is ' + str(type(np.sum)) + ' is not a unfunc')