import calendar
try:
    # year=int(input("Enter a Year: "))
    year=2020
    disp=calendar.calendar(year)
    print(disp)
except Exception as e:
    print("Invalid Entry: Error: ",e)