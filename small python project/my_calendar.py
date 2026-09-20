import calendar
from datetime import datetime

year = int(input("ENTER YEAR : "))
month_input = input("ENTER MONTH : ").strip()

# Check if the user entered digits or a month name
if month_input.isdigit():
    month = int(month_input)
else:
    # Converts names like "May", "january", "FEB" to numbers (1-12)
    month = datetime.strptime(month_input[:3].title(), "%b").month

print("\n", calendar.month(year, month))