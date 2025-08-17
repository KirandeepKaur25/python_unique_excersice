# write a program that generates 50 random numbers 
# such that the first number is between 1 and 2,
#  the second is between 1 and 3, 
# the third is between 1 and 4,..,
#  and the last is between 1 and 51
import random
random_number = []
for n in range(1,51):
    num = random.randint(1, n+1)
    random_number.append(num)
for i , num in enumerate(random_number, 1):
    print(f"Number {i}: {num}")
    



