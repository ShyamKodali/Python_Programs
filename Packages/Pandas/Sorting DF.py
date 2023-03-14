import pandas as pd

data = {'Brand': ['Hush_Puppies','Nike','Addidas','Puma'],
        'Price': [22000,25000,27000,35000],
        'Year': [2015,2013,2018,2018]
        }
 
df = pd.DataFrame(data)

# Sorting by Brand in Ascending Order (Default)

Ascending_Order = df.sort_values(by=['Brand'])

# Sorting by Brand in Descending Order (Default)

Descending_Order = df.sort_values(by=['Brand'], ascending=False)

# Sorting by Year & Price in Ascending Order (Default)

MulCols_Asc_Ord = df.sort_values(by=['Year','Price'])


print(df)
print("*************************************")
print(Ascending_Order)
print("*************************************")
print(Descending_Order)
print("*************************************")
print(MulCols_Asc_Ord)
print("*************************************")

