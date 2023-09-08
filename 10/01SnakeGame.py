'''
We all have played snake water gun game in our childhood. 
If you haven't, google the rules of the game and write a python program capable of playing this gmae with the users.
'''
import random
def GameStatus(com,you):
    if com ==you:
        return None
    elif com=="s":
        if you=="g":
            return True
        if you=="w":
            return False
    elif com=="w":
        if you=="s":
            return True
        if you=="g":
            return False
    elif com=="g":
        if you=="w":
            return True
        if you=="s":
            return False
def Check(choose):
    if choose=="s":
        return "Snake"
    elif choose=="w":
        return "Water"
    elif choose=="g":
        return "Gun"



print("Computer Turn: Choose Snake(s),Water(w), Gun(g): ")

com=random.randint(1,3)
if com==1:
    com="s"
elif(com==2):
    com="w"
else:
    com="g"


you = input("Your Turn: Choose Snake(s),Water(w),Gun(g): ")
you = you.lower()


print(f"Computer Choose {Check(com)}")
print(f"You Choose {Check(you)}")

result=GameStatus(com,you)

if result==None:
    print("Tie!!!")
elif result:
    print("You Win!!!")
else:
    print("You Loose!!!")

