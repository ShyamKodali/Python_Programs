import numpy as np
from scipy.interpolate import interp1d, UnivariateSpline, Rbf

# Interpolation : Generating Points between given points 

# 1D Interpolation : Interpolation distribution with 1 variable 
# 1D Interpoltaion for given xs and ys interpolate values from 2.1,2.2,2.3.....2.9

xs = np.arange(10)
ys = 2*xs + 1

interp_func_1 = interp1d(xs, ys)
newarr = interp_func_1(np.arange(2.1, 3, 0.1))

print('New xs should be in same range as of the old xs (we cant call interp_func() with values higher than 10, or less than 0)  : ' + str(newarr))


# Spline Interpolation : Points are fitted against PiecewiseFunction (A function that has different definition for different ranges) defined with polynomial
# Spline Interpoltaion for given xs and ys interpolate values from 2.1,2.2,2.3.....2.9

ysp = xs**2 + np.sin(xs) + 1

interp_func_2 = UnivariateSpline(xs, ysp)
newarr1 = interp_func_2(np.arange(2.1, 3, 0.1))

print('Spline Interpolation Array : ' + str(newarr1))


# Radial Basis Function : Defined corresponding to a fixed reference point
# Radial Basis Function  Interpoltaion for given xs and ys interpolate values from 2.1,2.2,2.3.....2.9

interp_func_3 = Rbf(xs, ysp)
newarr2 = interp_func_3(np.arange(2.1, 3, 0.1))

print('Radial Basis Function Interpolation Array : ' + str(newarr2))