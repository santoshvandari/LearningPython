import calendar
try:
    # year=int(input("Enter a Year: "))
    year=2020
    calender=calendar.month(year,1)
    print(calender)
except Exception as e:
    print("Invalid Entry: Error: ",e)