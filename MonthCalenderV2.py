from datetime import datetime, timedelta
import numpy as np
from dateutil.relativedelta import relativedelta
import calendar

# Get the current date and time


class MonthPlannerDate:

    def __init__(self) -> None:
        # create a datetime objct for the date i want to be the current month. The previous and next month
        # will be realtive to this
        self.selectedMonth = datetime.now()
        # Get the number of days in the selected month
        self.days_in_selected_month = calendar.monthrange(
            self.selectedMonth.year, self.selectedMonth.month)[1]
        # get the first day of the selected month. This will be an integer to determine where the current month starts
        # in matrix i.e Tuedays will return a 1. this means that the current month will start at index 1 in matrix
        # if it was thursday it would return a 3 so it would start at index 3
        self.currentDayAsInteger = self.get_first_day_of_selected_month(
            self.selectedMonth)

    def ChangeMonth(self, newMonth):
        self.selectedMonth = newMonth
        self.days_in_selected_month = calendar.monthrange(
            self.selectedMonth.year, self.selectedMonth.month)[1]
        self.currentDayAsInteger = self.get_first_day_of_selected_month(
            self.selectedMonth)

    def get_first_day_of_selected_month(self, selected_date):
        # Get the first day of the selected month
        return datetime(selected_date.year, selected_date.month, 1).weekday()

    def CurrentMonth(self, selectedMonth=None):
        if selectedMonth == None:
            # Get the current date and time
            current_datetime = datetime.now()
        else:
            return self.get_first_day_of_selected_month(selectedMonth)
        # Get the first day of the current month
        first_day_of_current_month = datetime(
            current_datetime.year, current_datetime.month, 1)
        # Extract the day of the week as an integer (Monday is 0, Sunday is 6)

        first_day_of_month_integer = first_day_of_current_month.weekday()

        return first_day_of_month_integer

    def PreviousMonth(self, selected_date, AmountOfPreviouMonths):
        # Calculate the first day of 1 months ago. Takes selected_date datetime object and subracts a datetime object
        # fron N months ago, return a new datatime onject
        first_day_of_previous_months = selected_date - \
            relativedelta(months=AmountOfPreviouMonths, day=1)
        # Get the number of days in previous month.Monthrange returns a tuple (day of week month starts, amount of days in month)
        # returns second element of object [1]
        days_in_month = calendar.monthrange(
            first_day_of_previous_months.year, first_day_of_previous_months.month)[1]

        return days_in_month

    def FillMatrixCurrentMonth(self, dayOfMonthInteger, days_in_current_month, calenderDays):
        # Start to fill the calender from the first day of the month.
        # using day datetime integer as a start index 0-Monday 1- Tuesday etc
        # Get the number of days in the current month
        # set the first day as 1 in the calender display
        beginning_new_month_output = 1

        for thisMonth in range(dayOfMonthInteger, days_in_current_month + dayOfMonthInteger):
            calenderDays.append(beginning_new_month_output)
            beginning_new_month_output += 1

    def FillMatrixPreviousMonth(self, currentDayAsInteger, selected_date, AmountOfPreviouMonths, calenderDays):
        # fill the calender days before the current month start date with
        # last days of previous month.i.e (28 29 30) 1 2 3
        previousMonthNumberOfDays = self.PreviousMonth(
            selected_date, AmountOfPreviouMonths)
        last_month_day_start = previousMonthNumberOfDays - currentDayAsInteger + 1
    # Start to fill calender matrix with previous months days if thi month doe not start on a Monday
        for day in range(0, currentDayAsInteger):
            calenderDays.append(last_month_day_start)
            last_month_day_start += 1

    def FillMatrixNextMonth(self, dayOfMonthInteger, selected_date, calenderDays):
        # fill matrix after current month end date with first days
        # of the next month i.e 28 29 30 (1 2 3)
        beginning_next_month_output = 1
        days_in_current_month = calendar.monthrange(
            selected_date.year, selected_date.month)[1]
        # fill any remaining slot in matrix with next months day starting at one.
        for day in range(days_in_current_month+dayOfMonthInteger, 42):
            # calendrDisplay[nextMonth] = beginning_next_month_output
            calenderDays.append(beginning_next_month_output)
            beginning_next_month_output += 1

    def SendCalendarDayToGUI(self):
        calenderDays = []

        self.FillMatrixPreviousMonth(
            self.currentDayAsInteger, self.selectedMonth, 1, calenderDays)

        self.FillMatrixCurrentMonth(
            self.currentDayAsInteger, self.days_in_selected_month, calenderDays)
        # FillMatrixCurrentMonth(
        #     calenderDisplay, currentDayAsInteger, days_in_selected_month,calenderDays)

        self.FillMatrixNextMonth(self.currentDayAsInteger,
                                 self.selectedMonth, calenderDays)
        return calenderDays

    def SendSelectedDateToGUI(self):
        return self.selectedMonth


# create a datetime objct for the date i want to be the current month. The previous and next month
# will be realtive to this
# selectedMonth = datetime(2024, 1, 1)
# # Get the number of days in the selected month
# days_in_selected_month = calendar.monthrange(
#     selectedMonth.year, selectedMonth.month)[1]
# # get the first day of the selected month. This will be an integer to determine where the current month starts
# # in matrix 1.e Tuedays will return a 1. this means that the current month will start at index 1 in matrix
# # if it was thursday it would return a 3 so it would start at index 3
# currentDayAsInteger = get_first_day_of_selected_month(selectedMonth)

# calenderDays = []

# FillMatrixPreviousMonth(
#     calenderDisplay, currentDayAsInteger, selectedMonth, 1, calenderDays)

# FillMatrixCurrentMonth(
#     calenderDisplay, currentDayAsInteger, days_in_selected_month, calenderDays)
# # FillMatrixCurrentMonth(
# #     calenderDisplay, currentDayAsInteger, days_in_selected_month,calenderDays)

# FillMatrixNextMonth(calenderDisplay, currentDayAsInteger,
#                     selectedMonth, calenderDays)

# # FillMatrixPreviousMonth(calenderDisplay, currentDayAsInteger, selectedMonth, 1,calenderDays)

# days_matrix = np.array(calenderDisplay).reshape(6, 7)
# print(f"Day : {current_datetime.day} Month : {current_datetime.month} Year : {current_datetime.year}\n")
# print(days_matrix)
# print(calenderDays)
