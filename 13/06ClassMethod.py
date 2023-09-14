class Employee:
    name="Ayush"
    salary=500

    @classmethod
    def ChangeSalary(cls,amt):
        cls.salary=amt

e=Employee()
print(e.name)
print(e.salary)
print(Employee.salary)
e.ChangeSalary(1000)
print(Employee.salary)