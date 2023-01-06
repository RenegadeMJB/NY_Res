from datetools import DateTools as DT
from datetime import datetime
import os


class Day:
    yellow = '\u001b[43m'
    green = '\u001b[42m'
    reset = '\u001b[0m'

    def __init__(self, numberResolutions):
        self._finished = []
        for i in range(0, numberResolutions):
            self._finished.append(False)
        self._color = Day.reset
        self._dayOfYear = datetime.now().timetuple().tm_yday - 1 

    def checkOff(self):
        for index, res in enumerate(self._finished):
            if res == False:
                self._finished[index] = True
                self.pickColor()
                break
    
    def pickColor(self, set=False):
        started = False
        done = False
        if True in self._finished:
            started = True

        if started == True and False not in self._finished:
            done = True

        if done:
            self._color = Day.green
            if set == True:
                print(f'{self._color}', flush=True, end='')
        elif started:
            self._color = Day.yellow
            if set == True:
                print(f'{self._color}',flush=True,end='')


class Year:
    def __init__(self, year, numberResolutions, days = []):
        self._year = year
        self._days = []
        self._numberResolutions = numberResolutions
        if DT.leapYear:
            totalDays = 366
        else:
            totalDays = 365
        if days == []:
            for day in range(0, totalDays + 1):
                newDay = Day(numberResolutions)
                self._days.append(newDay)
        else:
            for day in days:
                self._days.append(day)

        
    def run(self):
        currDay = Day(self._numberResolutions)
        self._days[currDay._dayOfYear]
        self._days[currDay._dayOfYear].checkOff()
        self.printYear()

    def addDay(self):
        day = Day(self._numberResolutions)
        self._days.append(day)

    def printYear(self):
        DT.clearscrn()
        row = 1
        column = 1
        for month in range(0,12):
            self.printMonth(month, row, column)
            column += 24
            if (month + 1) % 4 == 0:
                if month != 0:
                    column = 1
                    row += 9

    def printMonth(self, month:int, rowStart = 1, columnStart = 1):
        #DT.clearscrn()
        
        Col = columnStart
        Row = rowStart

        print(f'\33[{Row};{Col}H         {DT.monthString[month]}      ')
        Row += 1
        print(f'\33[{Row};{Col}H S  M  T  W  T  F  S ')
        Row += 1

        firstDayYear = DT.fdoyear(self._year)
        leapYear = DT.leapYear(self._year)

        #this is figuring out how many days up to that month not including the month
        days = 0
        for i in range(0, month):
            days += DT.daysInMonth[i]
            if i == 1 and leapYear:
                days += 1

        FirstDayMonth = (days%7 + firstDayYear) % 7
        
        for i in range(0, 3*FirstDayMonth):
            print(f'\33[{Row};{Col}H ')
            Col += 1

        for dayNumber in range(1, DT.daysInMonth[month] + 1):
            curDay = self._days[days]
            days += 1
            curDay.pickColor(set=True)
            print(f'\33[{Row};{Col}H{dayNumber:2} {Day.reset}')
            Col += 3
            colRelative = Col - columnStart
            if colRelative % 21 == 0:
                if colRelative != 3:
                    Row += 1
                    Col = columnStart

        if month == 1 and leapYear:
            leapDay = 29
            print(f'\33[{Row};{Col}H{leapDay:2} ')
            return (DT.daysInMonth[month] + 1)





def main():
    cmd = """osascript -e '
    tell application "Terminal"
        set bounds of front window to {700, 50, 1412, 510}
    end tell
    '
    """
    os.system(cmd)

    year = Year(2023, 2)
    year.run()

    input("Please press Enter....")
    DT.clearscrn()

if __name__ == "__main__":
    main()
    
