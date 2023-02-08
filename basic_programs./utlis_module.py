def input_list():
    while True:
        try:
            global l
            l = input(">> ")
            l = l.split()
            for i in range(len(l)):
                l[i] = int(l[i])
            break 

        except ValueError:
            print("Please enter a list of numbers seperated by space for each number!!")
            continue 
        
def display_list():
    print("Entered list of numbers are : ",l)
    
def find_max():
    maxi = l[0]
    for i in l:
        if i>maxi:
            maxi = i
    print("Maximum number in the entered list is: ",maxi)
