from functools import reduce
sum = lambda a,b:a+b
List=[1,2,3,4,5]
ListSum=reduce(sum,List)
print(ListSum)