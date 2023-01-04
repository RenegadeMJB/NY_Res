class DateTools:
    firstYear = 2021
    days = ('Fri', 'Sat', 'Sun', 'Mon', 'Tues', 'Wed', 'Thur')
    def __init__(self):
        pass

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