import calendar
try:
    disp=calendar.calendar(year)
    print(disp)
except Exception as e:
    print("Invalid Entry: Error: ",e)