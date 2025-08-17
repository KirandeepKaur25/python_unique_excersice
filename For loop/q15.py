'''
h = int( input("enter the size of the letter A:"))
print(" " * (size-1)+"*")
for i in range(1, size-1):
    left_space = " " *(size -1-i)
    middle_space = " " (2* i -1)
    print(left_space ="*" + middle_space + "*")
print("*" * (2 * size-1))

for i in range(size -2, 0 , -1):
    left_space =" " * (size -1-i)
    middle_space = " " * (2* i -1)
    print( left_space + "*" + middle_space + "*")
print ( " " * (size -1) + "*")
'''
size = int(input("Enter the size of the letter A: "))

# Top part (single *)
print(" " * (size - 1) + "*")

# Middle part (before the crossbar)
for i in range(1, size - 1):
    left_space = " " * (size - 1 - i)
    middle_space = " " * (2 * i - 1)
    print(left_space + "*" + middle_space + "*")

# Crossbar (solid line of *)
print("*" * (2 * size - 1))

# Bottom part (after the crossbar)
for i in range(size - 2, 0, -1):
    left_space = " " * (size - 1 - i)
    middle_space = " " * (2 * i - 1)
    print(left_space + "*" + middle_space + "*")

# Bottom single * (optional, matches the top)
print(" " * (size - 1) + "*")