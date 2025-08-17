h = int(input("enter the height of the diamond ( must be odd):"))
if h % 2 == 0:
    print("Height must be odd. Please try again.")
else:
    for i in range(1, h //2 +2):
        spaces = " " * ((h // 2+1) - i)
        stars ="*" * (2*i -1)
        print(spaces + stars)
    
    for i in range(h // 2, 0, -1):
        spaces = " " * ((h //2+1)-i)
        stars = "*" *(2*i -1)
        print( spaces + stars)

                        