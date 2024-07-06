def Sum(*num):
    sum = 0
    for i in num:
        sum+=i
    return sum

print(Sum(1))
print(Sum(5,6,8,10))
print(Sum(2,6,9,10,22,59))
print(Sum(15,6,5,10))