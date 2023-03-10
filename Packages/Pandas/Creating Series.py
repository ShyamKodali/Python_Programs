import pandas as pd

# Creating a Series 

df = pd.Series([pd.Timestamp(2023, 3, 10),pd.date_range(start="2023-03-10", end="2023-03-15",periods=6),69,19364,"smack"])

print(df)

# Locating 

print(df[1])

# Multiple Locatings 

print(df[[2,4]])