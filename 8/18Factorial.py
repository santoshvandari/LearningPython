n=int(input("Enter a Number: "))
fact = 1
for i in range(1,n+1):
    fact*=i
    i+=1
print("Factorial of "+str(n)+" = "+str(fact))