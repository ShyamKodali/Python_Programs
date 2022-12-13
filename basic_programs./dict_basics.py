# Declaring a dictionary
# Key : Value pairs
# Mapping

a = {"One" : 1, "Two" : 2, "Three" : 3, "Four" : 4, "Five" : 5, "Six" : 6, "Seven" : 7, "Eight" : 8, "Nine" : 9, "Ten" : 10, "One" : 1, "Two" : 2, "Three" : 3, "Four" : 4, "Five" : 5, "Six" : 6, "Seven" : 7, "Eight" : 8, "Nine" : 9, "Ten" : 10}

# Printin Only Keys in dictionary 
print("Keys of the dictionary are as follows: ")
for i in a:
    print(i)
    

print(" ")
    
#Printing Only Values in dictionary
print("Values of the dictionary are as follows: ")
for i in a:
    print(a[i])

print(" ")

#Key-Value pairs 
print("Key-Value pairs of the dictionary are as follows: ") 
print(" ")
res = ""
for i in a:
    key = str(i)
    value = str(a[i])
    res = res + key + "-"
    res = res + value + " "
print(res)

print(" ")

#Unique Key-Value Pairs
print("Unique Key-Value pairs of the dictionary are as follows: ") 
print(" ")
uniq_res = ""
for i in a:
    key = str(i)
    value = str(a[i])
    if key not in uniq_res:
            uniq_res += key + "-"
    if value not in uniq_res:
            uniq_res += value + " "
print(uniq_res)