# TkZero
[![PyPI Version][pypi-image]][pypi-url]
[![Build Status][build-image]][build-url]
[![Code Coverage][coverage-image]][coverage-url]
[![License][license-image]][license-url]

A lightweight and Pythonic wrapper around Tkinter.

[Documentation](https://unsignedarduino.github.io/TkZero/) is available on 
GitHub pages. You can find the raw HTML for the docs in the 
[`docs/`](https://github.com/UnsignedArduino/TkZero/tree/main/docs) directory.
[`pdoc`](https://pdoc3.github.io/pdoc/) is used to generate the documentation.

You can find examples in the 
[`Examples/`](https://github.com/UnsignedArduino/TkZero/tree/main/Examples) 
directory and tests in the 
[`Tests/`](https://github.com/UnsignedArduino/TkZero/tree/main/Tests) directory.

## Installation

### Using PyPI
Windows:
```commandline
pip install TkZero
```
macOS and Linux:
```shell
pip3 install TkZero
```
You may need to use the user (`-U`) flag to install if you are not using a 
virtual environment!

### From source
Make sure you have [Git](https://git-scm.com/) before following these steps. 
If you are on Windows, I highly suggest you install the 
[Windows Terminal](https://www.microsoft.com/en-us/p/windows-terminal/9n0dx20hk701)
as it's much better than the command prompt.

1. `cd` into your project root.
2. Run `git clone https://github.com/UnsignedArduino/TkZero`
3. Run `cd TkZero`
4. Install TkZero's dependencies with `pip install -r requirements.txt`. 
   (`pip3` on Linux and macOS - you may also need to use the user (`-U`) flag 
   if you are not using a virtual environment)

That's it!

## Basic Usage

```python
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


# "Submit" the form
def submit():
    root.enabled = False
    print(username.value)
    print(password.value)


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
[license-image]: https://badgen.net/github/license/UnsignedArduino/TkZero
[license-url]: https://github.com/UnsignedArduino/TkZero/blob/main/LICENSE
