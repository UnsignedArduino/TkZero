from datetime import datetime

from PIL.ImageTk import PhotoImage

from TkZero.Label import Label
from TkZero.MainWindow import MainWindow

# Make the main window and give it a title
root = MainWindow()
root.title = "Simple Label Example"

# Make a simple label that shows an image
clock_img = Label(root, image=PhotoImage(file="clock.png"))
clock_img.grid(row=0, column=0)

# Make a label that shows the time
time_label = Label(root)
time_label.grid(row=0, column=1)


# Define a function to update the time
def update_time():
    time_label.text = str(datetime.now().strftime("%A, %B %d, %Y\n%H:%M:%S:%f"))
    root.after(100, update_time)


update_time()

# Start the mainloop like in Tkinter
root.mainloop()
