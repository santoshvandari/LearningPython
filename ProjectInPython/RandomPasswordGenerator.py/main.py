# importing the necessary module  
import random                       # importing the random module  
 
def GeneratePassword(Type,length):    
    # defining the list of characters that will be used to generate the password  
    PasswordCombination=None
    if(Type==1):
        PasswordCombination="abcdefghijklmnopqrstuvwxyz"
    elif(Type==2):
        PasswordCombination="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    elif(Type==3):
        PasswordCombination="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    elif(Type==4):
        PasswordCombination="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890"
    elif(Type==5):
        PasswordCombination="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()<>?;"

    # defining an empty password string  
    GeneratePassword = ""  
  
    # creating a loop to randomly select the character from the list and insert it in the password string upto the given length  
    for i in range(len):  
        # using the random.choice() method to select a random character from the list and inserting it in the password string  
        GeneratePassword = GeneratePassword + random.choice(PasswordCombination)  
      
    # returning the generated password string  
    return GeneratePassword 

# main function  
if __name__ == "__main__":  
    while(True):
        welcomeDisplay='''\n********** Random Password Generator **********
        1. Combination of Lowercase[a-z]
        2. Combination of Uppercase[A-z]
        3. Combination of Lowercase[a-z] & Uppercase[A-Z]
        4. Combination of Lowercase[a-z], Uppercase[A-Z] & Numbers[0-9]
        5. Combination of Lowercase[a-z], Uppercase[A-Z], Numbers[0-9] & Special Character[@#$%^&*()<>?;]
        6. Quit the Password Generator
        '''
        print(welcomeDisplay)
        combinetype=int(input("Enter Your Choice(1,2,3,4,5,6): "))
        if(combinetype!=6):
            len=int(input("Enter a Length of Password: "))

        
        # defining the length of the password  
        len = 1000  
        # calling the generate_password() function and storing the returned value in a variable  
        pass_str = generate_password(1,len)  
        # printing the final result for the users  
        print("A randomly generated Password is:", pass_str)  