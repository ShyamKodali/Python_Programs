from sklearn import datasets


# MODELLING PROCESS

# Loading Iris Data into iris_data varaible 
iris_data = datasets.load_iris()
digits_data = datasets.load_digits()
houseprice_data = datasets.load_boston()
diabetes_data = datasets.load_diabetes()
breastcancer_data = datasets.load_breast_cancer()

# Defining varaibles to the feature_names and target_names 
feature_names = iris_data.feature_names
target_names = iris_data.target_names
print("Feature names:", feature_names)
print("Target names:", target_names)

# Defining varaibles to the data and output 
X = iris_data.data
y = iris_data.target
print("Iris Data: ", X)
print("Iris Target: ", y)

print(X[:10])