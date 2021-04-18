import tkinter as tk

from TkZero.Button import Button
from TkZero.Combobox import Combobox
from TkZero.Label import Label
from TkZero.MainWindow import MainWindow

# Make the main window and give it a title
root = MainWindow()
root.title = "Simple Combobox Example"

# Make a label for the combobox
lang_label = Label(root, text="Select year: ")
lang_label.grid(row=0, column=0)

# Make a combobox
lang_box = Combobox(root)
lang_box.grid(row=0, column=1)
lang_box.values = tuple(range(2021, 1900, -1))


# "Submit" the year
def submit():
    # You can enable or disable the combobox with combobox.enabled
    lang_box.enabled = False
    submit_btn.enabled = False
    # You can get (and set) the value of the combobox with combobox.value
    print(lang_box.value)


# Make a button that "submits" the year
submit_btn = Button(root, text="Submit", command=submit)
submit_btn.grid(row=1, column=0, columnspan=2, sticky=tk.NSEW)

# Start the mainloop like in Tkinter
root.mainloop()
