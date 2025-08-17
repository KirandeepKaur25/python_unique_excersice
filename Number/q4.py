#wrtie a program that generates a random decimal number between 1 and 10 with two decimal places of accuracy.
import random
from random import randint
x = round(random.randint(1,10),2)
print(x)
x = random.randint(100, 1000)/100
print(f"{x:.2f}")