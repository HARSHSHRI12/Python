# Wap to check if a list contain a palindrome of element 
# Hint:- use copy method 

list= [1,2,3,2,1]
list_copy=list.copy()
list_copy.reverse()
if(list_copy==list):
    print("THe element is palindrome ....")
else:
    print("The element is not palindrome .......")

