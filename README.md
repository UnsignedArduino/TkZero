# TkZero
[![PyPI Version][pypi-image]][pypi-url]
[![Build Status][build-image]][build-url]
[![Code Coverage][coverage-image]][coverage-url]

## A _sane_ and _Pythonic_ wrapper around Tkinter.

Here's the [documentation](https://bobingstern.github.io/TkZero/)

## Installation
```pip install TkZero```

## Basic Usage
```python
#Entry Example
import tkinter as tk

from TkZero.Button import Button
from TkZero.Entry import Entry
from TkZero.Label import Label
from TkZero.MainWindow import MainWindow

# Make the main window and give it a title
root = MainWindow()
root.title = "Simple Entry Example"

# Create a label and grid it
Label(root, text="Username: ").grid(row=0, column=0, sticky=tk.NW)

# Create an entry and grid it
username = Entry(root, width=30)
username.grid(row=0, column=1, sticky=tk.NW)

# Create more labels and entries
Label(root, text="Password: ").grid(row=1, column=0, sticky=tk.NW)

password = Entry(root, width=30, show="*")
password.grid(row=1, column=1, sticky=tk.NW)

Label(root, text="Secret number: ").grid(row=2, column=0, sticky=tk.NW)


# Create a function that only allows numbers
def numbers_only(new_str: str) -> bool:
    return new_str.isdecimal()


secret_num = Entry(root, width=30, validate=numbers_only)
secret_num.grid(row=2, column=1, sticky=tk.NW)


# "Submit" the form
def submit():
    root.enabled = False
    print(username.value)
    print(password.value)
    print(secret_num.value)


# Create a button to "submit"
submit = Button(root, text="Submit", command=submit)
submit.grid(row=3, column=0, columnspan=2, sticky=tk.NSEW)

# Start the mainloop like in Tkinter
root.mainloop()

```


<!-- Badges -->

[pypi-image]: https://img.shields.io/pypi/v/TkZero
[pypi-url]: https://pypi.org/project/TkZero/
[build-image]: https://github.com/UnsignedArduino/TkZero/actions/workflows/build.yml/badge.svg
[build-url]: https://github.com/UnsignedArduino/TkZero/actions/workflows/build.yml
[coverage-image]: https://codecov.io/gh/UnsignedArduino/TkZero/branch/main/graph/badge.svg?token=ZUP6MD6INL
[coverage-url]: https://codecov.io/gh/UnsignedArduino/TkZero
[docs]: https://bobingstern.github.io/TkZero/
