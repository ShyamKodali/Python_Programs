import pandas as pd

df_1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                    'B': ['B0', 'B1', 'B2', 'B3']})
  
df_2 = pd.DataFrame({'C': ['C0', 'C1', 'C2', 'C3'],
                      'D': ['D0', 'D1', 'D2', 'D3']})

join_1_on_2 = df_1.join(df_2)
join_2_on_1 = df_2.join(df_1)



print(join_1_on_2)
print("**********************") 
print(join_2_on_1)