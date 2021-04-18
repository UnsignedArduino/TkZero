from TkZero.Button import Button
from TkZero.Dialog import CustomDialog
from TkZero.Label import Label
from TkZero.MainWindow import MainWindow
from TkZero.Progressbar import Progressbar, OrientModes

# Make the root window and give it a title
root = MainWindow()
root.title = "Custom dialog dialogs"


# Pretend to grab more bytes from the downloading file
def grab_bytes(dlg: CustomDialog, bar: Progressbar):
    bar.value += 1
    if bar.value > 100:
        dlg.close()
        return
    bar.after(100, lambda: grab_bytes(dlg, bar))


# Pretend to cancel the download
def cancel(dlg: CustomDialog):
    print("Closing!")
    dlg.destroy()


# Define a function to pretend to download a file
def download_file():
    print("Downloading file")
    dlg = CustomDialog(root)
    Label(dlg, text="Pretending to download a file").grid(row=0, column=0)
    progressbar = Progressbar(dlg, length=200, orientation=OrientModes.Horizontal)
    progressbar.grid(row=1, column=0)
    grab_bytes(dlg, progressbar)
    dlg.on_close = lambda: cancel(dlg)
    dlg.grab_focus()
    dlg.wait_till_destroyed()


# Make a button that pretends to start downloading a file
download_btn = Button(root, text="Pretend to start downloading a file", command=download_file)
download_btn.grid(row=0, column=0)

# Start the mainloop like in Tkinter
root.mainloop()
