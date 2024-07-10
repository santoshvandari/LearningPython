def Sum(n):
    if(n==0):
        return 0
    return n+Sum(n-1)
print("Sum from 0 to 10 = "+str(Sum(10)))