with open("poems.txt") as f:
    data=f.read()
    print(data)
    if("Twinkle" in data or "twinkle" in data):
        print("Twinkle is Presnet in FIle")
    else:
        print("Twinkle is not Present in File")
