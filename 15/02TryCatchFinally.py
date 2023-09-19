try:
    num1=int(input("Enter First Number: "))
    num2=int(input("Enter Second Number: "))
    print(f"Division : {num1/num2}")
except Exception as e:
    print("Error: ",e)
finally:
    print("Code Executed!!!")