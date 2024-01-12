class Person:
    def __init__(self,name,age): #parameterized constructor
        self.name = name
        self.age = age
    def display(self):
        print("my name is : ",self.name, "my age is : ",self.age)

p1 = Person("alby",24) #object creation
p1.display() #function calling using object


class Person:
    def __init__(self): #non-parameterized constructor
        print("hello!")
    def display(self,name,age):
        self.name = name
        self.age = age
        print("my name is : ",self.name, "my age is : ",self.age)

p1 = Person()
p1.display("alby",24)


#STUDENT DETAIL
class Student:
    def __init__(self,name,mobile,address):
        self.name = name
        self.mobile = mobile
        self.address = address
    def display(self):
        print("name : ",self.name)
        print("mob number : ",self.mobile)
        print("address : ",self.address)

p1 = Student("Alby Jacob Mathew",994738034,"kottayam")
p1.display()


#Employee detail
class Employee:
    def __init__(self,name,code,salary):
        self.name = name
        self.code = code
        self.salary = salary
    def display(self):
        print("Employee name : ",self.name)
        print("Job ID : ",self.code)
        print("Employee salary : ",self.salary)

p1 = Employee("Alby J M", "JK254" , 45000)
p1.display()
