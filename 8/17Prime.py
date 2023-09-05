num = int(input("Enter a Number: "))
count=0
for i in range(2,num):
    if(num%i==0):
        count=1
        break
if(count):
    print(str(num)+" is a Not Prime Numeber.")
else:
    print(str(num)+" is a Prime Numeber.")