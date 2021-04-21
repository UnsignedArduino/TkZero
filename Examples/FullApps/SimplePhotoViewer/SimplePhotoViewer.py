import tkinter as tk

from PIL import UnidentifiedImageError
from PIL.ImageTk import PhotoImage

from TkZero.Button import Button
from TkZero.Dialog import open_file, show_error
from TkZero.Label import Label
from TkZero.MainWindow import MainWindow

# Create a main window
root = MainWindow()
root.title = "Simple Photo Viewer"

# Create a label to hold the image (when no image open it will hold text saying no image open)
image_label = Label(root, text="No image open!")
image_label.grid(row=0, column=0)


# Create a function to open an image
def open_image():
    path = open_file(title="Select an image")
    if path:
        try:
            image_label.image = PhotoImage(file=path)
        except UnidentifiedImageError:
            show_error(root, title="Simple Photo Viewer: Error!",
                       message="Could not open that file - format not recognized!", detail=f"Unidentified file: {path}")


# Create a button to open a new image
open_btn = Button(root, text="Open image", command=open_image)
open_btn.grid(row=1, column=0, sticky=tk.NSEW)

# Start the mainloop
root.mainloop()
