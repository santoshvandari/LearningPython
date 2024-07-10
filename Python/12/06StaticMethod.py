class Greeting:
    # def Greet(self):
        # print("Welcome to the World of Programming!!!")
    @staticmethod
    def Greet(name):
        print(f"Welcome {name} the World of Programming!!!")
    @staticmethod
    def Greet1():
            print(f"Welcome in the World of Programming!!!")

greet = Greeting()
greet.Greet("Santosh") 
greet.Greet1()