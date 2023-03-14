import pandas as pd

i = ['row_1', 'row_2', 'row_3', 'row_4', 'row_5','row_6', 'row_7', 'row_8', 'row_9', 'row_10']


df = pd.DataFrame({'col_1': list(range(1, 11)), 
                   'col_2': list(range(11, 21)), 
                   'col_3': list(range(21, 31)),
                   'col_4': list(range(31, 41)), 
                   'col_5': list(range(41, 51)), 
                   'col_6': list(range(51, 61)),
                   'col_7': list(range(61, 71)), 
                   'col_8': list(range(71, 81)), 
                   'col_9': list(range(81, 91))}, index= i)

# Indexing Operator [ ] 

print(df["col_6"])
print("***********************************************")

# Multiple Column Selection with [ [ ] ]

print(df[['col_5', 'col_1', 'col_8']])
print("***********************************************")

# loc Indexer : Selects both rows and Columns Data or Only Rows Data 

print(df.loc['row_1'])
print("***********************************************")

# # Multiple Column Selection with loc Indexer [ [ ] ]

print(df.loc[['row_6', 'row_2', 'row_9']])
print("***********************************************")

print(df.loc['row_7':'row_9'])
print("***********************************************")

print(df.loc[:'row_4'])
print("***********************************************")

print(df.loc[['row_4', 'row_2'], ['col_5', 'col_2', 'col_9']])
print("***********************************************")

print(df.loc[['row_4', 'row_2'], 'col_5':'col_7'])
print("***********************************************")

print(df.loc['row_4':'row_6', 'col_5':])
print("***********************************************")

print(df.loc[:'row_4', 'col_5'])
print("***********************************************")

loc = df.loc['row_6', 'col_3']
print("Using loc Indexer to locate a value at Row_6 & Col_3 : " + str(loc))
print("***********************************************")


# # at Indexer is Powerful than loc Indexer to locate exact value 
# # of the particular Row and Column 

at = df.at['row_6', 'col_3']
print("Using at Indexer to locate a value at Row_6 & Col_3 : " + str(at))
print("***********************************************") 


# iloc Indexer : Selects single row or multiple rows data using index postion

print(df.iloc[3]) 
print("***********************************************") 


# # Multiple Rows Selection with iloc Indexer [ [ ] ]

print("Indexing Starts from 0(Zero)")
print(df.iloc[[7, 8 ,9]])
print("***********************************************") 


print(df.iloc[3:6])
print("***********************************************") 

print(df.iloc[[8, 1, 9], 5:9])
print("***********************************************") 


# # iat Indexer is Powerful than iloc Indexer to locate exact value 
# # of the particular Row and Column 

print(df.iat[1, 2])
print("***********************************************") 



# Selecting all the rows of the dataframe
# where the value of `col_2` is greater than 15 but not equal to 19

print(df[(df['col_2'] > 15) & (df['col_2'] != 19)])
print("***********************************************") 


# Selecting all the rows of the dataframe where the value of `col_2` is greater than 15
# or the value of `col_5` is equal to 42


print(df[(df['col_2'] > 15) | (df['col_5'] == 42)])
print("***********************************************") 









