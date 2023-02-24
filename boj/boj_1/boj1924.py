import datetime

days = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
x, y = map(int, input().split())
date = datetime.date(2007, x, y)
print(days[date.weekday()])