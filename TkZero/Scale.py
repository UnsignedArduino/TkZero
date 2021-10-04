"""
Creates a themed scale. (Slider)
"""

import tkinter as tk
from tkinter import ttk
from typing import Union, Callable


class OrientModes:
    """
    The orient modes for scales.
    Horizontal - makes the scale horizontal and slides left and right.
    Vertical - makes the scale vertical and slides up and down.
    """

    Horizontal = tk.HORIZONTAL
    Vertical = tk.VERTICAL


class Scale(ttk.Scale):
    def __init__(
        self,
        parent: Union[tk.Widget, Union[tk.Tk, tk.Toplevel]],
        length: int,
        minimum: Union[int, float],
        maximum: Union[int, float],
        orientation: str = OrientModes.Horizontal,
        command: Callable = None,
    ):
        """
        Initiate a ttk.Scrollbar.

        :param parent: The parent of the scrollbar.
        :param length: An int, which is the length of the scale.
        :param minimum: The minimum value of the scale, an int or a float.
        :param maximum: The maximum value of the scale, an int or a float.
        :param orientation: The orientation of the scrollbar and what
         direction it should scroll the widget in. Defaults to
         OrientModes.Horizontal and is a str.
        :param command: The command to call when the scale changes. Will be
         passed in a positional float as the new value.
        """
        super().__init__(
            master=parent,
            orient=orientation,
            length=length,
            from_=float(minimum),
            to=float(maximum),
            command=lambda new_val: command(float(new_val))
            if command is not None
            else None,
        )
        self._style_root = "TScale"
        self._enabled = True
        self._orientation = orientation
        self._hovering_over = False
        self.bind("<Enter>", lambda _: self._set_hover_state(True))
        self.bind("<Leave>", lambda _: self._set_hover_state(False))

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
        self.set(float(new_value))

    @property
    def enabled(self) -> bool:
        """
        Get whether this widget is in normal mode or disabled mode. (grayed
        out and cannot interact with)

        :return: A bool, True if normal otherwise False.
        """
        return self._enabled

    @enabled.setter
    def enabled(self, new_state: bool) -> None:
        """
        Set whether this widget is in normal mode or disabled mode. (grayed
        out and cannot interact with)

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
