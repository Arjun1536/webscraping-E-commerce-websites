print("enter any two number")
n1 = int(input())
n2 = int(input())
while True :
    print("enter the element 1. Addition 2.Subtraction 3. Multiplication 4. Division")
    choice = int(input())
    if choice == 1:
        n = n1+n2
        print(n)
    elif choice == 2:
        n = n1-n2
        print(n)
    elif choice == 3:
        n  =n1*n2
        print(n)
    elif choice == 4:
        n = n1/n2
        print(n)

    else:
        print("invalid character")