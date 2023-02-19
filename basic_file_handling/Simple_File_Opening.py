# Opening File with open() function 

# r - read(default), a - append, w - write, x - create
# t - text(default), b - binary

text = open("demo.txt","rt")

# read method with 
print(text.read(2))
print(text.read(3))

# readline method to print lines of a document 

print(text.readline())

# readable method to check if file stream can be read or not

print(text.readable())

# writable method to check if file stream can be write or not

print(text.writable())

# write method to write specific string to a file
# print(text.write("234"))
# writelines method writes a specific strings to a file
# print(text.writelines())

# tell method returns current file postion 

print(text.tell())

# seekable method returns whether file allows us to change file postion 

print(text.seekable())

# seek method change the file postion; args : offset, whence

print(text.seek(43,0))

# truncate method resizes file to a specific size
# print(text.truncate())

# Closing File with close() function 

text.close()  