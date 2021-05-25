"""
TkZero - a lightweight and Pythonic wrapper around Tkinter.

PyPI: https://pypi.org/project/TkZero/

GitHub: https://github.com/UnsignedArduino/TkZero

Documentation: https://unsignedarduino.github.io/TkZero/

Examples: https://github.com/UnsignedArduino/TkZero/tree/main/Examples

Tests: https://github.com/UnsignedArduino/TkZero/tree/main/Tests

You can find more information on the GitHub README.
"""

__version_info__ = (0, 1, 1)
__version__ = ""
for index, digit in enumerate(__version_info__):
    __version__ += str(digit)
    if index < len(__version_info__) - 1:
        __version__ += "."
# "Prototype", "Development", or "Production"
__status__ = "Development"
__author__ = "UnsignedArduino at https://github.com/UnsignedArduino"
