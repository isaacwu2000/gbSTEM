user_correct_answers = 0
while user_correct_answers < 3:
    user_answer = int(input("1 + 1 = "))
    if user_answer == 2:
        user_correct_answers += 1
        print("correct")
    else:
        print("incorrect")
