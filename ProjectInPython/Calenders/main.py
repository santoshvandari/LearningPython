import calendar
try:
    year=int(input("Enter a Year: "))
    calender=calendar(year)
    print(calender)
except Exception as e:
    print("Invalid Entry: Error: ",e)