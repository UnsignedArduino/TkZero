from TkZero.Button import Button
from TkZero.Text import Text
from TkZero.Scrollbar import Scrollbar, OrientModes
from TkZero.MainWindow import MainWindow

# Make the main window and give it a title
root = MainWindow()
root.title = "Simple Text Example"

# Make a big text box
text_box = Text(root, width=50, height=15)
text_box.grid(row=0, column=0, columnspan=2)
# Make a scrollbar and attach it to the text box
Scrollbar(root, widget=text_box).grid(row=0, column=2)

# Make a button to print the contents
# Note that Tkinter adds an extra newline and the fact that print puts a newline after the printed text too
print_btn = Button(root, text="Print contents", command=lambda: print(text_box.text))
print_btn.grid(row=2, column=0)


# Make a function to clear the contents
def clear():
    text_box.text = ""


# Make a button to clear the contents
clear_btn = Button(root, text="Clear contents", command=clear)
clear_btn.grid(row=2, column=1)

# Start the mainloop like in Tkinter
root.mainloop()
