# Grab the 'datetime' tool from the datetime toolbox
from datetime import datetime

print("=== LIVE CLOCK LOG ===")

# 1. Grab the exact current date and time right now
now = datetime.now()

# 2. Extract single components easily
current_year = now.year
current_month = now.month

print(f"Raw Timestamp : {now}")
print(f"Current Year  : {current_year}")
print(f"Current Month : {current_month}")

print("-" * 30)

# 3. Simple Formatting (Turning the time into a beautiful string)
# %A = Full weekday name, %B = Full month name, %d = Day of the month
friendly_date = now.strftime("%A, %B %d, %Y")

print(f"Formatted Date: {friendly_date}")
print("======================")