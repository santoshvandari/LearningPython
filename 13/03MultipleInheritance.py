class Parent1:
    def p1Display(self):
        print("Displaying from Parent1...")

class Parent2:
    def p2Display(self):
        print("Displaying from Parent2...")

class Child(Parent1,Parent2):
    def Display(self):
        print("Displaying From Child Class....")
