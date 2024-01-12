from abc import ABC,abstractmethod
#define abstract class

class Shape(ABC):
    def area(self):
        print("area of the shape")

    def perimeter(self):
        print("perimeter of the shape")

class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return 3.14*self.radius*self.radius
    
    def perimeter(self):
        return 2*3.14*self.radius
    
class Square(Shape):
    def __init__(self,side_lenght):
        self.side_lenght=side_lenght
    def area(self):
        return self.side_lenght*self.side_lenght
    
    def perimeter(self):
        return 4*self.side_lenght
    
c=Circle(int(input("enter radius: ")))
s=Square(int(input("enter side length: ")))

print("circle area",c.area())
print("circle perimeter",c.perimeter())

print("square area",s.area())
print("square perimeter",s.perimeter())