class Calculation1:
    def Summation(self,a,b):
        return a+b;
class Claculation2:
    def Multipication(self,a,b):
        return a*b;
class Derived(Calculation1,Claculation2):
    def Divide(self,a,b):
        return a/b;
d = Derived()
print(isinstance(d,Derived))