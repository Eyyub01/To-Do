from datetime import timedelta
from datetime import datetime
from datetime import time


now = datetime.now()

reminder_time = now - timedelta(hours=1)
print(reminder_time)


# now = datetime.now()
# current_time = now.strftime("%H:%M:%S")
# print("Current Time =", current_time)