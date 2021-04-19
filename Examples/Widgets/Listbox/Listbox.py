import tkinter as tk

from TkZero.Button import Button
from TkZero.Label import Label
from TkZero.Listbox import Listbox
from TkZero.MainWindow import MainWindow
from TkZero.Scrollbar import Scrollbar

# Make the main window and give it a title
root = MainWindow()
root.title = "Simple Listbox Example"

# Make a label to well, label the listbox up ahead
Label(root, text="Select a language: ").grid(row=0, column=0, sticky=tk.NW)

# Make a listbox
lang_listbox = Listbox(root, height=10, width=20)
lang_listbox.grid(row=1, column=0, sticky=tk.NW)
# Got a random list of 20 most popular languages but I don't know what year it came from lol
lang_listbox.values = [
    "Mandarin",
    "Spanish",
    "English",
    "Hindi[a]",
    "Arabic",
    "Portuguese",
    "Bengali",
    "Russian",
    "Japanese",
    "Punjabi",
    "German",
    "Javanese",
    "Wu (Shanghainese)",
    "Malay",
    "Telugu",
    "Vietnamese",
    "Korean",
    "French",
    "Marathi",
    "Tamil"
]
# Make the scrollbar for the listbox
Scrollbar(root, widget=lang_listbox).grid(row=1, column=1)


# Make a function to "submit" the response
def submit():
    root.enabled = False
    print(lang_listbox.selected)


# Make a "submit" button
Button(root, text="Submit", command=submit).grid(row=2, column=0, columnspan=2, sticky=tk.NSEW)


# Start the mainloop like in Tkinter
root.mainloop()
