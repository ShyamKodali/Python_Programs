class Person:
    
    def __init__(self,name):
        self.name = name
        
    def intro(self):
        print(f"Hi, This is {self.name}")
        
    def talk(self):
        print(self.name + " can talk")
        
    def walk(self):
        print(self.name + " can walk")
        
    def run(self):
        print(self.name + " can run")
        
    def stand(self):
        print(self.name + " can stand")
        
person1 = Person("Shyam")
person1.intro()
person1.talk()
person1.walk()
person1.run()
person1.stand()