# This is an extremely simple Notepad that has one menu - a file menu
# There are many things you can improve upon, such as an edit menu, (like copy/cut/paste/delete/select all) undo/redo,
# an option to control word wrapping, a status bar, and more. Check out https://tkdocs.com/tutorial/text.html for a
# detailed explanation on the text widget.

from TkZero import Dialog
from TkZero.MainWindow import MainWindow
from TkZero.Menu import Menu, MenuCascade, MenuCommand, MenuSeparator
from TkZero.Scrollbar import Scrollbar, OrientModes
from TkZero.Text import Text

# Create a main window
root = MainWindow()
root.title = "Untitled - Notepad"
# Disables resizing on the X and Y axis
root.resizable(False, False)

# Whether or not we modified the currently open document
modified = False
# Whether or not the user has saved this file
saved_doc = False
# Where to save the currently opened document. None if this document has never been saved.
save_location = None

# Create the main menus
menu_bar = Menu(root, is_menubar=True)


# Create a function to open a new document
def file_new() -> None:
    # Yes, global variables aren't pretty but for the sake of simplicity we will not use a class
    global modified, saved_doc, save_location
    if modified:
        result = Dialog.ask_yes_or_no_or_cancel(root, title="Notepad: Confirm",
                                                message="You have unsaved changes - discard them?")
        if result is None:
            return
        elif not result:
            file_save()
        elif result:
            pass
    text_area.text = ""
    root.title = "Untitled - Notepad"
    modified = False
    saved_doc = False
    save_location = None


# Create a function to open a new document
def file_open() -> None:
    # Yes, global variables aren't pretty but for the sake of simplicity we will not use a class
    global modified, saved_doc, save_location
    path = Dialog.open_file(title="Please select a text file")
    if path is None:
        return
    if modified:
        result = Dialog.ask_yes_or_no_or_cancel(root, title="Notepad: Confirm",
                                                message="You have unsaved changes - discard them?")
        if result is None:
            return
        elif not result:
            file_save()
        elif result:
            pass
    modified = False
    saved_doc = True
    save_location = path
    root.title = f"{path.name} - Notepad"
    text_area.text = path.read_text()


# Create a function to save the currently opened document
def file_save() -> None:
    # Yes, global variables aren't pretty but for the sake of simplicity we will not use a class
    global modified, saved_doc, save_location
    if save_location is None:
        path = Dialog.save_file(title="Please select a location to save")
        if path is None:
            return
        save_location = path
    save_location.write_text(text_area.text)
    modified = False
    saved_doc = True
    root.title = f"{save_location.name} - Notepad"


# Create a function to close the notepad
def file_close() -> None:
    # Yes, global variables aren't pretty but for the sake of simplicity we will not use a class
    global modified, saved_doc, save_location
    if modified:
        result = Dialog.ask_yes_or_no_or_cancel(root, title="Notepad: Confirm",
                                                message="You have unsaved changes - discard them?")
        if result is None:
            return
        elif not result:
            file_save()
        elif result:
            pass
    root.destroy()


# Create a function to update the modified states
def text_update() -> None:
    # Yes, global variables aren't pretty but for the sake of simplicity we will not use a class
    global modified, saved_doc, save_location
    modified = True
    title = root.title[:-10]
    if not title[-1] == "*":
        title += "*"
    root.title = title + " - Notepad"


# Create the actual menu contents
menu_bar.items = [
    MenuCascade(label="File", items=[
        MenuCommand(label="New", command=file_new, underline=0),
        MenuCommand(label="Open...", command=file_open, underline=0),
        MenuCommand(label="Save", command=file_save, underline=0),
        MenuSeparator(),
        MenuCommand(label="Exit", command=file_close, underline=0)
    ], underline=0)
]

# Create the main text area
text_area = Text(root, width=64, height=16)
text_area.grid(row=0, column=0, padx=1, pady=1)

# Bind to the modified event
text_area.bind("<<TextModified>>", lambda _: text_update())

# Create some scrollbars for the text area
y_scrollbar = Scrollbar(root, orientation=OrientModes.Vertical, widget=text_area)
y_scrollbar.grid(row=0, column=1, padx=1, pady=1)

x_scrollbar = Scrollbar(root, orientation=OrientModes.Horizontal, widget=text_area)
x_scrollbar.grid(row=1, column=0, padx=1, pady=1)

# Start the mainloop
root.mainloop()
