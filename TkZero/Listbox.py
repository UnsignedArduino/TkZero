"""
Creates a "classic" Listbox
"""

import tkinter as tk
from typing import Union, Callable, Tuple, List


class SelectModes:
    """
    Select modes on listboxes you can use:
    Single: Single item only
    Multiple: Can select multiple items
    """

    Single = tk.BROWSE
    Multiple = tk.EXTENDED


class Listbox(tk.Listbox):
    def __init__(
        self,
        parent: Union[tk.Widget, Union[tk.Tk, tk.Toplevel]],
        values: Union[List[str, ...], Tuple[str, ...]] = None,
        select_mode: str = SelectModes.Single,
        height: int = None,
        width: int = None,
        on_select: Callable = None,
        on_double_click: Callable = None,
    ):
        """
        Initiate a tk.Listbox.

        :param parent: The parent of the listbox.
        :param values: The default values you can choose, should be a list or
         tuple of str. Defaults to []
        :param select_mode: The select mode to use. (allows you to select one
         or more items or not) Should be a str and defaults to
         SelectModes.Single
        :param height: The height of the listbox. Defaults to None.
        :param width: The width of the listbox. Defaults to None.
        :param on_select: The function to call
        """
        if values is not None:
            self._values = [str(item) for item in values]
        else:
            self._values = []
        self._variable = tk.StringVar(value=self._values)
        super().__init__(
            master=parent,
            height=height,
            width=width,
            listvariable=self._variable,
            selectmode=select_mode,
        )
        if on_select is not None:
            self.bind("<<ListboxSelect>>", lambda event: on_select())
        if on_double_click is not None:
            self.bind("<<Double-1>>", lambda event: on_double_click())
        self._enabled = True
        self._hovering_over = False
        self.bind("<Enter>", lambda _: self._set_hover_state(True))
        self.bind("<Leave>", lambda _: self._set_hover_state(False))

    @property
    def selected(self) -> Tuple[int]:
        """
        Get the selected items in this listbox.

        :return: A tuple of ints to represent the selected items.
        """
        return self.curselection()

    @selected.setter
    def selected(self, new_selection: Tuple[int]) -> None:
        """
        Set the selected items in this listbox.

        :param new_selection: The new selections. Should be a tuple of ints
         (ex. (0, 1, 3))
        :return: None.
        """
        self.selection_clear(0, tk.END)
        for index in new_selection:
            self.selection_set(index)

    @property
    def values(self) -> List[str]:
        """
        Get the values you can select.

        :return: A list of str of the values in this listbox.
        """
        return self._values

    @values.setter
    def values(self, new_values: Union[List[str, ...], Tuple[str, ...]]) -> None:
        """
        Set the items on this combobox.

        :param new_values: The new items, as a list or tuple of str.
        :return: None.
        """
        self._values = [str(item) for item in new_values]
        self._variable.set(self._values)

    def scroll_to(self, index: int) -> None:
        """
        Scroll to the index, so that we can see it.

        :param index: The index to scroll to. Raises IndexError if not in the
         list.
        :return: None.
        """
        if index >= len(self._values):
            raise IndexError(
                f"index is out of range! "
                f"(index passed in: {index} "
                f"length of items: {len(self._values)})"
            )
        self.see(index=index)

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
        self.config(state=tk.NORMAL if self._enabled else tk.DISABLED)

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
