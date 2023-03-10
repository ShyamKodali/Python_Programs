import pandas as pd
import numpy as np

dates = pd.date_range(start = "2023-03-10", periods=6)
cols = ['A1','A2','A3','A4','A5','A6']

df = pd.DataFrame(np.random.randn(6,6), index = dates, columns=cols)

# Viewing Data 

print(df)
print("**********************************************************************")
print("Columns of the DataFrame are below: ")
print(df.columns)
print("Index of the DataFrame are below: ")
print(df.index)
print("**********************************************************************")
print("First 2 Rows of data are below: ")
print(df.head(2))
print("**********************************************************************")
print("Last 2 Rows of data are below: ")
print(df.tail(2))
print("****************************   END   *********************************")