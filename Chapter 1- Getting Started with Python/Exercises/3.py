

#Write a Python program to display the current date and time.
# 'datetime' is used to access working times and date
# (%Y-%m-%d %H:%M:%S) represents Year-Month-Day Hour:Minute:Second

import datetime
current_time = datetime.datetime.now()
formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
print("Current Date and Time:", formatted_time)

