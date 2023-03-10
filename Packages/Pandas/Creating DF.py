import pandas as pd

# Creating a DataFrame 

df = pd.DataFrame({'A' : 1, 'B' : pd.Timestamp(2023, 3, 10), 'C' : pd.date_range(start='2023-03-10', periods=5), 'D' : pd.Categorical(["ash","cash","smash","flash","trash"]), 'E' : "foo"})

print(df)

# Locating 

print(df.loc[3])

# Multiple Locatings 

print(df.loc[[2,4]])

# If Indexed 

i = ['X','Y','Z','P','Q']

df = pd.DataFrame({'A' : 1, 'B' : pd.Timestamp(2023, 3, 10), 'C' : pd.date_range(start='2023-03-10', periods=5), 'D' : pd.Categorical(["ash","cash","smash","flash","trash"]), 'E' : "foo"}, index = i)

print(df.loc['X'])
print(df.loc[['Y','Q']])

