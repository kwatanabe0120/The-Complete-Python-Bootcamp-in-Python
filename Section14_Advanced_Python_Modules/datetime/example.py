import datetime

today = datetime.date.today()
print(f"Year: {today.year}, Month: {today.month}, Day: {today.day}")

my_datetime = datetime.datetime(2021,10,3,14,20,1)
print(my_datetime)

print(my_datetime.replace(year=3000))

date1 = datetime.date.today()
date2 = datetime.date(2000,1,1)
result = date1 - date2
print(result.days)

