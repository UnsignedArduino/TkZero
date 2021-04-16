"""
Creates a themed frame.
"""
import tkinter as tk
from tkinter import ttk
from typing import Union


class Frame(ttk.Frame):
    def __init__(self, parent: Union[tk.Widget, Union[tk.Tk, tk.Toplevel]]):
        """
        Initiate a ttk.Frame.

        :param parent: The parent of the frame.
        """
        super().__init__(master=parent)
        self._style_root = "TFrame"
        self._enabled = True

    @property
    def width(self) -> int:
        """
        Get the width of the frame.

        :return: An int which is the width of the frame.
        """
        return self.cget("width")

    @width.setter
    def width(self, new_width: int) -> None:
        """
        Set the width of the frame.

        :param new_width: An int which should be the new width of the frame. Cannot be less than 1.
        :return: None.
        """
        if not isinstance(new_width, int):
            raise TypeError(f"new_height is not a int! (type passed in: {repr(type(new_width))})")
        if new_width < 1:
            raise ValueError(f"new_height is less than 1! (value passed in: {repr(new_width)})")
        self.configure(width=new_width)

    @property
    def height(self) -> int:
        """
        Get the height of the frame.

        :return: An int which is the height of the frame.
        """
        return self.cget("height")

    @height.setter
    def height(self, new_height: int) -> None:
        """
        Set the width of the frame.

        :param new_height: An int which should be the new height of the frame. Cannot be less than 1.
        :return: None.
        """
        if not isinstance(new_height, int):
            raise TypeError(f"new_height is not an int! (type passed in: {repr(type(new_height))})")
        if new_height < 1:
            raise ValueError(f"new_height is less than 1! (value passed in: {repr(new_height)})")
        self.configure(height=new_height)

    def _enable_children(self, parent: Union[tk.Widget, None] = None, enable: bool = True) -> None:
        """
        Enable or disable the children.

        :param parent: A tk.Widget that is our parent. If None then default to self.
        :param enable: Whether to enable or disable the children.
        :return: None.
        """
        if parent is None:
            parent = self
        for child in parent.winfo_children():
            if child.winfo_class() not in ("Frame", "LabelFrame"):
                child.state(["!disabled" if enable else "disabled"])
            else:
                self._enable_children(parent, enable)

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
        self._enable_children(enable=self._enabled)


    def apply_style(self, style_name: str) -> None:
        """
        Apply a theme to this frame.

        :param style_name: The name of the theme as a str, ex. "Warning"
        :return: None.
        """
        if not isinstance(style_name, str):
            raise TypeError(f"style_name is not a str! (type passed in: {repr(type(style_name))})")
        self.configure(style=f"{style_name}.{self._style_root}")
