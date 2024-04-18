class Car:
    def __init__(self,type):
        self.type=type
    @staticmethod
    def start():
        print("Car started .....")
    @staticmethod
    def stop():
        print("Car stoped ....")
class Hyndai_Car(Car):
    def __init__(self,name,type):
         super().__init__(type)
         self.name=name
         super().start()
car1=Hyndai_Car("verna","Electric")
print(car1.name)
print(car1.type)    
       