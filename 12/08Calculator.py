class Calculator:
    def __init__(self,num):
        self.num=num
    def Square(self):
        print(f"Square of {self.num} = {self.num**2}")
    def Cube(self):
        print(f"Cube of {self.num} = {self.num**3}")
    def SquareRoot(self):
        print(f"Square root of {self.num} = {pow(self.num,1/2)}")

calc = Calculator(4)
calc.Square()
calc.Cube()
calc.SquareRoot()