import tkinter as tk


def create_entry(parent, row, column):
    return tk.Entry(parent, width=5, borderwidth=0.5, relief="solid").grid(row=row, column=column,  sticky="nsew")


# Create the main window
root = tk.Tk()
root.title("Tkinter Grid with Border")
root.config(bg="lightblue")


# Set the size of the window to cover most of the screen
screen_width, screen_height = root.winfo_screenwidth(), root.winfo_screenheight()
window_width, window_height = int(
    screen_width * 0.85), int(screen_height * 0.9)
root.geometry(
    f"{window_width}x{window_height}+{int((screen_width - window_width) / 2)}+{int((screen_height - window_height) / 2)}")
labelList = []
calenderDays = [27, 28, 29, 30, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
                16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 1, 2, 3, 4, 5, 6, 7, 8]

title = tk.Label(text="PLANNER",
                 background='#EEEEEE', font=('ariel', 12), width=17,  border=1, bg='lightblue')
title.grid(column=2, row=0, columnspan=3)
# create row and use modulus to create alternative label and text box rows
for rows in range(2, 14):

    if rows % 2 == 0:
        for cols in range(0, 7):
            foo = tk.Label(text="hello",
                           background='lightblue', font=('ariel', 12), width=19, height=0, border=1)
            foo.grid(column=cols, row=rows,
                     padx=5, pady=3)
            # send each instance of label to the list, where it can be accessed by list indexing
            labelList.append(foo)
    else:
        for cols in range(0, 7):
            foo = tk.Text(
                background='#EEEEEE', font=('ariel', 11), width=19, height=4, border=1,)
            foo.grid(column=cols, row=rows,
                     padx=5, pady=5)
            # labelList.append(foo)
for x in range(0, 42):
    labelList[x].config(text=calenderDays[x])

# Run the Tkinter event loop
root.mainloop()
print(len(labelList))
