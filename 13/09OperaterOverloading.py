class Data:
    def __init__(self,num):
        self.number=num
    def __add__(obj1,obj2):
        return obj1.number+obj2.number
    def __sub__(obj1,obj2):
        return obj1.number-obj2.number
    def __mul__(obj1,obj2):
        return obj1.number*obj2.number
    def __truediv__(obj1,obj2):
        return obj1.number/obj2.number

obj1=Data(10)
obj2=Data(5)
print(obj1+obj2)
print(obj1-obj2)
print(obj1*obj2)
print(obj1/obj2)