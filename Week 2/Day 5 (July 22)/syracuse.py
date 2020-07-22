def syracuse(n):
    if (n%2==0):
        return n//2
    else:
        return (3*n+1)


a = 123456789

while (a!=1):
    print(a)
    a = syracuse(a)

print(a)
