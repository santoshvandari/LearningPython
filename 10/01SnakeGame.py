'''
We all have played snake water gun game in our childhood. 
If you haven't, google the rules of the game and write a python program capable of playing this gmae with the users.
'''
# Importing Random to Generate Random Number
import random
# Defining the Funciton to Check the Status fo the Game. What Win
def GameStatus(com,you):
    if com ==you:
        # When Both are Equal
        return None
    elif com=="s":
        if you=="g":
            # Snake Get Killed By Gun
            return True
        if you=="w":
            # Snake Drink the Water
            return False
    elif com=="w":
        if you=="s":
            # Snake Drink the Water
            return True
        if you=="g":
            # Gun Get Destroyed by Water
            return False
    elif com=="g":
        if you=="w":
            # Gun Get Destroyed by Water
            return True
        if you=="s":
            # Snake Get Killed By Gun
            return False
# Function to Return What User had Selected
def Check(choose):
    if choose=="s":
        return "Snake"
    elif choose=="w":
        return "Water"
    elif choose=="g":
        return "Gun"
# Creating the Main Function for the Recursion
def Main():
    # Print the Message to make the choose by computer
    print("Computer Turn: Choose Snake(s),Water(w), Gun(g): ")
    # Generating Random Number and Making The Choice according to that Number
    com=random.randint(1,3)
    if com==1:
        com="s"
    elif(com==2):
        com="w"
    else:
        com="g"
    # Asking for the User to Choose One of the Option
    you = input("Your Turn: Choose Snake(s),Water(w),Gun(g): ")
    you = you.lower()
    #  Printing What Compute and User Choose
    print(f"Computer Choose {Check(com)}")
    print(f"You Choose {Check(you)}")
    # Checking the Status of the Game
    result=GameStatus(com,you)
    #  Printing the Result of the Game
    if result==None:
        print("Tie!!!")
    elif result:
        print("You Win!!!")
    else:
        print("You Loose!!!")
    # Invoking the Main Function for the loop
    print()
    Main()
# Invoking the Main Function for Once Execution
Main()