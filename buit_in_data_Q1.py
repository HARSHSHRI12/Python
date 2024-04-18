# figure out a way to store 9 & 9.0 as seprate values in the set
#Hint:- you can take help of built-in data type

"""value=(9,"9.0")
print(value)"""

# with built-in data (tuple)
value={
    ("float",9.0),
    ("int",9)
}
print(value)