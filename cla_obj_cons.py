"""class student:#class creating AND if you have not create a constructer by defoult python is create there
     name= "harsh shrivastava"
     sec="A"
s1 = student()#object creating
print(s1.name)
print(s1.sec)"""

#with constructer create class and object...

class player:
 #by defoult construters...
 def __init__(self):
   pass
 #parameterize constructers....
 def __init__(self,name,color,name2,no):
   self.team=name
   self.jcolor=color
   self.country=name2
   self.jno=no
   print("crete a team and duarate the companey......")

p1=player("hydrabad","red","india",18)
print(p1.team)
print(p1.jcolor)
print(p1.country)
print(p1.jno)
p2=player("prayagraj","blue","amarica",20)
print(p2.team)
print(p2.jcolor)
print(p2.country)
print(p2.jno)


    

 