import tkinter as tk
from MonthCalenderV2 import SendCalendarDayToGUI, SendSelectedDateToGUI


def OnPreviousMonthButtonClick():
    pass


# Program variables

# stores the current datetime object that is in use
selectedMonth = SendSelectedDateToGUI()
# list of previous, current and next month days
calenderDays = SendCalendarDayToGUI()
# Create the main window
root = tk.Tk()
root.title("Monthly Planner")
root.config(bg="lightblue")

# Set the size of the window to cover most of the screen
screen_width, screen_height = root.winfo_screenwidth(), root.winfo_screenheight()
window_width, window_height = int(
    screen_width * 0.96), int(screen_height * 0.96)
# set the screen location centrally
root.geometry(
    f"{window_width}x{window_height}+{int((screen_width - window_width) / 2)}+{int((screen_height - window_height) / 2)}")

######################  Screen layout ################################

day_labels = ['Monday', 'Tuesday', 'Wednesday',
              'Thursday', 'Friday', 'Saturday', 'Sunday']

title = tk.Label(text="PLANNER",
                 background='#EEEEEE', font=('ariel', 12), width=17, pady=5, bg='lightblue')
title.grid(column=2, row=0, columnspan=3)
monthSelecterLabel = tk.Label(text=selectedMonth.strftime("%B"), width=17)
prevMonthButton = tk.Button(text="<<<", width=17, bg="lightyellow",
                            )
nextMonthButton = tk.Button(text=">>>", width=17, bg="lightyellow")

monthSelecterLabel.grid(column=5, row=1)
prevMonthButton.grid(column=4, row=1)
nextMonthButton.grid(column=6, row=1)
for num in range(7):
    dayLabel = tk.Label(text=day_labels[num],
                        background='#EEEEEE', font=('ariel', 12), width=17,  border=1, bg='lightblue')
    dayLabel.grid(column=num, row=2)

# create row and use modulus to create alternative label and text box rows
labelList = []  # stores list of label objects
for rows in range(4, 16):

    if rows % 2 == 0:
        for cols in range(0, 7):
            foo = tk.Label(text="hello",
                           background='lightblue', font=('ariel', 12), width=23, height=0, border=1)
            foo.grid(column=cols, row=rows,
                     padx=1, pady=3)
            # send each instance of label to the list, where it can be accessed by list indexing
            labelList.append(foo)
    else:
        for cols in range(0, 7):
            foo = tk.Text(
                background='#EEEEEE', font=('ariel', 11), width=19, height=3.8, border=0.5, relief=tk.RAISED, bd=2)
            foo.grid(column=cols, row=rows,
                     padx=1, pady=5)
            # labelList.append(foo)


def FillCalender():
    for x in range(0, 42):
        labelList[x].config(text=calenderDays[x])


FillCalender()
# Run the Tkinter event loop
root.mainloop()
print(len(labelList))
