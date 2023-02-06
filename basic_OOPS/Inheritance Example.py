#Base Class or Parent Class

class HumanBeing:
    
    def __init__(self,f,l):
        self.fname = f
        self.lname = l
        
    def talk(self):
        print(f"{self.fname} {self.lname} can talk fluently")
        
    def walk(self):
        print(f"{self.fname} {self.lname} can walk rigurously")
        
# Created 2 Child Classes : Female, Male, Trans

# Inherited all properties from Parent Class and adding new properties 

class Female(HumanBeing):
    
    # Not to Override the Parent Class __init__() 
    
    def __init__(self,f,l):
        HumanBeing.__init__(self, f, l)
        
    def ChildBirth(self,b,g):
        self.babyboy = b
        self.babygirl = g
        print(f'{self.fname} {self.lname} can give birth to {b} or {g} or both at a time')
        
# Inherited all properties from Parent Class without any addition of new properties 
        
class Male(HumanBeing):
    pass

# Inherited all properties from Parent Class and adding new properties

# Overrides Parent Class __init__() 

class Trans(HumanBeing):
    
    def __init__(self,name):
        self.name = name
        
    def sexualorientation(self):
        print(f"{self.name} having a bi gender sexual orientation")


# Object for Parent Class 

Hum1 = HumanBeing("Shyam","Singha Roy")

# Calling the method using Object created above 

Hum1.walk()

# Object for 1st Child Class 

Fem1 = Female("Samantha", "Ruth Prabhu")

# Calling the method using Object created above 

Fem1.talk()
Fem1.ChildBirth("baby_boy", "baby_girl")

# Object for 2nd Child Class 

Mal1 = HumanBeing("Ram", "Charan")

# Calling the method using Object created above 

Mal1.walk()

# Object for 3rd Child Class 

Trans1 = Trans("Jo")

# Calling the method using Object created above 

Trans1.sexualorientation()