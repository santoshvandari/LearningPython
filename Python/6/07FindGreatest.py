a=int(input("Enter a Number: "))
b=int(input("Enter a Number: "))
c=int(input("Enter a Number: "))
d=int(input("Enter a Number: "))
if(a>b and a>c and a>d):
    print(a," is Greatest")
elif(b>c and b>d):
    print(b," is Greatest.")
elif(c>d):
    print(c," is Greatest.")
else:
    print(d, " is Greatest.")