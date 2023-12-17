from datetime import datetime, timedelta
import numpy as np
from dateutil.relativedelta import relativedelta
import calendar

# Get the current date and time
current_datetime = datetime.now()
current_day_words = current_datetime.strftime("%A")
# Format the current month as a string
current_month = current_datetime.strftime("%B")
print(current_day_words)
print(current_month)


# Extract the day of the week as an integer (Monday is 0, Sunday is 6)

first_day_of_month_integer = 4  # first_day_of_current_month.weekday()+1

# Calculate the first day of 1 months ago
first_day_of_1_months_ago = current_datetime - relativedelta(months=1, day=1)
print(first_day_of_1_months_ago)


# Get the number of days in previous month
days_in_month = calendar.monthrange(
    first_day_of_1_months_ago.year, first_day_of_1_months_ago.month)[1]
print(days_in_month)

# Print the result
# print("First day of the current month as an integer:", first_day_of_month_integer)

# set a list for 42 days ( 7 days time 6 weeks)
days = [0 for x in range(0, 42)]


# current months number of days
current_month_days = 30
last_month_number_of_days = days_in_month
#
lastMonth = 35-current_month_days

beginning_next_month_output = 1
beginning_new_month_output = 1

last_month_day_start = last_month_number_of_days - first_day_of_month_integer + 1
# Start to fill calender matrix with previous months days if thi month doe not start on a Monday
for day in range(0, first_day_of_month_integer):

    days[day] = last_month_day_start
    last_month_day_start += 1
# fill in the current month days using current datetime day integer as a start point. Fill matrix out for the amount of day
# un thi month
for thisMonth in range(first_day_of_month_integer, current_month_days + first_day_of_month_integer):

    days[thisMonth] = beginning_new_month_output
    beginning_new_month_output += 1
# fill any remaining slot in matrix with next months day starting at one.
for nextMonth in range(current_month_days+first_day_of_month_integer, 42):
    days[nextMonth] = beginning_next_month_output
    beginning_next_month_output += 1

# Convert the list to a NumPy array
days_matrix = np.array(days).reshape(6, 7)
print(days_matrix)
