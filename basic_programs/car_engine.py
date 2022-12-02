welcome_note = "Welcome to the Car Game!!"
print(welcome_note.center(90))


start = "Car Started! Accelerate to GO!!"
started = False
already_started = "Car already started... Accelerate to move the car!!"
stop = "Car Stopped! Start agin!!"
already_stopped = "Car already stopped... Please start the car!!"
quit = "Good Bye! See you next time"
help = '''
start = To start the car.
stop = To stop the car.
accelerate = To move the car.
quit = To exit from the game.
'''


user_input = "" 

while  True:
    
    user_input = input(">> ").lower()
    
    if user_input == "start":
        if started:
            print(already_started)
        else:
            started = True
            print(start)
            
    elif user_input == "stop":
        if not started:
            print(already_stopped)
        else:
            strated = False
            print(stop)
            
    elif user_input == "help":
        print(help)
        
    elif user_input == "quit":
        print(quit)
        break 
else: 
    print ("Sorry! I dont understand that please type 'help' to get options")
    


