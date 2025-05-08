# Today, we continued working on our trivia game project
"""
Mini Project: Trivia Game (remainder of class) 
	1.	Create at least 3 trivia questions, and prompt the user. 
	2.	Count how many the user gets right, and if they get a score above 70%, they win! 
	3.	If the user fails, they have to redo the trivia quiz until they win. 
	4.	Make sure to randomize the order the questions go in.
"""
score = 0
q1 = input("Who is the best muscian")
if q1 == "person a" or q1 = "person b":
    score += 1
q2 = input("1+1=")
if q2 == "2":
    score += 1
q3 = input("1+2=")
if q3 == "3":
    score += 1
print("Score", score)