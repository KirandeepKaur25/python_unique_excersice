# fibonacci series
n = int(input("how many Fiboncci number should I print?"))
if n == 0 :
    print("No number to print.")
elif n == 1:
    print(1)
else:
    a, b = 1,1
    print (a, end='')
    print(a, end='')
    for i in range(2,n):
        c = a+b
        print(c, end=' ')
        a , b = b, c
    print()