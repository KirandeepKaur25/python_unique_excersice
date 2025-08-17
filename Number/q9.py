# write a program that asks user for an hour between 1 and 12 and for 
# how many hours in the future they want to go. Print out what the hour will be that many hours into the future
hour = int(input("enter the number of hours"))
future_hour = int(input("enter the number of hours you want to go into the future"))
if hour >= 1 and hour <= 12:
    print(hour + future_hour)
else:
    print("invalid hour")
    