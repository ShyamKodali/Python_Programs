# Use open() function with one of the parameters : a, w, x

# a - append to end of the file and it will create file if specified file dont exit

test = open("demo1.txt",'a')
print(test)

# w - write will create file if specified file dont exit
# w - It will over writes entire file 

test1 = open("demo2.txt",'w')
print(test1)

    # writable method to check if file stream can be write or not
print(test1.writable())

    # write method to write specific string to a file
print(test1.write("Model - The data you want to present, usually data from a database."))

    # writelines method writes a specific strings to a file
print(test1.writelines("View - A request handler that returns the relevant template and content - based on the request from the user."))

# x - creates a new file, Error : if file exit

test2 = open("demo1.txt",'x')
print(test2)