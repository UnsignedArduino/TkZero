"""
Creates a themed separator.
"""

import tkinter as tk
from tkinter import ttk
from typing import Union


class OrientModes:
    """
    The orient modes for separators
    Horizontal - makes the separators horizontal
    Vertical - makes the separators vertical
    """

    Horizontal = tk.HORIZONTAL
    Vertical = tk.VERTICAL


class Separator(ttk.Separator):
    def __init__(
        self,
        parent: Union[tk.Widget, Union[tk.Tk, tk.Toplevel]],
        orientation: str = OrientModes.Vertical,
    ):
        """
        Initiate a ttk.Separator.

        :param parent: The parent of the scrollbar.
        :param orientation: The orientation of the scrollbar and what
         direction it should scroll the widget in. Defaults to
         OrientModes.Vertical and is a str.
        """
        if not isinstance(parent, (tk.Widget, tk.Tk, tk.Toplevel)):
            raise TypeError(
                f"parent is not a "
                f"Union[tk.Widget, Union[tk.Tk, tk.Toplevel]]! "
                f"(type passed in: {repr(type(parent))})"
            )
        if not isinstance(orientation, str):
            raise TypeError(
                f"orientation is not a str! "
                f"(type passed in: {repr(type(orientation))})"
            )
        super().__init__(master=parent, orient=orientation)
        self._style_root = "TSeparator"
        self._enabled = True
        self._orientation = orientation

    @property
    def enabled(self) -> bool:
        """
        Get whether this widget is in normal or disabled mode. (grayed out and
        cannot interact with)

        :return: A bool, True if normal otherwise False.
        """
        return self._enabled

    @enabled.setter
    def enabled(self, new_state: bool) -> None:
        """
        Set whether this widget is in normal mode or disabled mode. (grayed out
        and cannot interact with)

        :param new_state: The new state (a bool) True for enabled and False
         for disabled.
        :return: None.
        """
        if not isinstance(new_state, bool):
            raise TypeError(
                f"new_state is not a bool! "
                f"(type passed in: {repr(type(new_state))})"
            )
        self._enabled = new_state
        self.state(["!disabled" if self._enabled else "disabled"])