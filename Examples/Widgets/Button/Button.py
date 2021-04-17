import tkinter as tk
from time import time

from PIL.ImageTk import PhotoImage

from TkZero.Button import Button, DisplayModes
from TkZero.MainWindow import MainWindow

# Make the main window and give it a title
root = MainWindow()
root.title = "Simple Button Example"

# Make a button and grid it onto the main window
btn1 = Button(parent=root, text="Button 1", command=lambda: print("Button 1 pressed!"))
btn1.grid(row=0, column=0)

# Make another button and grid it onto the main window
btn2 = Button(parent=root, text="Button 2", command=lambda: print("Button 2 pressed!"))
btn2.grid(row=0, column=1)
btn2.enabled = False


# Define a function to toggle the button states
def update_states():
    # You can set and get the state of a button via button.enabled
    # This toggles the button state
    btn1.enabled = not btn1.enabled
    btn2.enabled = not btn2.enabled


# Make another button and grid it onto the main window
toggle_btn = Button(parent=root, text="Toggle buttons", command=update_states)
toggle_btn.grid(row=0, column=2)

# Make a button with an image
save_btn = Button(parent=root, text="Save", image=PhotoImage(file="save_icon.png"), command=lambda: print("Saved!"))
save_btn.display_mode = DisplayModes.ImageTopText
save_btn.grid(row=1, column=0)

# Make a button that will print the time
# You can get the text via button.text
time_btn = Button(parent=root, command=lambda: print(time_btn.text))
time_btn.grid(row=1, column=1, columnspan=2, sticky=tk.NSEW)


# Define and schedule a function to run every 100 ms to update the text on the button
def update_time():
    # You can set the text on a button via button.text
    # The same applies to images - button.image but it is not used in this example
    time_btn.text = f"Time is\n{round(time(), 3)}"
    root.after(100, update_time)


update_time()

# Start the event loop like in Tkinter
root.mainloop()
