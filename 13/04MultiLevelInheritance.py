class GrandParent:
    def gDisplay(self):
        print("Displaying From Grand Parent...")

class Parent(GrandParent):
    def pDisplay(self):
        print("Displaying From Parent....")

class Child(Parent):
    def cDisplay(self):
        print("Displaying From Child...")

c= Child()
c.gDisplay()
c.pDisplay()
c.cDisplay()