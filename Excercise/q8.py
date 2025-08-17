# write a program that  asks the user to enter three numbers.
# Create a variable called total and average that hold the sum and average of the three numbers and print out the values of total and average.
num1 = int(input("Enter a number:"))
num2 = int(input("Enter a number:"))
num3 = int(input("Enter a number:"))
total = num1 + num2 + num3
average = total / 3
print("The total is: ", total)
print("The average is: ", average)
