listitem=[10,55,1,5,4,48,45695,5456,6656,61,45,56]
def Even(n):
    if(n%2):
        return False
    return True

evenNumber=list(filter(Even,listitem))
print(evenNumber)