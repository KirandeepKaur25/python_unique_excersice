# write a program that generates a random number 
# , x , between 1 and 50 , a random number 
# y and between 2 and 5  and computes x the power y.
import random 
from random import randint
x = randint(1,50)
y = randint(2 , 5)
z = x**y
print(f"the value of x is {x} and the value of y is {y}\n"
      f"the value of x to the power of y is {z}")  # output: the value of

print(z)
