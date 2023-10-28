class ParentClass:
    def Display(self):
        print("Reading from the Parent Class...")

class ChildClass(ParentClass):
    def Display1(self):
        print("Reading from the Child Class....")

child = ChildClass()
child.Display()
child.Display1()