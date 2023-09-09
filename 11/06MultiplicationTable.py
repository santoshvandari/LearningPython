num = int(input("Enter a Number To Generate Multiplication Table: "))
with open(f"MultiplicationTable{num}.txt","w") as f:
    i=1
    while i<=10:
        f.write(f"{num} x {i} = {num*i}\n")
        i+=1
print("Table Generated Successfully.")