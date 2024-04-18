# del keyword...

class student:
   def __init__(self,name,age,stream):
      self.name=name 
      self.age=age
      self.stream=stream
s1=student("harsh",19,"BCA")
print(s1.name)
print(s1.age)
print(s1.stream)
del s1.name
print(s1.name)
print(s1.age)
print(s1.stream)
