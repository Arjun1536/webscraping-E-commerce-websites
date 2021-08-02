'''
def count(n):
    c= 0
    while n>=0:
        if n%2==0:
            n =n/2
            c+=1
        else:
            c+=1
    return c
print(count(10))'''

def matrix(n,m):
    a =[]
    for i in range (n):
        c = []
        for j in range (m):
            j  = int(input("enter number ["+str(i)+"] ["+str(j)+"]"))
            c.append(j)
        a.append(c)
    return a
def printmatrix(a):
    for i in range(len(a)):
        for j in range(len(a[0])):
            print(a[i][j],end = " ")
        print()

n = int(input("enter row"))
m = int(input("enter column"))
r = matrix(n,m)
printmatrix(r)