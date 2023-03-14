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
 
         
# Inserting new column with values of list made above using for loop
data.insert(2, "Type New", Type_new)
 
# list output
print(data)
print("*************************************")

# Inserting new column with values of list 
data.insert(3, "Power", [340,420,323,378,392])

# list output
print(data)