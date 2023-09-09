with open("WithFile.txt","a") as f:
    f.write("Hello, I am Using WIth to Open file")
    
with open("WithFile.txt","r") as file:
    data = file.read()
    print(data)


with open("WithFile.txt","w") as f:
    f.write("Hello, I am Using WIth to Open file")




