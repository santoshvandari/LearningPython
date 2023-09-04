fact = 1
def Factorial(n):
    if(n==0):
        return fact
    fact*Factorial(n-1)
number = int(input("Enter a Number to Calculate Factorial: "))