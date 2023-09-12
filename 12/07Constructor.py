class ConstructorDemo:
    name=address=None
    def __init__(self,name,address):
        self.name=name
        self.address=address
    def Display(self):
        print(f"Name = {self.name}\nAddress = {self.address}")

