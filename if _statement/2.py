from random import randint
num = randint(1,10)
guess = eval(input("enter your guess:"))
if guess==num:
    print('You got it!')
else:
    print('Sorry. The number is ', num)
