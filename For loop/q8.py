# write a program that asks the user for their name and how many times to print it. The program should print out the user's name the specified number of times.
name = input("Enter your name:")
times = int(input("how many times should it be printed?"))
for i in range(times):
    print(name)