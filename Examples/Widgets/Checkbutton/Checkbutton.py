from PIL.ImageTk import PhotoImage

from TkZero.Checkbutton import Checkbutton, DisplayModes
from TkZero.Button import Button
from TkZero.MainWindow import MainWindow
import tkinter as tk

# Make the main window and give it a title
root = MainWindow()
root.title = "Simple Checkbutton Example"


# Make a check button
disc_chkbtn = Checkbutton(root, "Enable logs from disc-related activity")
disc_chkbtn.grid(row=0, column=0, columnspan=2, sticky=tk.NW)

# Make another check button
net_chkbtn = Checkbutton(root, "Enable logs from network-related activity")
net_chkbtn.grid(row=1, column=0, columnspan=2, sticky=tk.NW)

# Make another check button
cpu_chkbtn = Checkbutton(root, "Enable logs from CPU-related activity")
cpu_chkbtn.grid(row=2, column=0, columnspan=2, sticky=tk.NW)


def enable_all_chkbtns(state: bool = False):
    # Pretend we can't set the state of them because quiet mode is on
    if quiet_chkbtn.value:
        return
    # You can set (and get) the state of the check buttons via checkbutton.value
    disc_chkbtn.value = state
    net_chkbtn.value = state
    cpu_chkbtn.value = state


# Make some buttons
en_all_btn = Button(root, text="Enable all", command=lambda: enable_all_chkbtns(True))
en_all_btn.grid(row=3, column=0)
dis_all_btn = Button(root, text="Disable all", command=lambda: enable_all_chkbtns(False))
dis_all_btn.grid(row=3, column=1)


def quiet_mode():
    disc_chkbtn.value = False
    net_chkbtn.value = False
    cpu_chkbtn.value = False
    # You can enable and disable check buttons via checkbutton.enabled (like all other widgets)
    disc_chkbtn.enabled = not quiet_chkbtn.value
    net_chkbtn.enabled = not quiet_chkbtn.value
    cpu_chkbtn.enabled = not quiet_chkbtn.value


# Make another check button
# The command function gets called every time the check button is clicked
quiet_chkbtn = Checkbutton(root, text="Quiet mode", image=PhotoImage(file="night.png"), command=quiet_mode)
quiet_chkbtn.grid(row=4, column=0, columnspan=2)
quiet_chkbtn.display_mode = DisplayModes.ImageLeftText


# Start the event loop like in Tkinter
root.mainloop()
