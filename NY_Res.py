from datetools import DateTools as DT

print(DT.leapYear(2024))
days = ('Sun', 'M', 'Tue', 'W', 'Thur', 'F', 'Sat')
for i in range(2023, 2050):
    day = DT.fdoyear(i)
    print(i, days[day])