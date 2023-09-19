import math
increment=lambda a:a+10
listitems=[25,45,48]
incrementList=list(map(increment,listitems))
print(incrementList)


def Cube(n):
    # return math.pow(n,3)
    return n*n*n
item=[1,2,3,4,5,6,7,8,9,10]
print(list(map(Cube,item)))