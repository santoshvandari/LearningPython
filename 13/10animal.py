class Animal:
    def __init__(self,name):
        self.name=name 
    
class Pets(Animal):
    def __init__(self,name,gender):
        super().__init__(name)
        self.gender=gender

class Dog(Pets):
    def __init__(self,name,gender,bark):
        super().__init__(name,gender)
        self.bark=bark
    def Display(self):
        print(f"Name : {self.name}\nType : {self.gender}")
    def Bark(self):
        print(f"Barking : {self.bark}")

dog = Dog("Jenny","Female","Bow Bow")
dog.Display()
dog.Bark()

