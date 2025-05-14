"""Make a program that solves a diophantine equation ax+by=c for one integer solution. 
Test the numbers -1000 to 1000 for both x and y.
Note that there may not be a solution."""

"""
Fizzbuzz
 
For every number from 1 to 100 inclusive,
- if that number is divisble by 2, print "fizz"
- if that number is divisble by 3, print "buzz"
- if that number is divisble by both 2 and 3, print "fizzbuzz"
"""

"""Mini Project: Trivia Game (remainder of class) 
    1.  Create at least 3 trivia questions, and prompt the user. 
    2.  Count how many the user gets right, and if they get a score above 70%, they win! 
    3.  If the user fails, they have to redo the trivia quiz until they win. 
    4.  Make sure to randomize the order the questions go in."""

"""
# nested for loop
for i in range(1, 11):
    for j in range(1, 11):
        print(i*j)
        """

# find a solutions to 2x+y=300
for y in range(1, 101):
    for x in range(1, 101):
        if 2*x+y==300:
            print(x, y)