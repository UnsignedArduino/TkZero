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
    The orient modes for progress bars.
    Horizontal - makes the progress bar horizontal.
    Vertical - makes the progress bar vertical.
    """
    Horizontal = tk.HORIZONTAL
    Vertical = tk.VERTICAL


class ProgressModes:
    """
    The progress bar modes for, well, progress bars.
    Determinate - you know how much would be completed, etc.
    Indeterminate - you don't know, the progress bar will just be loading forever until stopped.
    """
    Determinate = "determinate"
    Indeterminate = "indeterminate"


class Progressbar(ttk.Progressbar):
    def __init__(self, parent: Union[tk.Widget, Union[tk.Tk, tk.Toplevel]], length: int,
                 mode: str = ProgressModes.Determinate, orientation: str = OrientModes.Vertical):
        """
        Initiate a ttk.Scrollbar.

        :param parent: The parent of the scrollbar.
        :param length: An int, which is the length of the scale.
        :param mode: The mode the progress bar should operate in. Defaults to ProgressModes.Determinate
        :param orientation: The orientation of the scrollbar and what direction it should scroll the widget in. Defaults
         to OrientModes.Vertical and is a str.
         value.
        """
        super().__init__(master=parent, orient=orientation, length=length, mode=mode)
        self._style_root = "TProgressbar"
        self._enabled = True
        self._orientation = orientation
        self._mode = mode

    @property
    def value(self) -> float:
        """
        Get the value on this progress bar.

        :return: A float.
        """
        if self._mode != ProgressModes.Determinate:
            raise AttributeError("Can not access value while using indeterminate mode!")
        return self["value"]

    @value.setter
    def value(self, new_value: Union[int, float]) -> None:
        """
        Set the value on this progress bar.

        :param new_value: A float or an int.
        :return: None.
        """
        if not isinstance(new_value, float) and not isinstance(new_value, int):
            raise TypeError(f"new_value is not a float or an int! (type passed in: {repr(type(new_value))})")
        if self._mode != ProgressModes.Determinate:
            raise AttributeError("Can not access value while using indeterminate mode!")
        self["value"] = float(new_value)

    @property
    def maximum(self) -> float:
        """
        Get the maximum on this progress bar.

        :return: A float.
        """
        if self._mode != ProgressModes.Determinate:
            raise AttributeError("Can not access value while using indeterminate mode!")
        return self["maximum"]

    @maximum.setter
    def maximum(self, new_value: Union[int, float]) -> None:
        """
        Set the maximum on this progress bar.

        :param new_value: A float or an int.
        :return: None.
        """
        if not isinstance(new_value, float) and not isinstance(new_value, int):
            raise TypeError(f"new_value is not a float or an int! (type passed in: {repr(type(new_value))})")
        if self._mode != ProgressModes.Determinate:
            raise AttributeError("Can not access value while using indeterminate mode!")
        self["maximum"] = float(new_value)

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
