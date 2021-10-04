"""
Creates tabbed notebooks.
"""

import tkinter as tk
from tkinter import ttk
from typing import Union

from TkZero.Frame import Frame


class Tab(Frame):
    def __init__(self, parent: ttk.Notebook, title: str = "Tab"):
        """
        Initiate a TkZero.Frame.Frame

        :param parent: The parent of the tab, which should be a notebook.
        """
        super().__init__(parent=parent)
        self._title = title
        self._parent = parent
        self._hovering_over = False
        self.bind("<Enter>", lambda _: self._set_hover_state(True))
        self.bind("<Leave>", lambda _: self._set_hover_state(False))

    @property
    def title(self) -> str:
        """
        Get the title of this tab.

        :return: A str
        """
        return self._title

    @title.setter
    def title(self, new_title: str) -> None:
        """
        Set the title of this tab.

        :param new_title: A str.
        :return: None.
        """
        self._title = new_title
        try:
            self._parent.tab(self, text=self._title)
        except tk.TclError:
            pass

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
        self._enable_children(enable=self._enabled)
        try:
            self._parent.tab(self, state=tk.NORMAL if self._enabled else tk.DISABLED)
        except tk.TclError:
            pass

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

    def add_to(self, notebook: ttk.Notebook) -> None:
        """
        Add this tab to the notebook at index.

        :param notebook: The notebook to add_to. Must be a ttk.Notebook.
        :return: None.
        """
        notebook.add(
            self, text=self.title, state=tk.NORMAL if self.enabled else tk.DISABLED
        )


class Notebook(ttk.Notebook):
    def __init__(self, parent: Union[tk.Widget, Union[tk.Tk, tk.Toplevel]]):
        """
        Initiate a ttk.Notebook

        :param parent: The parent of the notebook.
        """
        super().__init__(master=parent)
        self._tabs = []
        self._selected = 0

    @property
    def tabs(self) -> list[Tab]:
        """
        Get a list of tabs in this notebook.

        :return: A list of TkZero.Notebook.Tab
        """
        return self._tabs

    @tabs.setter
    def tabs(self, new_tabs: list[Tab]) -> None:
        """
        Set the list of tabs in this notebook.

        :param new_tabs: A list of TkZero.Notebook.Tab
        :return: None.
        """
        self._tabs = new_tabs

    def update_tabs(self) -> None:
        """
        Update the tabs. You should call this after adding tabs, removing, or
        modifying all your tabs.

        :return: None.
        """
        for tab in super().tabs():
            self.forget(tab)
        for index, tab in enumerate(self._tabs):
            tab.add_to(self)
        if len(self._tabs) > 0:
            self.selected = 0

    @property
    def selected(self) -> int:
        """
        Get the index of the selected tab.

        :return: An int.
        """
        return self._selected

    @selected.setter
    def selected(self, new_index: int) -> None:
        """
        Set the selected tab.

        :param new_index: An int of the position of the tab you want to be
         selected.
        :return: None.
        """
        if new_index < 0:
            raise ValueError(
                f"new_index cannot be less then 0! " f"(value passed in: {new_index})"
            )
        if new_index >= len(self.tabs):
            raise ValueError(
                f"new_index cannot be greater or equal to {len(self.tabs)}! "
                f"(value passed in: {new_index})"
            )
        self._selected = new_index
        self.select(self._selected)
