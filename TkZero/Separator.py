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
        super().__init__(master=parent, orient=orientation)
        self._style_root = "TSeparator"
        self._enabled = True
        self._orientation = orientation
        self._hovering_over = False
        self.bind("<Enter>", lambda _: self._set_hover_state(True))
        self.bind("<Leave>", lambda _: self._set_hover_state(False))

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
        self._enabled = new_state
        self.state(["!disabled" if self._enabled else "disabled"])

    @property
    def hovering_over(self) -> bool:
        """
        Get whether the cursor is hovering over this widget or not.

        :return: A bool.
        """
        return self._hovering_over

    def _set_hover_state(self, is_hovering: bool) -> None:
        """
        Set whether we are hovering over this widget or not.

        :param is_hovering: A bool.
        :return: None.
        """
        self._hovering_over = is_hovering
