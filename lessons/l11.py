"""
Make a calulator that takes in the user-inputted a and b as well as some operation (+, -, *, /) and outputs the result
If you finish, you can add a 'sqrt' function and a 'square' function

Hint:
You can use functions for each operation (eg. add, subtract, multiply, divide) 
and if statements to determine which operation the user selects
"""

a = input("n0: ")
b = input("n1: ")
def sum(x, y):
    return int(x)+int(y) 

print(sum(a, b))