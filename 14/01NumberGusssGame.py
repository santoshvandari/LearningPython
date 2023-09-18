import random
randomNum= random.randint(10,20)
Guess=0
GuessNumber=None
while(GuessNumber==randomNum):
    GuessNumber=int(input("Enter a Guess Number: "))
    Guess+=1
    if(GuessNumber==randomNum):
        print(f"You have Guess the Correct Number in {Guess} Guesses!!!")
    else:
        if(GuessNumber>randomNum):
            print("You Guessed Wrong Number! Please Guess Smaller Number.")