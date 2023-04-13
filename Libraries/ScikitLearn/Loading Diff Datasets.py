# Differenet available Datasets Loading

from sklearn import datasets 

# MODELLING PROCESS

# Loading different Data into different varaible 

iris_data = datasets.load_iris()
digits_data = datasets.load_digits()
houseprice_data = datasets.load_boston()
diabetes_data = datasets.load_diabetes()
breastcancer_data = datasets.load_breast_cancer()

# Defining varaibles to the feature_names and target_names 

f_names_iris = iris_data.feature_names
t_names_iris = iris_data.target_names
f_names_digits = digits_data.feature_names
t_names_digits = digits_data.target_names
f_names_houseprice = houseprice_data.feature_names
f_names_diabetes = diabetes_data.feature_names
f_names_breastcancer = breastcancer_data.feature_names
t_name_breastcancer = breastcancer_data.target_names


print("Feature names of Iris Data : ", f_names_iris)
print("Target names of Iris Data :", t_names_iris)
print('******************************************************')
print("Feature names of Digits Data : ", f_names_digits)
print("Target names of Digits Data : ", t_names_digits)
print('******************************************************')
print("Feature names of Boston House Price Data : ", f_names_houseprice)
print('******************************************************')
print("Feature names Diabetes Data : ", f_names_diabetes)
print('******************************************************')
print("Feature names Breast Cancer Data : ", f_names_breastcancer)
print("Target names Breast Cancer Data :", t_name_breastcancer)
print('******************************************************')


# Defining varaibles to the data and output 

X1 = iris_data.data
y1 = iris_data.target
X2 = digits_data.data
y2 = digits_data.target
X3 = houseprice_data.data
y3 = houseprice_data.target
X4 = diabetes_data.data
y4 = diabetes_data.target
X5 = breastcancer_data.data
y5 = breastcancer_data.target



print("Iris Data: ", X1)
print("Iris Target: ", y1)
print(X1[:10])
print('******************************************************')
print("Digits Data: ", X1)
print("Digits Target: ", y1)
print(X2[:10])
print('******************************************************')
print("Boston House Price Data: ", X1)
print("Boston House Price Target: ", y1)
print(X3[:10])
print('******************************************************')
print("Diabetes Data: ", X1)
print("Diabetes Target: ", y1)
print(X4[:10])
print('******************************************************')
print("Breast Cancer Data: ", X1)
print("Breast Cancer Target: ", y1)
print(X5[:10])
print('******************************************************')















