class Car:
    @staticmethod
    def start():
        print("car started....")
    @staticmethod
    def stop():
        print("car stoped.....")
class hyndai_car(Car):
    def __init__(self,brand):
        self.brand=brand
class verna(hyndai_car):    
       def __init__(self,type):
            self.type=type
car1=verna("petrol") 
car1=verna("Disel") 
car1.start()                           