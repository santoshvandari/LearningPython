class Animal:
    def __init__(self,name):
        self.name=name 
    
class Pets(Animal):
    def __init__(self,name,types):
        super().__init__(name)
        self.type=types

class Dog(Pets):
    def __init__(self,name,type,bark):
        super().

