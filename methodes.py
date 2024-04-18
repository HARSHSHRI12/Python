class student:
    college_name="ABC college"#class attribute one time memory occupy
    
    def __init__(self,name,marks):#constructer
        self.name=name#object attribute
        self.marks=marks
    def welcome(self):#method declearation
        print("Hello student Welcome to our college..",self.name,self.marks)
s1=student("harsh shrivastava",98)
print(s1.college_name)
s1.welcome()#Methodes calling
        