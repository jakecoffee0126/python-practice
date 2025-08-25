# https://www.w3schools.com/python/python_datetime.asp

import datetime

# we can NOT use 'datetime' as a file name
# because datetime is a built in module

x = datetime.datetime.now()
print(x)
print(x.year)
print(x.strftime('%A'))  # Weekday, full version

print("===============")

y = datetime.datetime(2020, 5, 17)
print(y)

print("===============")

z = datetime.datetime(2018, 6, 1)
print(z.strftime("%B"))
