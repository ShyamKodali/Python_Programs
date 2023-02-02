# Creating a Class 

class Employees:
    # To explain ATTRIBUTES defined in a class
    employee_name = " "
    employee_age = 0
    employee_id = " "
    
# Creating Objects from the defined class (Employees)

Employee_1 = Employees()
Employee_2 = Employees()
Employee_3 = Employees()

# Accessing ATTRIBUTES & Assigning values to the Attributes using "." notion

Employee_1.employee_name = "Shyam"
Employee_1.employee_age = 26
Employee_1.employee_id = "1234A"
Employee_2.employee_name = "Kumar"
Employee_2.employee_age = 27
Employee_2.employee_id = "1234B"
Employee_3.employee_name = "Kodali"
Employee_3.employee_age = 28
Employee_3.employee_id = "1234C"

print(f"""Employee_1 deatils are as follows: 
          Name : {Employee_1.employee_name}
          Age : {Employee_1.employee_age}
          Employee ID: {Employee_1.employee_id}""")
          
print(f"""Employee_2 deatils are as follows: 
          Name : {Employee_2.employee_name}
          Age : {Employee_2.employee_age}
          Employee ID: {Employee_2.employee_id}""")
          
print(f"""Employee_3 deatils are as follows: 
          Name : {Employee_3.employee_name}
          Age : {Employee_3.employee_age}
          Employee ID: {Employee_3.employee_id}""")
