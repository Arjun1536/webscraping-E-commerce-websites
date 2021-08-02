def fact(n):
    if n ==1 or n == 2:
        return 1
    return fact(n-1) + fact(n-1)
print(fact(4))