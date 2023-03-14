import pandas as pd

df = pd.read_csv("/Users/kodalisimac/GitHub/Python_Programs/Packages/Pandas/nba.csv")


# Applying Aggregation across all the columns 
# sum and min will be found for each 
# numeric type column in df dataframe
  
a = df.aggregate(['sum', 'min'])

# Aggregation for specific columns

b = df.aggregate({"Number":['sum', 'min'],
              "Age":['max', 'min'],
              "Weight":['min', 'sum'], 
              "Salary":['sum']})


print(a)
print("********************************************") 
print(b)