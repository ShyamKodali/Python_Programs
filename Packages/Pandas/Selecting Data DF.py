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

# General Purpose 

# df.loc[df[‘column name’] condition]


# Selecting all the rows of the dataframe
# where the value of `col_2` is greater than 15 but not equal to 19

print(df[(df['col_2'] > 15) & (df['col_2'] != 19)])
print("***********************************************") 


# Selecting all the rows of the dataframe where the value of `col_2` is greater than 15
# or the value of `col_5` is equal to 42


print(df[(df['col_2'] > 15) | (df['col_5'] == 42)])
print("***********************************************") 