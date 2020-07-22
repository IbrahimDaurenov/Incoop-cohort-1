def fibbo(n):
    if (n==1 or n==2):
        return 1
    else:
        return ( fibbo(n-1) + fibbo(n-2) )


print(fibbo(1))
print(fibbo(2))
print(fibbo(3))
print(fibbo(4))
print(fibbo(5))
print(fibbo(6))
print(fibbo(7))
print(fibbo(8))
print(fibbo(9))
