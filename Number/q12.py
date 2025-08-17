# write a program that asks the user for a number and prints out the factorial of that numbers.
x = int(input("Enter the factorial:"))
factorial =1
for i in range(1, x+1):
 factorial = factorial * i
print(factorial)
