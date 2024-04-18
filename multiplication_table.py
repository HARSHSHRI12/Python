"""n=int(input("Enter a number :"))
i=1
while i<=10:
    print(n*i)
    i+=1"""

# Q2> print the element following list using loop
#> [1,4,9,16,25,36,49,64,81,100]
"""num=[1,4,9,16,25,36,49,64,81,100]
i=0
while i<=len(num)-1: # i<10
    print(num[i])
    i+=1"""

    # example 2> print the following list using loop

"""list=["harsh","anshu","mummy","papa","dadi","dada"]
i=0
while i<=len(list)-1:
    print(list[i])
    i+=1"""

    # search for a number x in this tuple using loop 
    #(1,4,9,16,25,36,49,64,81.100)
num = (1, 4, 9, 10, 16, 25, 56, 49, 64, 81, 100)
x = 16
i = 0

while i < len(num):
    if num[i] == x:
        print("Found at index", i)
        break
    else:
        print("Finding...")
    i += 1


