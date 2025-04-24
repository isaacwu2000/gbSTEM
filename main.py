"""
Functions Review:
- Code that does stuff
- Simpler and reusable
'
def square(x):
    return x*x
'

Getting character indicies
# Get the first n letters
s = "hello world!"
print(s[:n])

# Get the characters from index n forward
s = "hello world!"
print(s[n:])

# Get the characters between index a and b (includes a, but not b)
s = "hello world!"
print(s[a:b])

# Get the last n characters
s = "hello world!"
l = len(s)
n=3
print(s[l-n:])
"""

"""
Project:
Create a function that takes in a string and int n. 
The function should create a string that prints the last n letters of the inputted string, 
and the rest of the string.

Input: string="hello", n=3
Output: "llohe"
"""