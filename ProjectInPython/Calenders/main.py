import calendar
try:
    year=int(input("Enter a Year: "))
    disp=calendar.calendar(year)
except Exception as e:
    print("Invalid Entry: Error: ",e)