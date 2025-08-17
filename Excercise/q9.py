# A lot of cell phones have tip calculators. write one. 
# Ask the users for the price of the meal and the percent
#  tip they want to leave. Then print both the tip  amount
#  and the total bill with the tip included.
user = int(input("Enter the price of meal:"))
tip = int(input("Enter the percent of tip:"))
tip_amount = (user * tip) / 100
total_bill = user + tip_amount
print("The tip amount is: ", tip_amount)