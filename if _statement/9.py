# write a program that asks the user to enter a number and prints out all the divisors of that numbers.
num = int(input("enter a number:"))
print(f"the divisors of {num} are:")
for i in range(1, num+1):
    if num % 1 ==0:
        print(i)


