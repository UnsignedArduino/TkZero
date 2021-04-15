"""
Creates a themed scale. (Slider)
"""
import tkinter as tk
from tkinter import ttk
from pathlib import Path
from PIL.ImageTk import PhotoImage
from typing import Union, Any, Callable


class OrientModes:
    """
    The orient modes for scales.
    Horizontal - makes the scale horizontal and slides left and right.
    Vertical - makes the scale vertical and slides up and down.
    """
    Horizontal = tk.HORIZONTAL
    Vertical = tk.VERTICAL


class Scale(ttk.Scale):
    def __init__(self, parent: Union[tk.Widget, Union[tk.Tk, tk.Toplevel]], length: int, minimum: float, maximum: float,
                 orientation: str = OrientModes.Vertical, command: Callable = None):
        """
        Initiate a ttk.Scrollbar.

        :param parent: The parent of the scrollbar.
        :param length: An int, which is the length of the scale.
        :param minimum: The minimum value of the scale, a float.
        :param maximum: The maximum value of the scale, a float.
        :param orientation: The orientation of the scrollbar and what direction it should scroll the widget in. Defaults
         to OrientModes.Vertical and is a str.
        :param command: The command to call when the scale changes. Will be passed in a positional float as the new
         value.
        """
        super().__init__(master=parent, orient=orientation, length=length, from_=minimum, to=maximum,
                         command=lambda new_val: command(float(new_val)) if command is not None else None)
        self._style_root = "TScale"
        self._enabled = True
        self._orientation = orientation

    @property
    def value(self) -> float:
        """
        Get the value on this scale.

        :return: A float.
        """
        return self.get()

    @value.setter
    def value(self, new_value: Union[int, float]) -> None:
        """
        Set the value on this scale.

        :param new_value: A float or an int.
        :return: None.
        """
        if not isinstance(new_value, float) and not isinstance(new_value, int):
            raise TypeError(f"new_value is not a float or an int! (type passed in: {repr(type(new_value))})")
        self.set(float(new_value))

    @property
    def enabled(self) -> bool:
        """
        Whether this widget is in normal mode or disabled mode (grayed out and cannot interact with) in Tk terms.

        :return: A bool, True if normal otherwise False.
        """
        return self._enabled

    @enabled.setter
    def enabled(self, new_state: bool) -> None:
        """
        Set whether this widget is in normal mode or disabled mode (grayed out and cannot interact with) in Tk terms.

        :param new_state: The new state (a bool) True for enabled and False for disabled.
        :return: None.
        """
        if not isinstance(new_state, bool):
            raise TypeError(f"new_state is not a bool! (type passed in: {repr(type(new_state))})")
        self._enabled = new_state
        self.state(["!disabled" if self._enabled else "disabled"])
