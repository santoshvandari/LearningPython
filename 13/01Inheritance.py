class Employee:
    company="Google"
    def getDetails(self):
        print(f"Work at {self.company}")

class Programmer(Employee):
    def __init__(self,lang):
        self.language=lang
    def getLanguage(self):
        print(f"Work With {self.language}.")
    def getDetails(self):
        print(f"Working as Programmer")

e=Employee()
e.getDetails()
p=Programmer("Python")
p.getDetails()
p.getLanguage()