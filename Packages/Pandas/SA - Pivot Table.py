import pandas as pd


df = pd.DataFrame({'A': ['John', 'Boby', 'Mina', 'Peter', 'Nicky'],
      'B': ['Masters', 'Graduate', 'Graduate', 'Masters', 'Graduate'],
      'C': [27, 23, 21, 23, 24]})

# Simplest pivot table must have a dataframe
# and an index/list of index.

tab = pd.pivot_table(df, index =['A', 'B'])

# Creates a pivot table dataframe

table = pd.pivot_table(df, values ='A', index =['B', 'C'],
                         columns =['B'], aggfunc = "sum")


print(df)
print("*****************************")
print(tab)
print("*****************************")
print(table)