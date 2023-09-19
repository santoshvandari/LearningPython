while(True):
    print("Enter a q to Quit.")
    a=input("Enter a Value: ")
    if(a=='q' or a=='Q'):
        break
    try:
        a=int(a)
        if(a>10):
            print("Yes input Vaue ")