import tkinter as tk

from TkZero.Button import Button
from TkZero.Entry import Entry
from TkZero.MainWindow import MainWindow

# Create a main window
root = MainWindow()
root.title = "Calculator"

# Create the entry that holds the operations and result
entry = Entry(root, width=30)
entry.grid(row=0, column=0, columnspan=4, padx=1, pady=1)
entry.read_only = True


# Create a function to "add" numbers and operations
def add_entry(string: str) -> None:
    entry.read_only = False
    entry.value += string
    entry.read_only = True


# Create a function to delete a number of characters
def del_chars_entry(num: int) -> None:
    entry.read_only = False
    entry.value = entry.value[:-(abs(num))]
    entry.read_only = True


# Create a function to "run" the calculation
def calculate() -> None:
    entry.read_only = False
    try:
        entry.value = str(eval(entry.value))
    except SyntaxError:
        entry.value = "Syntax error"
    entry.read_only = True


# Create a list of list of buttons that do stuff
all_btns = [
    [
        {"(": lambda: add_entry("(")},
        {")": lambda: add_entry(")")},
        {"←": lambda: del_chars_entry(1)},
        {"/": lambda: add_entry("/")}
    ],
    [
        {"1": lambda: add_entry("1")},
        {"2": lambda: add_entry("2")},
        {"3": lambda: add_entry("3")},
        {"*": lambda: add_entry("*")}
    ],
    [
        {"4": lambda: add_entry("4")},
        {"5": lambda: add_entry("5")},
        {"6": lambda: add_entry("6")},
        {"-": lambda: add_entry("-")}
    ],
    [
        {"7": lambda: add_entry("7")},
        {"8": lambda: add_entry("8")},
        {"9": lambda: add_entry("9")},
        {"+": lambda: add_entry("+")}
    ],
    [
        {"C": lambda: del_chars_entry(len(entry.value))},
        {"0": lambda: add_entry("0")},
        {".": lambda: add_entry(".")},
        {"=": lambda: calculate()}
    ]
]

# For every "row"
for y, row in enumerate(all_btns):
    # For every "col" or item in the row
    for x, col in enumerate(row):
        # Make a button
        b = Button(parent=root, text=list(col.keys())[0], command=list(col.values())[0])
        # Set the width of the button to 20 px
        b.configure(width=6)
        b.grid(row=y+1, column=x)

# Start the mainloop
root.mainloop()
