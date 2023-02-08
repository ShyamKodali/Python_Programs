secret_number = 624

welcome_text = 'Welcome to the Guess Game!'
print(welcome_text.center(90))

instructions = 'Enter a number from [1 to 9] in 3 chances to win the game!'
print(instructions.center(90))

guess_limit = 3
guess_count = 0

while guess_count < guess_limit:
    guess_count += 1
    guess = int(input("Enter a guess number: "))
    if guess == secret_number:
        print("You Won!")
        break
else:
    print("You Failed!")
