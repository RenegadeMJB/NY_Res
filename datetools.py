class DateTools:
    firstYear = 2021
    days = ('Fri', 'Sat', 'Sun', 'Mon', 'Tues', 'Wed', 'Thur')
    daysInMonth = (31, 28, 31, 30, 31, 30, 31, 31, 31, 31, 30, 31)
    monthString = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')

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

    def printMonth(month:int, year:int):
        DateTools.clearscrn()
        
        print(f'  {DateTools.monthString[month]}   ')
        print('S M T W T F S')