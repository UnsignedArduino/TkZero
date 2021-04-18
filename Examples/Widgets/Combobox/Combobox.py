from TkZero.Combobox import Combobox
from TkZero.Label import Label
from TkZero.MainWindow import MainWindow

# Make the main window and give it a title
root = MainWindow()
root.title = "Simple Combobox Example"

# Make a label for the combobox
lang_label = Label(root, text="Language: ")
lang_label.grid(row=0, column=0)

# Make a combobox
lang_box = Combobox(root, values=("English", "Spanish", "French", "Chinese"))
lang_box.grid(row=0, column=1)

# Start the mainloop like in Tkinter
root.mainloop()
