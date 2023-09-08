'''
We all have played snake water gun game in our childhood. 
If you haven't, google the rules of the game and write a python program capable of playing this gmae with the users.
'''
import random
def GameStatus():
    pass
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
result=GameStatus(com,you)
