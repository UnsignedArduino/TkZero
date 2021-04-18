from TkZero import Dialog
from TkZero.Button import Button
from TkZero.MainWindow import MainWindow

# Make the root window and give it a title
root = MainWindow()
root.title = "Built-in dialogs"

# Make a list of a list of dictionaries to represent the buttons and there actions
btns = [
    [
        # Open a file. Returns a pathlib.Path of the select path or None if canceled
        {"Open file": lambda: print(Dialog.open_file(title="Select a file",
                                                     file_types=(("All files", "*.*"), )))},
        # Save a file. Returns a pathlib.Path of the select path or None if canceled
        {"Save file": lambda: print(Dialog.save_file(title="Select a location to save this file"))},
        # Select a directory. Returns a pathlib.Path of the select path or None if canceled
        {"Select directory": lambda: print(Dialog.select_directory(title="Select a directory"))}
    ],
    [
        # Choose a color! Returns a hex value as the string ("ff0000" for red) or a tuple of floats representing the
        # color. ((255.0, 0.0, 0.0) for red)
        {"Choose a color": lambda: print(Dialog.choose_color(as_rgb=False))}
    ],
    [
        # Show some info, warning, and error dialogs
        {"Show info": lambda: print(Dialog.show_info(root, "Some information",
                                                     "Here is some information", "Here are some details"))},
        {"Show warning": lambda: print(Dialog.show_warning(root, "Some warning",
                                                           "Here is a warning", "Here are some details"))},
        {"Show error": lambda: print(Dialog.show_error(root, "Some error",
                                                       "Here is an error", "Here are some details"))}
    ],
    [
        # Ask the user a question with the "Ok" or "Cancel" buttons
        {"Ask Ok/Cancel": lambda: print(Dialog.ask_ok_or_cancel(root, "Asking Ok/Cancel",
                                                                "Ok or cancel?", "(Also here are some details)"))},
        # Ask the user a question with the "Yes" or "No" buttons
        {"Ask Yes/No": lambda: print(Dialog.ask_yes_or_no(root, "Asking Yes/No",
                                                          "Yes or no?", "(Here are some details for you)"))},
        # Ask the user a question with the "Yes," "No," or "Cancel" buttons
        {"Ask Yes/No/Cancel": lambda: print(Dialog.ask_yes_or_no_or_cancel(root, "Ask Yes/No/Cancel",
                                                                           "Yes, no, or cancel?",
                                                                           "(Some details for you)"))},
        # Ask the user a question with the "Retry" or "Cancel" buttons
        {"Ask Retry/Cancel": lambda: print(Dialog.ask_retry_cancel(root, "Ask Retry/Cancel",
                                                                   "Retry or cancel?", "(Some details for you here)"))}
    ]
]

# For every "row"
for y, row in enumerate(btns):
    # For every "col" or item in the row
    for x, col in enumerate(row):
        # Make a button
        b = Button(parent=root, text=list(col.keys())[0], command=list(col.values())[0])
        # Set the width of the button to 20 px
        b.configure(width=20)
        b.grid(row=y, column=x)

# Start the main loop like in Tkinter
root.mainloop()
