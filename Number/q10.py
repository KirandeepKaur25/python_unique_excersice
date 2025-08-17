'''One way to find out the last digit of a number is to mod the number by 10. Write a
program that asks the user to enter a power. Then find the last digit of 2 raised to that
power'''
power = int(input("Enter the power:"))
result = 2**power
last_digit = result % 10
print(f"2 raised to the power of {power} is {result}")
print(f"The last digit is : {last_digit}")

