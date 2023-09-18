import random
randomNum= random.randint(1,100)
print(randomNum)
Guess=0
GuessNumber=None
while(GuessNumber!=randomNum):
    GuessNumber=int(input("Enter a Guess Number: "))
    Guess+=1
    if(GuessNumber==randomNum):
        print(f"You have Guess the Correct Number in {Guess} Guesses!!!")
    else:
        if(GuessNumber>randomNum):
            print("You Guessed Wrong Number! Please Guess Smaller Number.")
        else:
            print("You Guessed Wrong Number! Please Guess Larger Number.")
with open("HighestScore.txt","r") as f:
    highScore=int(f.read())
if(highScore>Guess):
    print("Congrats!!! You Have Broken Highest Score Record!")
    with open("HighestScore.txt","w") as f:
        f.write(str(Guess))