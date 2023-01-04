class DateTools:
    firstYear = 2017
    days = ('Sun', 'Mon', 'Tues', 'Wed', 'Thur', 'Fri', 'Sat')
    daysInMonth = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    monthString = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')
    columnMax = 21
    rowMax = 8

    def __init__(self):
        pass

    def clearscrn():
        print('\33[0;0H')
        for i in range(0,25):
            for j in range (0,81):
                print(f'\33[{i};{j}H ', flush=True, end='')

        print('\33[0;0H', flush=True, end='')

    def leapYear(year:int) -> bool:
        if year%4 != 0:
            return False

        if year%100 == 0 and year%400 != 0:
            return False

        return True

    def fdoyear(year:int) -> int:
        years = year - DateTools.firstYear

        leapYears = years // 4

        otherYears = years - leapYears

        totalDays = otherYears*365 + leapYears*366

        day = totalDays%7

        return day

    def printMonth(month:int, year:int, Row = 1, Col = 1):
        DateTools.clearscrn()
        
        print(f'\33[{Row};{Col}H         {DateTools.monthString[month]}      ')
        Row += 1
        print(f'\33[{Row};{Col}H S  M  T  W  T  F  S ')
        Row += 1

        day = DateTools.fdoyear(year)
        leapYear = DateTools.leapYear(year)

        days = 0
        for i in range(0, month):
            days += DateTools.daysInMonth[i]
            if i == 1 and leapYear:
                days += 1

        days %= 7
        firstDay = (days + day) % 7
        
        for i in range(0, 3*firstDay):
            print(f'\33[{Row};{Col}H ')
            Col += 1

        for i in range(1, DateTools.daysInMonth[month] + 1):
            print(f'\33[{Row};{Col}H{i:2} ')
            Col += 3
            if Col % 21 == 1:
                Row += 1
                Col = 1

    def printYear(year:int):
        row = 1
        column = 1
        for month in range(0, 12):
            DateTools.printMonth(month, year, row)