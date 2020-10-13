import calendar
import datetime
value= datetime.datetime.now()
time= calendar.HTMLCalendar(firstweekday=0)
print(time.formatmonth(int(value.strftime("%Y")), int(value.strftime("%m"))))
