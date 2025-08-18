# write a program that asks the user how many credits they have taken. if they have taked 23 or less, print that the student is a freshman. 
# if they have taken between 24 and 53. print the they are a sophomore. 
# the range for juniors is 54 and 83, and for seniors it is 84 and over.
credits = int(input("how mamy credits have you taken?"))
if credits <=23:
    print("You are a freshman.")
elif 24<= credits <=53:
    print("you are a sophomore.")
elif 54<= credits <=83:
    print("you are a junior.")
else:
    print("you area a senior.")