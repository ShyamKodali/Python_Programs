class Employee:
 
    # Initializing Constructor
    def __init__(self):
        print('Employee created')
 
    # Calling Destructor
    def __del__(self):
        print("Destructor called")

# Created a new function
def Create_obj():
    print('Making Object...')
    obj = Employee()
    print('function end...')
    return obj
 
print('Calling Create_obj() function...')
obj = Create_obj()
print('Program End...')