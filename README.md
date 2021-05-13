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

### Using PyPI (recommended)
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

#### Using Git
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

#### Downloading via zip
Go to the main page of this [repo](https://github.com/UnsignedArduino/TkZero),
click on the green `Code` button and click `Download ZIP`. Once the zip file 
finishes downloading, extract all of it to your project root. Then open a 
terminal and run:

1. `cd` into your project root.
2. `cd TkZero`
3. Install TkZero's dependencies with `pip install -r requirements.txt`. 
   (`pip3` on Linux and macOS - you may also need to use the user (`-U`) flag 
   if you are not using a virtual environment)

That's it!

## A simple example

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

See? Looks much better than Tkinter code ;)

## How you can help

Want to help! Great! Here are some ways you can help: (from easiest to hardest)

### Suggest an idea

Are you annoyed by something in Tkinter that hasn't been wrapped in TkZero? 
Please comment in this 
[discussion](https://github.com/UnsignedArduino/TkZero/discussions/4)! You can 
also open an issue for a feature request 
[here](https://github.com/UnsignedArduino/TkZero/issues/new?template=feature_request.md)
but don't forget to make sure that there isn't an issue for it open already!

### Report a bug

Found a bug? Great! Please report it 
[here](https://github.com/UnsignedArduino/TkZero/issues/new?template=bug_report.md)
but don't forget to make sure that there isn't an issue for it open already!

### Run unit tests and improve test coverage

As I develop on Windows, I'm unable to run my unit tests on macOS and Linux. If
you could run your unit tests and report any failures as a bug report, I would 
be ever grateful. Even better, you can improve the test coverage by adding on 
to the unit tests!

To get the coverage make sure you install `coverage` with 
`pip install coverage` (`pip3` for macOS and Linux and you may need to use the
user (`-U`) flag if you are not in a virtual environment) and then you can run 
these commands: (make sure you `git clone`d this repo and `cd` into it!)

```commandline
coverage erase
coverage run --include=TkZero/* -m pytest -ra
coverage report -m
```

### Adding examples

You can help by adding or improving (or simplifying!) examples, like for 
individual widgets
[here](https://github.com/UnsignedArduino/TkZero/tree/main/Examples/Widgets) or
"full applications" 
[here](https://github.com/UnsignedArduino/TkZero/tree/main/Examples/FullApps).


### Help fix bugs and full-fill feature requests with a pull request

Squashing bugs and implementing features can take time. If you are impatient 
like me, you can help to try to fix those bugs and full-fill feature requests! 
Please do not forget to run your code through `black`, `flake8`, `pylint`, and
`mypy`! You can also automate this by using `tox` at the repo root:

```commandline
tox -e py39
```

### Donate

If you want to give me your money (even just 1 dollar goes a long way) here is 
my Monero address :)

Don't worry, I'll let you mine to it as well ;) 
```text
43PuCHFFAc1EGCN5vjuerVNrxzc37r3fSV73EmimxsMw3Uxh6grNqAGUy97GwnH2g52HMsAj8LdRmbjGbJQHRs3WUpL9oGq
```
And my Bitcoin address:
```text
No Bitcoin address just yet! (Syncing the blockchain takes forever)
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
