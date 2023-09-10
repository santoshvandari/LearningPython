class Person:
    def printData(self):
        print(f"Name : {self.name}\nAddress : {self.address}\nAge : {self.age}")

p1=Person()
p2=Person()
p1.name="Santosh"
p1.address="Kanakai"
p1.age=23
p2.name="Krian"
p2.address="Birtamode"
p2.age=21
p1.printData()
p2.printData()