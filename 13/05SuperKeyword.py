class Person:
    def __init__(self,name):
        print("Initilizing Person....")
        self.name=name
    def Display(self):
        print(f"Name of Person : {self.name}")

class Employee(Person):
    def __init__(self,name,company):
        super().__init__(name)
        self.company=company
        print("Initilizing Employee....")
        self.name=name
    def Display(self):
        super().Display()
        print(f"Company of Employee : {self.company}")

emp = Employee("Santosh","Google")
emp.Display()