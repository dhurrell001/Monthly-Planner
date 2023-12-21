import tkinter as tk
from MonthCalenderV2 import SendCalendarDayToGUI


def create_entry(parent, row, column):
    return tk.Entry(parent, width=5, borderwidth=0.5, relief="solid").grid(row=row, column=column,  sticky="nsew")


# Create the main window
root = tk.Tk()
root.title("Tkinter Grid with Border")

# Set the size of the window to cover most of the screen
screen_width, screen_height = root.winfo_screenwidth(), root.winfo_screenheight()
window_width, window_height = int(screen_width * 0.9), int(screen_height * 0.9)
root.geometry(
    f"{window_width}x{window_height}+{int((screen_width - window_width) / 2)}+{int((screen_height - window_height) / 2)}")

# Create a frame to contain the grid
grid_frame = tk.Frame(root, borderwidth=1, relief="solid")
grid_frame.pack(fill=tk.BOTH, expand=True, padx=1, pady=1)
# Set the height of the second row to 50 pixels
# grid_frame.grid_rowconfigure(1, minsize=25)

# Create Headings in the first two rows
heading_labels = ['Heading 1', 'Heading 2', 'Heading 3',
                  'Heading 4', 'Heading 5', 'Heading 6', 'Heading 7']
for col, heading_text in enumerate(heading_labels):
    tk.Label(grid_frame, text=heading_text, width=5, borderwidth=1,
             relief="solid").grid(row=0, column=col,  sticky="nsew")

day_labels = ['Monday', 'Tuesday', 'Wednesday',
              'Thursday', 'Friday', 'Saturday', 'Sunday']
for col, subheading_text in enumerate(day_labels):
    tk.Label(grid_frame, text=subheading_text, width=20, height=1,  borderwidth=1,
             relief="solid").grid(row=1, column=col,  sticky="nsew")


# Create Entries and place them in the grid starting from the third row
# Start from the third row (index 2) and go up to the eleventh row (index 10)

for row in range(2, 8):
    for col in range(7):  # Seven columns
        create_entry(grid_frame, row, col)
grid_frame.grid_rowconfigure(0, minsize=100)  # First row
grid_frame.grid_rowconfigure(1, minsize=10)  # Second row

# Set the height of each row individually
# Set the height of each row individually
for i in range(8):
    tk.Label(grid_frame, height=1).grid(row=i, column=0, sticky="nsew")


# Set row and column weights so that they expand with the window
for i in range(8):
    grid_frame.grid_rowconfigure(i, weight=1)
for j in range(7):
    grid_frame.grid_columnconfigure(j, weight=1)

# Run the Tkinter event loop
root.mainloop()
