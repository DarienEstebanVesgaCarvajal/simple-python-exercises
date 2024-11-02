currentHour =int(input("What's the current hout? (1-12): "))
hoursAdd = int(input("What's number of hours to add?: "))

futureHour = (currentHour + hoursAdd) % 12

if futureHour == 0:
    futureHour = 12

print(f"In {hoursAdd} hours, the clock will show {futureHour}.")