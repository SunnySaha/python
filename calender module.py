import calendar

#print(calendar.TextCalendar(firstweekday=4).formatyear(2015))

m, d, y = map(int,input().split())

print((calendar.day_name[calendar.weekday(y, m, d)]).upper())