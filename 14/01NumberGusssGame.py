# Create a Game that will ask the user to guess the random number. If the User Guess the Smaller Number, then Suggest to Guess the Larger Number and if the User Guess the Larger Number, then Suggest to Guess the Smaller Number.
# Importing the Random Module for the Generating the Random Number
import random
# Generating the Random Number
randomNum= random.randint(1,100)
# print(randomNum)
Guess=0
GuessNumber=None
# Looping the Guessing Process Until the Guess Number is equal to Random Number.
while(GuessNumber!=randomNum):
    print("Enter q to Quit the Game")
    try:
        GuessNumber=input("Enter a Guess Number: ")
        # If the User Guess is Correct.
        if(GuessNumber=="q" or GuessNumber=="Q"):
            print("Thank You for Playing Game....")
            exit()
        else: 
            Guess+=1
            GuessNumber=int(GuessNumber)
            if(GuessNumber==randomNum):
                print(f"You have Guess the Correct Number in {Guess} Guesses!!!")
            # If the User Guess is not correct.
            else:
                if(GuessNumber>randomNum):
                    print("You Guessed Wrong Number! Please Guess Smaller Number.")
                else:
                    print("You Guessed Wrong Number! Please Guess Larger Number.")
    except Exception as e:
        print("Failed!!! Your Entered Something Wrong. Error: ",e)

try:
    # Reading the Highest Score File of the Previously set.
    with open("HighestScore.txt","r") as f:
        highScore=int(f.read())
    # Rewriting the Highest Score if it is a New Hightest Score
    if(highScore>Guess):
        print("Congrats!!! You Have Broken Highest Score Record!")
        with open("HighestScore.txt","w") as f:
            f.write(str(Guess))
except Exception as e:
    print("Failed to Open File!!! Error: ",e)