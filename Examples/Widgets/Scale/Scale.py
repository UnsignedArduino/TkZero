from TkZero.Label import Label
from TkZero.MainWindow import MainWindow
from TkZero.Scale import Scale

# Make the main window and give it a title
root = MainWindow()
root.title = "Simple Scale Example"

# Make a label
value_label = Label(root)
value_label.grid(row=0, column=0)


# Update the label with the new "disk size"
def update_label(new_value: float = None):
    value_label.text = f"Select fake disk size: {round(value_scale.value / 1024 / 1024, 2)} MiB"


# Make a scale
value_scale = Scale(root, length=500, minimum=1.0, maximum=float(1024*1024*1024), command=update_label)
value_scale.grid(row=1, column=0)

# Update the label
update_label()

# Start the mainloop like in Tkinter
root.mainloop()
