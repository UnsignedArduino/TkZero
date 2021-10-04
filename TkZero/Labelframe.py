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
        Initiate a ttk.Labelframe.

        :param parent: The parent of the frame.
        :param text: The text on the label frame. Should be a str and defaults
         to "".
        """
        super().__init__(master=parent, text=text)
        self._style_root = "TLabelframe"
        self._enabled = True
        self._hovering_over = False
        self.bind("<Enter>", lambda _: self._set_hover_state(True))
        self.bind("<Leave>", lambda _: self._set_hover_state(False))

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
        self._enabled = new_state
        self._enable_children(enable=self._enabled)

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
        self.configure(text=new_text)

    def apply_style(self, style_name: str) -> None:
        """
        Apply a theme to this frame.

        :param style_name: The name of the theme as a str, ex. "Warning"
        :return: None.
        """
        self.configure(style=f"{style_name}.{self._style_root}")
