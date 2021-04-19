import tkinter as tk
from random import randint

from TkZero.Button import Button
from TkZero.Label import Label
from TkZero.MainWindow import MainWindow
from TkZero.Progressbar import Progressbar

# Make the main window and give it a title
root = MainWindow()
root.title = "Simple Progressbar Example"


# "Start" the download
def start_download():
    start_btn.enabled = False
    get_bytes()


# "Download" and update the progress bar
def get_bytes():
    bar.value += randint(1024*1024, 1024*1024*8)
    if bar.value < bar.maximum:
        root.after(100, get_bytes)
    else:
        # Just so that we don't go over the limit. In a real situation, you wouldn't need to do this.
        bar.value = bar.maximum
    label.text = f"{round(bar.value / 1024 / 1024, 2)}/{round(bar.maximum / 1024 / 1024, 2)} MiB downloaded"


# Create a button to "start" the download
start_btn = Button(root, text="Start download", command=start_download)
start_btn.grid(row=0, column=0)

# Create a progress bar to represent the "download"
bar = Progressbar(root, length=200)
bar.grid(row=1, column=0)
bar.maximum = randint(1024*1024*128, 1024*1024*1024)

# Create a label to show the exact byte counts
label = Label(root)
label.grid(row=2, column=0, sticky=tk.NW)
label.text = f"File is {round(bar.maximum / 1024 / 1024, 2)} MiB"

# Start the mainloop like in Tkinter
root.mainloop()
