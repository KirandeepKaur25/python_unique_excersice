'''Write a program that asks the user to enter a power and how many digits they want.
Find the last that many digits of 2 raised to the power the user entered.'''
power = int(input("enter a power:"))
result = 2**power
last_digit = result % 100
print(last_digit)