w = int(input("enter the width of the box:"))
h = int(input("enter the height of the box:"))
print("*" * w)
for i in range(h-2):
    if w >= 2:
        print('*'+''*(w -2)+'*')
    else:
        print('*')

    if h > 1:
        print( '*'* w)
