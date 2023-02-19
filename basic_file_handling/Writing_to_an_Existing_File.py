# To write to an existing file 

test = open("demo1.txt",'a')
test.write("Update the content of this file if this program excutes!!")
test.close()
test.open("demo1.txt",'rt')
print(test.read())