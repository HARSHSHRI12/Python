# 1st method are
"""class student:
    
    def __init__(self,name,m1,m2,m3):
       self.name=name
       self.m1=m1
       self.m2=m2
       self.m3=m3

    def average(self):
        avg= (self.m1 + self.m2 + self.m3) / 3
        print("The name is :", self.name, "the average of three numbers are :", avg)

s1 = student("harsh", 99, 98, 89)
print(s1.name)
s1.average()"""

#2nd methode----

class student:
    
    def __init__(self,name,marks):
       self.name=name
       self.marks=marks

    def average(self):
       sum=0
       for val in self.marks:
           sum+=val
       print("The name is :", self.name, "your average  numbers are :", sum/3)

s1 = student("harsh", [99, 98, 89])
s1.average()



