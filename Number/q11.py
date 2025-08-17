'''Write a program that asks the user to enter a weight in kilograms. The program should
convert it to pounds, printing the answer rounded to the nearest tenth of a pound.'''
weight_Kg = float(input("Enter the weight_in_kg:"))
weight_pound = weight_Kg*2.2
print("Weight in pound is: ", round(weight_pound,1))
