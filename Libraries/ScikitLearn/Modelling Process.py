from sklearn import datasets


# MODELLING PROCESS

# Loading Iris Data into iris_data varaible 
iris_data = datasets.load_iris()


# Defining varaibles to the feature_names and target_names 
f_names_iris = iris_data.feature_names
t_names_iris = iris_data.target_names


print("Feature names of Iris Data : ", f_names_iris)
print("Target names of Iris Data :", t_names_iris)

# Defining varaibles to the data and output 
X = iris_data.data
y = iris_data.target
print("Iris Data: ", X)
print("Iris Target: ", y)

print(X[:10])