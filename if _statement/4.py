# write a program that asks the user to enter.
# a length in centimeter. If the user enters 
# a negative length, the program should tell the 
# user that the entry is invaild. Otherwise,
# the should covert the lenght to inches.
centimeter = int(input("Enter the value of centimeter:"))
if centimeter<0:
    print("Invalid entry")
else:
    inch = centimeter * 2.54
    print(inch)