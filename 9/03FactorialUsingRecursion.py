def Factorial(n):
    if(n==0):
        return 1
    return n*Factorial(n-1)
number = int(input("Enter a Number to Calculate Factorial: "))
print("Factorial of ",number," is ",Factorial(number))