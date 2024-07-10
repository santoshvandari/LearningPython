while(True):
    print("Enter a q to Quit.")
    a=input("Enter a Value: ")
    if(a=='q' or a=='Q'):
        break
    try:
        print("Processing......")
        a=int(a)
        if(a>10):
            print("Yes input Vaue is Greater than 10.....")
        else:
            print("No Input Value is not Greater than 10....")
    except Exception as e:
        print(f"Failed!!! You have entered Wrong. Error: {e}")
print("Thank You For Playing Game....")