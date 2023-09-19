try: 
    num=int(input("Enter a Number: "))
    print(1/num)
except Exception as e:
    print(e)
else:
    print("Successfully Executed!!")