class Person:
    def __init__(self,name):
        print("Initilizing Person....")
        self.name=name
    def Display(self):
        print(f"Name of Person : {self.name}")