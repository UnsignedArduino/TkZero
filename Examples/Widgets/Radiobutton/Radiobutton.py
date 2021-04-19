import tkinter as tk

from TkZero.Button import Button
from TkZero.Label import Label
from TkZero.MainWindow import MainWindow
from TkZero.Radiobutton import Radiobutton

# Make the main window and give it a title
root = MainWindow()
root.title = "Simple Radiobutton Example"

# Make a label
Label(root, text="Select a template:").grid(row=0, column=0, sticky=tk.NW)

# Make a variable
template_var = tk.StringVar(value="none")

# Make some radio buttons
Radiobutton(root, text="No template", variable=template_var, value="none").grid(row=1, column=0, sticky=tk.NW)
Radiobutton(root, text="Python Unittest", variable=template_var, value="unittest").grid(row=2, column=0, sticky=tk.NW)
Radiobutton(root, text="Python Stub", variable=template_var, value="stub").grid(row=3, column=0, sticky=tk.NW)


# "Make" the file
def make_file():
    print(template_var.get())


# Make a button to "create" the file
Button(root, text="Create Python file", command=make_file).grid(row=4, column=0, sticky=tk.NSEW)

# Start the mainloop like in Tkinter
root.mainloop()
