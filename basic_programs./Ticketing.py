total = ""
ticket_price = 0
count = 1

while count<= 5:
    age = int(input('>> '))
    count += 1
    if age <= 3:
        print("Under Age less than 3 is Free of cost!")
        continue
    print(age)
    
    ticket_price += 100
    
total = ticket_price
print(total)
