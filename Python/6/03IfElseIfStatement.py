'''Check the Division of the Marks. Here are the conditions
marks 0-20: failed
21-60: Third Division
61-80: Second Division
81-100: First Division
'''
mark=int(input("Enter the Marks: "))
if(mark>=0 and mark<=20):
    print("Failed")
elif(mark>20 and mark<=60):
    print("Third Division......")
elif(mark>60 and mark<=80):
    print("Second Division......")
elif(mark>80 and mark<=100):
    print("First Division......")
else:
    print("Invalid Marks......")