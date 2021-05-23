from TkZero.Button import Button
from TkZero.Frame import ScrollableFrame
from TkZero.MainWindow import MainWindow

# Create the main window and set a title
root = MainWindow()
root.title = "Scrollable Frame Example"

# Create a scrollable frame
scrollable_frame = ScrollableFrame(root, x_scrolling=True, y_scrolling=True)
scrollable_frame.grid(row=0, column=0)

# Create a bunch of buttons in the scrollable frame
for x in range(10):
    for y in range(20):
        # Note the usage of the frame attribute of the scrollable frame instead
        # of using it directly.
        b = Button(scrollable_frame.frame, text=f"{x}, {y}")
        b.grid(row=y, column=x)

# Start the mainloop like in Tkinter
root.mainloop()
