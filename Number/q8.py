#write a program that asks the users for a number of seconds
#  and prints out how many minutes and seconds that is. 
# For instance, 200 seconds is 3 minutes and 20 seconds. 
def convert_to_minutes_and_seconds(seconds):
    minutes = seconds // 60
    seconds = seconds % 60
    return minutes, seconds
# ask the future 
seconds = int(input("Enter the number of seconds:"))
minutes, seconds = convert_to_minutes_and_seconds(seconds)
print(f"{minutes} minutes and {seconds} seconds")  # f-string formatting to print minutes
