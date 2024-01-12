class Animal:
    def __init__(self,name):
       self.name=name

    def speak(self):
        print("welcome to inheritance")

class Dog(Animal):
    def speak(self):
        print("says bowwboww",self.name)

class Cat(Animal):
    def speak(self):
        print("says meowmeow",self.name)

d=Dog("puppy")
d.speak()

c=Cat("pussy")
c.speak()