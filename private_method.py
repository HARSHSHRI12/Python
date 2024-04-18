class Account:
    def __init__(self,acc_no,acc_pass):
        self.acc_no=acc_no
        self.__acc_pass=acc_pass # if you have to private your acc_pass then use __
    def reset_pass(self):
       print(self.__acc_pass)
acc1=Account("1236435088","harsh12")
print(acc1.acc_no)
print(acc1.reset_pass())