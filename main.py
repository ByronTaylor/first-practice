from datetime import date
import math

def getBirthday():
    YYYY = int(input("In what year were you born? "))
    print("In what month were you born?")
    month = str(input('Type at least the first three letters. '))
    if month[:3].lower() == "jan":
        MM = 1
    elif month[:3].lower() == "feb":
        MM = 2
    elif month[:3].lower() == "mar":
        MM = 3
    elif month[:3].lower() == "apr":
        MM = 4
    elif month[:3].lower() == "may":
        MM = 5
    elif month[:3].lower() == "jun":
        MM = 6
    elif month[:3].lower() == "jul":
        MM = 7
    elif month[:3].lower() == "aug":
        MM = 8
    elif month[:3].lower() == "sep":
        MM = 9
    elif month[:3].lower() == "oct":
        MM = 10
    elif month[:3].lower() == "nov":
        MM = 11
    elif month[:3].lower() == "dec":
        MM = 12
    else:
        print("I'm going to crash now because you can't follow simple directions.")
    DD = int(input("On what day of the month were you born? "))

    birthday = date(YYYY, MM, DD)
    return birthday

birthday = getBirthday()
days = date.today() - birthday

def getCandles(days):
    numDays = days.days
    print("numDays = ", numDays)
    years = numDays / 365
    print(years)
    numYears = math.floor(years)
    #  candles_lifetime = 0
    for i in range(1, numYears):
        numYears += i
    print(numYears)

getCandles(days)



