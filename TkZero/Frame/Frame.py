"""
Creates a themed frame.
"""
import tkinter as tk
from tkinter import ttk
from typing import Union, Any, Callable


class Frame(ttk.Frame):
    def __init__(self, parent: Union[tk.Widget, Union[tk.Tk, tk.Toplevel]]):
        """
        Initiate a ttk.Frame.

        :param parent: The parent of the frame.
        """
        super().__init__(master=parent)
        self._style_root = "TFrame"

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

    def apply_style(self, style_name: str) -> None:
        """
        Apply a theme to this frame.

        :param style_name: The name of the theme as a str, ex. "Warning"
        :return: None.
        """
        if not isinstance(style_name, str):
            raise TypeError(f"style_name is not a str! (type passed in: {repr(type(style_name))})")
        self.configure(style=f"{style_name}.{self._style_root}")
