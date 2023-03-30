from datetime import datetime
from datetime import date
from datetime import time

today = datetime.today()
print(today)

print(today.year)  # this will print year from datetime
print(today.ctime())  # this will print in human-readable format
print(today.month)
print(today.date())  # fetching only from datetime

current_date = today.date()
print(type(current_date))

last_year_date = date(2022,12,1)
print(last_year_date)
print(type(last_year_date))

diff_date = current_date - last_year_date # we can perform arthematic operations on two date , datetime , time
print(diff_date)

current_time = time(10,10,10)
print(current_time)

