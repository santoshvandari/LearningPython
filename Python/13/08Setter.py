class Employee:
    name="krian"
    salary=100
    bonus=50
    @property
    def totalSalary(self):
        return self.salary+self.bonus
    @totalSalary.setter
    def totalSalary(self,value):
        self.bonus=value-self.salary

e=Employee()
print(e.name)
print(e.salary)
print(e.bonus)
print(e.totalSalary)
e.totalSalary=110
print(e.bonus)