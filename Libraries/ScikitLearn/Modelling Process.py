from sklearn import datasets


# MODELLING PROCESS

# Loading Iris Data into iris_data varaible 
iris_data = datasets.load_iris()


# Defining varaibles to the feature_names and target_names 
f_names_iris = iris_data.feature_names
t_names_iris = iris_data.target_names


print("Feature names of Iris Data : ", f_names_iris)
print('*************************************************')
print("Target names of Iris Data :", t_names_iris)
print('*************************************************')

# Defining varaibles to the data and output 
X = iris_data.data
y = iris_data.target
print("Iris Data: ", X)
print('*************************************************')
print("Iris Target: ", y)

print(X[:10])

from sklearn.model_selection import train_test_split

# Splitting Data as Training and Testing Datasets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 1)

print('*************************************************')
print('Training Dataset shape of whole Data : ' + str(X_train.shape))
print('Testing Dataset shape of whole Data : ' + str(X_test.shape))
print('*************************************************')
print('Training Dataset shape of Target Data : ' + str(y_train.shape))
print('Testing Dataset shape of Target Data : ' + str(y_test.shape))
print('*************************************************')

# Training the Model

# Ex: KNN (used)

from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics

# Creating Model with required arguments
knn = KNeighborsClassifier(n_neighbors = 3)

# Fitting created model to Train data sets (data(X_train) and Target(y_train))
knn.fit(X_train, y_train)


# Predicting with Test datasets 
y_pred = knn.predict(X_test)

# Finding accuracy by comparing actual response values(y_test)with predicted response value(y_pred)
print("Accuracy: ", metrics.accuracy_score(y_test, y_pred))
print('*************************************************')


# Providing sample data and the model will make prediction out of that data
sample = [[5, 5, 3, 2], [2, 4, 3, 5]]
preds = knn.predict(sample)
pred_species = [t_names_iris[p] for p in preds]

print("Predictions:", pred_species)
print('*************************************************')


# Model Persistence
import joblib

# Saves Iris Data KNN model as iris_knn.joblib
joblib.dump(knn, 'iris_knn.joblib')

# Reloads Iris Data KNN model 
joblib.load('iris_knn.joblib')