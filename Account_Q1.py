
class Account:
 def __init__(self,bal,acc):
     self.balance=bal
     self.account_number=acc

        #Debit methode
 def debit(self,amount):
     self.balance -= amount
     print("Rs.",amount,"was debited")
     print("Total balance is = ",self.get_balance())
        #cradit method
 def credit(self,amount):
     self.balance += amount
     print("Rs.",amount,"was credit")
     print("Total balance is = ",self.get_balance())
        #Printing methode
 def get_balance(self):
     return self.balance  

 print("Welcom to State Bank of India ")
print("-------------------------------------\n \n")
pin=int(input("Enter your pin to unlock service :"))
if pin==7706:
    print("what to do:-MENU")
    print("-------------------\n")
    print("1-> For Debit press 1 ")
    print("2-> For Credit press 6 ")
    print("3-> For Check curent balance press 0 \n")
    num=int(input("Enter a number what do you want : "))
acc1=Account(12000,4235647)
if num==1:
    amount=int(input("enter a Amount to be debited :"))
    acc1.debit(amount)
elif num==6:
    c=int(input("enter a Amount to be Credited :"))
    acc1.credit(c)
elif num==0:
    print("current balance is =",acc1.get_balance())


   