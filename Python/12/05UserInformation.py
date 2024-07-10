class Person:
    name=address=age=None
    def setInfo(self,n,a,ag):
        self.name=n
        self.address=a
        self.age=ag
    def printData(self):
        print(f"Name : {self.name}\nAddress : {self.address}\nAge : {self.age}")

p1=Person()
p2=Person()
p1.setInfo("Santosh Bhandari","Kanakai-07",23)
p2.setInfo("Kiran Sharma","Birtamode-03",21)
p1.printData()
p2.printData()