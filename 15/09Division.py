try:
    n1=int(input("Enter First Number: "))
    n2=int(input("Enter Second Number: "))
    print(f"{n1}/{n2} = {n1/n2}")
except ZeroDivisionError:
    print("Infinite")
    