#1.Create a base class Person with attributes name and age. Then, create a subclass Employee that inherits from Person and has an additional attribute employee_id
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Employee(Person):
    def function(self,empid):
        self.empid=empid
        print("name of the person:",self.name,"\n","age of the person:",self.age,"\n","employee id:",self.empid)
p=Employee("rajesh",36)

p.function("E202076")


#2.Create a base class Shape with a method area and then create two subclasses Circle and Rectangle that inherit from Shape and implement their own versions of the area method.

class Shape:
    def area(self):
        pass
class Circle(Shape):
    def area(self,radius):
        self.radius=radius
        print("radius=",3.14*self.radius**2)
class Rectangle(Shape):
    def area(self,length,height):
        self.length=length
        self.height=height
        print("area of rectangle=",self.length*self.height)
a=Circle()
a.area(5)
b=Rectangle()
b.area(4,5)

#3.

class Vehicle:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
class Car(Vehicle):
    def function(self):
        print("the barnd is",self.brand,"\n","model is:",self.model)
class Motorcycle(Vehicle):
    def function(self):
        print("the barnd is",self.brand,"\n","model is:",self.model)
p=Car("lamborgini","urus")
p.function()
d=Motorcycle("triumph","bobber")
d.function()