class Employee:
    name="Krishna"
    salary=500
    salaryBonus=50
    @property
    def TotalSalary(self):
        return self.salary+self.salaryBonus

e=Employee()
print(e.name)
print(e.salary)
print(e.salaryBonus)
print(e.TotalSalary)