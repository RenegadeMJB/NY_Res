class DateTools:

    def __init__(self):
        pass

    def leapYear(year:int) -> bool:
        if year%4 != 0:
            return False

        if year%100 == 0 and year%400 != 0:
            return False
            
        return True

    