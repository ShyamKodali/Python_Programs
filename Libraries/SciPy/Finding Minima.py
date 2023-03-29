# Minimize the function x^2 + x + 2 with BFGS: 
    
from scipy.optimize import minimize

def eqn(x):
  return x**2 + x + 2

mymin = minimize(eqn, 0, method='BFGS')

print('The minima of the equation x^2 + x + 2 with BFGS is: '+str(mymin.x))
print('******************************************************************')
print(mymin)