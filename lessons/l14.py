# Today, we continued working on our trivia game project
"""Mini Project: Trivia Game (remainder of class) 
	1.	Create at least 3 trivia questions, and prompt the user. 
	2.	Count how many the user gets right, and if they get a score above 70%, they win! 
	3.	If the user fails, they have to redo the trivia quiz until they win. 
	4.	Make sure to randomize the order the questions go in."""
import random
score = 0
win = "lose"
while win == "lose":
    questions_done = " "
    for i in range(3):
        question_num = random.randint(1,3)
        if str(question_num) in questions_done:
            question_num = 0
        if question_num == 1:
            questions_done = questions_done + "1"
            question = input("Find the sum: 1/1^2 + 1/2^2 + 1/3^2 ... use pi for pi")
            if question == "1":
                score += 1
        if question_num == 2:
            questions_done = questions_done + "2"
            question = input("What day did the american revelution start?")
            if question == "2":
                score += 1
        if question_num == 3:
            questions_done = questions_done + "3"
            question = input("What is the distance from the earth to the sun to the nearest million miles?")
            if "3" in question or "93 000 000" in question or "93000000" in question:
                score += 1
    print("---------------")
    score_per = score/3
    if score_per > 0.7 :
        win = "win"
        break
print("You win!!!!!!!")
