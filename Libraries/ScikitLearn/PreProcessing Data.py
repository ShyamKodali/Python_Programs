# PreProcessing Data 

import numpy as np
from sklearn import preprocessing

data = np.array([[2.1,-1.9,5.5],[-1.5,2.4,3.5],[0.5,-7.9,5.6],[5.9,2.3,-5.8]])
mean = data.mean(axis=0)
stddev = data.std(axis=0)
print('Sample Data : ',data)
print('****************************************************************')
print('Mean of Sample Data : ',mean)
print('****************************************************************')
print('Standard Deviation of Sample Data : ',stddev)
print('****************************************************************')

# Binarisation : Convert Numerical to Boolean values 
#                Threshold value determines at value the original val to be converted  

binarizeddata = preprocessing.Binarizer(threshold=0.5).transform(data)

# Above Threshold value = 0.5, which means It converts above 0.5 == 1, below 0.5 == 0
print('Binarized Data : ',binarizeddata)
print('****************************************************************')

# Mean Removal : Eliminate MEAN from feature vector, so that every feature centered on "ZERO"

meanremovaldata = preprocessing.scale(data)

mrmean = meanremovaldata.mean(axis=0)
mrstddev = meanremovaldata.std(axis=0)
print('Mean of the data after Mean Removal : ',mrmean)
print('****************************************************************')
print('Standard Deviation of the data after Mean Removal : ',mrstddev)
print('****************************************************************')


# Scaling : For Scaling Feature Vector 

scaleddata = preprocessing.MinMaxScaler(feature_range=(0,1)).fit_transform(data)

# Above feature_range value = (0,1) which means 
print('Scaled Data with MinMax Scaler : ',scaleddata)
print('****************************************************************')