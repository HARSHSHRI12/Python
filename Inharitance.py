class Car:
    color="black"
    @staticmethod
    def start():
        print("Car Started......")
    @staticmethod
    def stop():
        print("Car Stoped.....")
class HyndaiCar(Car):#inharite parents class method and attribute
    def __init__(self,name):#constructer 
        self.name=name
car1=HyndaiCar("verna")
car2=HyndaiCar("hyndaCityZ")
print(car1.start())
print(car1.color)    
print(car2.stop())                
print(car2.color)