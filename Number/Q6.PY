#write a program that asks the user to enter two number, x and y  and compute 
from random import randint
x = randint(1, 100)
y = randint(1,100)
numerator = abs(x-y)
denominator = x+y
result = numerator /denominator
print(f" Randomly generated numbers: x = {x},y = {y}")
print(f" The result of |{x}-{y}|/({x}+{y}) is : {result: .4f}")
