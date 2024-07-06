def Display(n):
    if(n==1):
        return print("Hello "+str(n))
    print("Hello "+str(n))
    return Display(n-1)

# Display(5)
# Display(2)
Display(10)