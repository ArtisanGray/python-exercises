## import time or datetime
from datetime import datetime as dt
from datetime import timedelta
import replit
import time
print("_" * 30)
print("Welcome to Countdown Clock!")
print("Here, you can enter a date and get a countdown until that date.")
print("_" * 30)
year_int = int(input("Enter year: "))
month_int = int(input("Enter the value of the month you want to countdown to. (1 - 12): "))
day_int = int(input("Enter the day you want to countdown to. (1-31): "))
hour_int = int(input("Enter the hour: "))
#There are a few things that need to be added in order to prevent negatives, but overall the premise works.
while True:
  now = dt.now() - timedelta(hours = 6)
  if day_int > now.day:
    print(str(year_int - now.year)+ " years\n" +
    str(12 + (month_int - now.month)) + " months\n" +
    str(day_int - now.day) + " days\n" + 
    str(hour_int - now.hour) + " hours\n" +
    str(59 - now.minute) + " minutes\n" +
    str(59 - now.second) + " seconds\n")
    print(now)
  else:
    print(str(year_int - now.year)+ " years\n" +
    str(12 + (month_int - now.month)) + " months\n" +
    str(30 -(abs(day_int - now.day))) + " days\n" + 
    str(hour_int - now.hour) + " hours\n" +
    str(59 - now.minute) + " minutes\n" +
    str(59 - now.second) + " seconds\n")
    print(now)
  replit.clear()
  time.sleep(1)

#get local time
#end time(christmas)
