# WAP to entered marks of 3 subject from the use and store them in a dictionary . start with an empaty dictionary & add one b y one . use subject name as key & marks as value

marks={}
x=int(input("Enter english marks :"))
marks.update({"english":x})

x=int(input("Enter maths marks :"))
marks.update({"Maths":x})

x=int(input("Enter physics marks :"))
marks.update({"physics":x})
    
print(marks)
