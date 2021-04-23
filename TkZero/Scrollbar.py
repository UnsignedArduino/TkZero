"""
Creates a themed scrollbar.
"""

import tkinter as tk
from tkinter import ttk
from typing import Union


class OrientModes:
    """
    The orient modes for scrollbars
    Horizontal - makes the scrollbar horizontal and scrolls left and right
    Vertical - makes the scrollbar vertical and scrolls up and down
    """

    Horizontal = tk.HORIZONTAL
    Vertical = tk.VERTICAL


class Scrollbar(ttk.Scrollbar):
    def __init__(
        self,
        parent: Union[tk.Widget, Union[tk.Tk, tk.Toplevel]],
        orientation: str = OrientModes.Vertical,
        widget: tk.Widget = None,
    ):
        """
        Initiate a ttk.Scrollbar.

        :param parent: The parent of the scrollbar.
        :param orientation: The orientation of the scrollbar and what
         direction it should scroll the widget in. Defaults to
         OrientModes.Vertical and is a str.
        :param widget: The widget to scroll. Defaults to None and should be a
         tk.Widget.
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
        if not isinstance(widget, tk.Widget) and widget is not None:
            raise TypeError(
                f"widget is not a tk.Widget! " f"(type passed in: {repr(type(widget))})"
            )
        super().__init__(master=parent, orient=orientation)
        self._style_root = "TScrollbar"
        self._enabled = True
        self._orientation = orientation
        if widget is not None:
            self.attach_to(widget=widget)

    # noinspection PyUnresolvedReferences
    def attach_to(self, widget: tk.Widget) -> None:
        """
        Attach to a widget.

        :param widget: The widget to scroll. Should be a tk.Widget.
        :return: None.
        """
        if not isinstance(widget, tk.Widget):
            raise TypeError(
                f"widget is not a tk.Widget! " f"(type passed in: {repr(type(widget))})"
            )
        if self._orientation == OrientModes.Vertical:
            try:
                self.configure(command=widget.yview)
                widget.configure(yscrollcommand=self.set)
            except AttributeError:
                raise ValueError(
                    f"This widget ({repr(widget)}) does not support scrolling "
                    f"in the X direction!"
                )
        else:
            try:
                self.configure(command=widget.xview)
                widget.configure(xscrollcommand=self.set)
            except AttributeError:
                raise ValueError(
                    f"This widget ({repr(widget)}) does not support scrolling "
                    f"in the Y direction!"
                )

    def grid(self, *args, **kwargs) -> None:
        """Position a widget in the parent widget in a grid. Use as options:
        column=number - use cell identified with given column (starting with 0)
        columnspan=number - this widget will span several columns
        in=master - use master to contain this widget
        in_=master - see 'in' option description
        ipadx=amount - add internal padding in x direction
        ipady=amount - add internal padding in y direction
        padx=amount - add padding in x direction
        pady=amount - add padding in y direction
        row=number - use cell identified with given row (starting with 0)
        rowspan=number - this widget will span several rows
        sticky=NSEW - if cell is larger on which sides will this
                      widget stick to the cell boundary
        :return: None.
        """
        super().grid(*args, **kwargs, sticky=tk.NSEW)

    @property
    def enabled(self) -> bool:
        """
        Whether this widget is in normal mode or disabled mode (grayed out and
        cannot interact with) in Tk terms.

        :return: A bool, True if normal otherwise False.
        """
        return self._enabled

    @enabled.setter
    def enabled(self, new_state: bool) -> None:
        """
        Set whether this widget is in normal mode or disabled mode (grayed out
        and cannot interact with) in Tk terms.

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
