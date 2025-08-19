# write a multiplication game program for kids.
#  The program should give the players ten randomly generated 
# multiplication questions to do. 
# After each, the program should tell him whether 
# they got it right or wrong and what the corrected answer
#  is;-
'''x = int(input("Enter the value:"))
y - int(input("Enter the value:"))
if x * y == 12 : 
    print("Right!")
    else x* y == 44:
    print(f"Wrong the answer is {x*y}")'''
import random
print("Welcome to the Multiplication game!")
print("you'll get 10 mulitiplication problems to solve.")
print("let's begin\n")

score = 0

for question in range(1,11):
    x = random.randint(1,12)
    y = random. randint(1,12)

    user_answer = int(input(f"quesion{question}: what is {x} * {y}?"))
    correct_answer = x*y
    if user_answer == correct_answer:
        print("Right!")
    else:
        print(f"wrong! the correct answer is {correct_answer}\n")
    
print(f"Game over! your score is {score}/10")
if score == 10:
   print("Perfect ! you're a multiplication master!")
elif score >=7:
   print("Good job! you're doing well!")
elif score>= 6:
   print("no bad! keep practising!")
else:
    print(" keep practicing! you'll get better!")
