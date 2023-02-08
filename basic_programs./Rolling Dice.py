import random

class Dice():
    
    def roll(self):
        a = random.randint(1, 6)
        b = random.randint(1, 6)
        result = (a,b)
        print(result)
        
dice1 = Dice()
dice1.roll()


