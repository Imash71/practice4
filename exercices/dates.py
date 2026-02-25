
from datetime import datetime, timedelta

now = datetime.now()

print("Current date:", now)

some_date = datetime(2020, 1, 1)

print("Specific date:", some_date)

formatted = now.strftime("%d-%m-%Y %H:%M")

print("Formatted date:", formatted)

difference = now - some_date

print("Days difference:", difference.days)

future = now + timedelta(days=10)

print("After 10 days:", future)

