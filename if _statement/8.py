#  A store charges $12 per items if you buy less than 10 items. if you buy between 10 and 99 items, 
# the cost is $10 per items. 
# if you buy 100 or more items, the cost is $7 per items.
# write a program that asks the user how many items they are buying and prints the total
items= int(input("Enter the number of items:"))
if items <10:
    print("The total cost is $", items*12)
elif 10 <= items <= 99:
    print("The total cost is $", items*10)
else:
    print("The total cost is $", items*7) 
     # This line is indented