class Person:
    def __init__(self,name):
        print("Initilizing Person....")
        self.name=name
    def Display(self):
        print(f"Name of Person : {self.name}")

class Employee(Person):
    def __init__(self,name,comapny):
        super(name)
        self.company=comapny
        print("Initilizing Employee....")
        self.name=name
    def Display(self):
        super().Display()
        print(f"Company of Employee : {self.company}")

