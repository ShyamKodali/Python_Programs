class CSStudent:
    stream = 'cse'                  # Class Variable
    def __init__(self,name,roll):
        self.name = name            # Instance Variable
        self.roll = roll            # Instance Variable
 

a = CSStudent('Samantha', 623)
b = CSStudent('Kajal', 624)
 
print(a.stream)  
print(b.stream)  
print(a.name)   
print(b.name)    
print(a.roll)    
print(b.roll)  
 
# Class variables can be accessed using class
# name also
print(CSStudent.stream) 
 
# Now if we change the stream for just a it won't be changed for b
a.stream = 'ece'
print(a.stream) 
print(b.stream) 
 
# To change the stream for all instances of the class we can change it
# directly from the class
CSStudent.stream = 'mech'
 
print(a.stream) 
print(b.stream) 