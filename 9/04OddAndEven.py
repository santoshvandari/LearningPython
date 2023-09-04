def odd(n):
    if(n%2):
        print(n, " is a Odd Number.")
    else:
        print(n," is a not a Odd Number.")

def even(n):
    if(n%2):
        print(n," is not a Even Number.")
    else:
        print(n," is a Even Number.")
num=int(input("Enter a Number to Check Odd or Even: "))
odd(num)
even(num)