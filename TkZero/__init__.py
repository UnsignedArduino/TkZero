"""
TkZero - a sane and Pythonic wrapper around Tkinter.

Find this project on PyPI at https://pypi.org/project/TkZero/, or it's source
code at https://github.com/UnsignedArduino/TkZero.
"""
# TODO: Create into proper Python package -
#  https://antonz.org/python-packaging/#a-readme-and-changelog:~:text=A.%20Readme%20and%20changelog

__version_info__ = (0, 0, 1)
__version__ = ""
for index, digit in enumerate(__version_info__):
    __version__ += str(digit)
    if index < len(__version_info__) - 1:
        __version__ += "."
# "Prototype", "Development", or "Production"
__status__ = "Prototype"
__author__ = "UnsignedArduino at https://github.com/UnsignedArduino"
