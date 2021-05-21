import tkinter as tk

from TkZero.Button import Button
from TkZero.MainWindow import MainWindow
from TkZero.Notebook import Notebook, Tab
from TkZero.Text import Text

# Make the main window and give it a title
root = MainWindow()
root.title = "Simple Notebook Example"

# Make the notebook
notebook = Notebook(root)
notebook.grid(row=0, column=0, columnspan=2)


# Define a function to add a tab on demand
def add_tab(nb, n) -> None:
    t = Tab(nb, title=f"Tab {n}")
    Text(t, width=50, height=15).grid(row=0, column=0)
    nb.tabs.append(t)
    nb.update_tabs()


# Define a function to remove a tab on demand
def remove_tab(nb, n) -> None:
    nb.tabs.pop(n)
    nb.update_tabs()


for _ in range(3):
    # Add some tabs to the notebook
    add_tab(notebook, len(notebook.tabs) + 1)

# Create buttons to add and remove tabs
Button(root, text="Add tab",
       command=lambda: add_tab(notebook, len(notebook.tabs) + 1)).grid(
    row=1, column=0, sticky=tk.NSEW
)
# Note this will cause an exception if a tab is removed but there are no tabs
Button(root, text="Remove tab",
       command=lambda: remove_tab(notebook, len(notebook.tabs) - 1)).grid(
    row=1, column=1, sticky=tk.NSEW
)


# Start the mainloop like in Tkinter
root.mainloop()
