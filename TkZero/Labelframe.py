"""
Creates a themed label frame.
"""

import tkinter as tk
from tkinter import ttk
from typing import Union


class Labelframe(ttk.Labelframe):
    def __init__(
        self, parent: Union[tk.Widget, Union[tk.Tk, tk.Toplevel]], text: str = ""
    ):
        """
        Initiate a ttk.Frame.

        :param parent: The parent of the frame.
        :param text: The text on the label frame. Should be a str and defaults
         to "".
        """
        if not isinstance(parent, (tk.Widget, tk.Tk, tk.Toplevel)):
            raise TypeError(
                f"parent is not a "
                f"Union[tk.Widget, Union[tk.Tk, tk.Toplevel]]! "
                f"(type passed in: {repr(type(parent))})"
            )
        if not isinstance(text, str):
            raise TypeError(
                f"text is not a str! " f"(type passed in: {repr(type(text))})"
            )
        super().__init__(master=parent, text=text)
        self._style_root = "TLabelframe"
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

        :param new_width: An int which should be the new width of the frame.
         Cannot be less than 1.
        :return: None.
        """
        if not isinstance(new_width, int):
            raise TypeError(
                f"new_height is not a int! "
                f"(type passed in: {repr(type(new_width))})"
            )
        if new_width < 1:
            raise ValueError(
                f"new_height is less than 1! " f"(value passed in: {repr(new_width)})"
            )
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

        :param new_height: An int which should be the new height of the frame.
         Cannot be less than 1.
        :return: None.
        """
        if not isinstance(new_height, int):
            raise TypeError(
                f"new_height is not an int! "
                f"(type passed in: {repr(type(new_height))})"
            )
        if new_height < 1:
            raise ValueError(
                f"new_height is less than 1! " f"(value passed in: {repr(new_height)})"
            )
        self.configure(height=new_height)

    def _enable_children(
        self, parent: Union[tk.Widget, None] = None, enable: bool = True
    ) -> None:
        """
        Enable or disable the children.

        :param parent: A tk.Widget that is our parent. If None then default to
         self.
        :param enable: Whether to enable or disable the children.
        :return: None.
        """
        if parent is None:
            parent = self
        for child in parent.winfo_children():
            if child.winfo_class() not in ("Frame", "LabelFrame"):
                try:
                    child.state(["!disabled" if enable else "disabled"])
                except AttributeError:
                    child.configure(state=tk.NORMAL if enable else tk.DISABLED)
            else:
                self._enable_children(parent, enable)

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
        if not isinstance(new_state, bool):
            raise TypeError(
                f"new_state is not a bool! "
                f"(type passed in: {repr(type(new_state))})"
            )
        self._enabled = new_state
        self._enable_children(enable=self._enabled)

    @property
    def text(self) -> str:
        """
        Get the text on this Labelframe.

        :return: A str.
        """
        return self.cget("text")

    @text.setter
    def text(self, new_text: str) -> None:
        """
        Set the text on this Labelframe.

        :param new_text: The new text. Should be a str.
        :return: None.
        """
        if not isinstance(new_text, str):
            raise TypeError(
                f"new_text is not a str! " f"(type passed in: {repr(type(new_text))})"
            )
        self.configure(text=new_text)

    def apply_style(self, style_name: str) -> None:
        """
        Apply a theme to this frame.

        :param style_name: The name of the theme as a str, ex. "Warning"
        :return: None.
        """
        if not isinstance(style_name, str):
            raise TypeError(
                f"style_name is not a str! "
                f"(type passed in: {repr(type(style_name))})"
            )
        self.configure(style=f"{style_name}.{self._style_root}")
