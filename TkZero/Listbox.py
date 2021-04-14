"""
Creates a "classic" Listbox
"""
import tkinter as tk
from tkinter import ttk
from TkZero.Platform import on_aqua
from pathlib import Path
from PIL.ImageTk import PhotoImage
from typing import Union, Any, Callable


class SelectModes:
    """
    Select modes on listboxes you can use:
    Single: Single item only
    Multiple: Can select multiple items
    """
    Single = tk.BROWSE
    Multiple = tk.EXTENDED


class Listbox(tk.Listbox):
    def __init__(self, parent: Union[tk.Widget, Union[tk.Tk, tk.Toplevel]], values: list[str, ...] = [],
                 select_mode: str = SelectModes.Single, height: int = None, width: int = None,
                 on_select: Callable = None, on_double_click: Callable = None):
        """
        Initiate a tk.Listbox.

        :param parent: The parent of the listbox.
        :param values: The default values you can choose, should be a list of str. Defaults to []
        :param select_mode: The select mode to use. (allows you to select one or more items or not) Should be a str and
         defaults to SelectModes.Single
        :param height: The height of the listbox. Defaults to None.
        :param width: The width of the listbox. Defaults to None.
        :param on_select: The function to call
        """
        self._values = [str(item) for item in values]
        self._variable = tk.StringVar(value=self._values)
        super().__init__(master=parent, height=height, width=width, listvariable=self._variable)
        self._enabled = True

    @property
    def selected(self) -> tuple[int]:
        """
        Get the selected items in this listbox.

        :return: A tuple of ints to represent the selected items.
        """
        return self.curselection()

    @selected.setter
    def selected(self, new_selection: tuple[int]) -> None:
        """
        Set the selected items in this listbox.

        :param new_selection: The new selections. Should be a tuple of ints (ex. (0, 1, 3))
        :return: None.
        """
        if not isinstance(new_selection, tuple):
            raise TypeError(f"new_selection is not a tuple! (type passed in: {repr(type(new_selection))})")
        self.selection_clear(0, tk.END)
        for index in new_selection:
            self.selection_set(index)

    @property
    def values(self) -> list[str]:
        """
        Get the values you can select.

        :return: A list of str of the values in this listbox.
        """
        return self._values

    @values.setter
    def values(self, new_values: list[str]) -> None:
        """
        Set the items on this combobox.

        :param new_values: The new items, as a list of str.
        :return: None.
        """
        if not isinstance(new_values, list):
            raise TypeError(f"new_values is not a list! (type passed in: {repr(type(new_values))})")
        self._values = [str(item) for item in new_values]
        self._variable.set(self._values)

    def scroll_to(self, index: int) -> None:
        """
        Scroll to the index, so that we can see it.

        :param index: The index to scroll to. Raises IndexError if not in the list.
        :return: None.
        """
        if not isinstance(index, int):
            raise TypeError(f"index is not a int! (type passed in: {repr(type(index))})")
        if index < len(self._values):
            raise IndexError(f"index is out of range! (index passed in: {index} length of items: {len(self._values)}")
        self.see(index=index)

    @property
    def enabled(self) -> bool:
        """
        Whether this widget is disabled (grayed out and cannot interact with) in Tk terms.

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
        self.config(state=tk.NORMAL if self._enabled else tk.DISABLED)
