class Employee:
    company="ABC"

emp1=Employee()
emp2=Employee()
print(emp1.company, emp2.company)
Employee.company="XYZ"
print(emp1.company, emp2.company)