import pandas as pd

df_1 = pd.DataFrame({'Key': ['K0', 'K1', 'K2', 'K3'],
                    'A': ['A0', 'A1', 'A2', 'A3'],
                    'B': ['B0', 'B1', 'B2', 'B3']})
  
df_2 = pd.DataFrame({'Key': ['K0', 'K1', 'K2', 'K3'],
                      'C': ['C0', 'C1', 'C2', 'C3'],
                      'D': ['D0', 'D1', 'D2', 'D3']})



inner_merge = pd.merge(df_1, df_2, how ='inner', on ='Key')
outer_merge = pd.merge(df_1, df_2, how ='outer', on ='Key')



print(inner_merge)
print("**********************") 
print(outer_merge)
print("*******************************") 
equality = (inner_merge == outer_merge)
print(equality)