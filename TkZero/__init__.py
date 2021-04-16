"""
TkZero - a sane and Pythonic wrapper around Tkinter.
"""
# TODO: Review all tests to make sure no copy/paste errors and fix them
# TODO: Review all doc strings to make sure no copy/paste errors and fix them
# TODO: Make examples for each widget
# TODO: Make examples of "full-featured" applications like:
#  - File downloader
#  - Photo viewer
#  - Calculator
#  - Notepad
#  And compare the TkZero code to Tkinter code
# TODO: Create into proper Python package - https://antonz.org/python-packaging/

__version_info__ = (0, 0, 1)
__version__ = ""
for index, digit in enumerate(__version_info__):
    __version__ += str(digit)
    if index < len(__version_info__) - 1:
        __version__ += "."
# "Prototype", "Development", or "Production"
__status__ = "Prototype"
__author__ = "UnsignedArduino at https://github.com/UnsignedArduino"
