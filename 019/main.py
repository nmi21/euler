"""
You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""

import datetime
import pandas as pd

# determine start and end dates
start_date = datetime.date(year=1901, month=1, day=1)
end_date = datetime.date(year=2000, month=12, day=31)

sunday_starts = []
# create a range of these dates
for x in range(0, (end_date - start_date).days + 1):
    date = start_date + datetime.timedelta(x)
    day_of_month = date.strftime("%d")
    if day_of_month == "01" and date.weekday() == 6:
        sunday_starts.append(date)

ans = len(sunday_starts)
print(f"ans == {ans}")
