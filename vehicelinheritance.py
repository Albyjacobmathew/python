class Vehicle:
    def __init__(self,make,model):
        self.make = make
        self.model = model

    def start(self):
        print(self.model,"started")
    def stop(self):
        print(self.model,"stopped")

class car(Vehicle):
    def display(self,num_door):
        self.num_door = num_door
        print("Make : ",self.make,"Model : ",self.model,"number of doors : ",self.num_door)



class motorcycle(Vehicle):
    def display(self,two_wheels):
        self.two_wheels = two_wheels
        print("Make : ",self.make,"Model : ",self.model,"tyres :",self.two_wheels)



c = car("Hyundai","i20")
c.start()
c.display(4)
c.stop()

m = motorcycle("Bajaj","ns200")
m.start()
m.display("MRF")
m.stop()