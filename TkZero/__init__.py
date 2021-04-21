"""
TkZero - a sane and Pythonic wrapper around Tkinter.
"""
# TODO: Make examples of "full-featured" applications like:
#  [✔] File downloader
#  [ ] Photo viewer
#  [ ] Calculator
#  [ ] Notepad
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
