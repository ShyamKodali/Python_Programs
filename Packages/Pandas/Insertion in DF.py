import pandas as pd
 
Type_new = pd.Series([])
data = pd.read_csv("pokemon.csv")
 
 
# running a for loop and assigning some values to series
for i in range(len(data)):
    if data["Type"][i] == "Grass":
        Type_new[i]="Green"
 
    elif data["Type"][i] == "Fire":
        Type_new[i]="Orange"
 
    elif data["Type"][i] == "Water":
        Type_new[i]="Blue"
 
    else:
        Type_new[i]= data["Type"][i]
 
         
# inserting new column with values of list made above       
data.insert(2, "Type New", Type_new)
 
# list output
print(data.head())