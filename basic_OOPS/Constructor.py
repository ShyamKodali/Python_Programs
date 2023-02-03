# Constructors are 2 types : 1) Default Constructor 2) Parameterized Constructor

# 1) Default Constructor

class Point:
 
    # Default Constructor is used below
    def __init__(self):
        self.d = "Data that can be accessed"

    # Method for printing data members
    def print_data(self):
        print(self.d)
    
# Creating object of the class
Point1 = Point()
 
# Calling the instance method using the object Point1
Point1.print_data()


# 2) Parameterized Constructor 

class Addition:
    first = 0
    second = 0
    answer = 0
 
    # Parameterized Constructor is used below
    def __init__(self,f,s):
        self.first = f
        self.second = s
 
    def display(self):
        print("First number = " + str(self.first))
        print("Second number = " + str(self.second))
        print("Addition of two numbers = " + str(self.answer))
 
    def calculate(self):
        self.answer = self.first + self.second
 
 
# Creating object of the class along with the arguments 
# This will invoke parameterized constructor

Add1 = Addition(1000, 2000)
 
# Creating second object of same class along with the different arguments 
Add2 = Addition(10, 20)
 
# Performing Addition on Object: Add1
Add1.calculate()
 
# Performing Addition on Object: Add2
Add2.calculate()
 
# Displaying result of Object: Add1
Add1.display()
 
# display result of Object: Add2
Add2.display()