"""
Creates a themed label.
"""

import tkinter as tk
from tkinter import ttk
from typing import Union

from PIL.ImageTk import PhotoImage


class DisplayModes:
    """
    The display modes for labels.
    Original: Display only the image if set, otherwise text.
    Text: Text only
    Image: Image only
    Center: Text on top of image
    Top: Image above text
    Left: Image left of text, etc.
    """

    Original = "none"
    TextOnly = "text"
    ImageOnly = "image"
    CenterTextImage = "center"
    ImageTopText = "top"
    ImageLeftText = "left"
    ImageBottomText = "bottom"
    ImageRightText = "right"


class Label(ttk.Label):
    def __init__(
        self,
        parent: Union[tk.Widget, Union[tk.Tk, tk.Toplevel]],
        text: str = "",
        image: Union[PhotoImage, tk.PhotoImage] = None,
    ):
        """
        Initiate a ttk.Label.

        :param parent: The parent of the label.
        :param text: The text on the label. Defaults to "".
        :param image: The image on the label. Defaults to None.
        """
        super().__init__(master=parent)
        self._style_root = "TLabel"
        self._photo_image = None
        self._enabled = True
        self.text = text
        if image is not None:
            self.image = image
        self._hovering_over = False
        self.bind("<Enter>", lambda _: self._set_hover_state(True))
        self.bind("<Leave>", lambda _: self._set_hover_state(False))

    @property
    def text(self) -> str:
        """
        Get the text on this label.

        :return: A str of the text on this label.
        """
        return self.cget("text")

    @text.setter
    def text(self, new_text: str) -> None:
        """
        Set the text on this label.

        :param new_text: The new text.
        :return: None.
        """
        self.configure(text=new_text)

    @property
    def image(self) -> Union[PhotoImage, None]:
        """
        Get the PIL.ImageTk.PhotoImage on this label. Returns None if none was
        ever set.

        :return: A PIL.ImageTk.PhotoImage or a tk.PhotoImage or None.
        """
        return self._photo_image

    @image.setter
    def image(self, new_image: Union[PhotoImage, tk.PhotoImage]) -> None:
        """
        Set the PIL.ImageTk.PhotoImage on this label.

        :param new_image: A PIL.ImageTk.PhotoImage or None.
        :return: None.
        """
        self._photo_image = new_image
        self.configure(image=self._photo_image)

    @property
    def display_mode(self) -> str:
        """
        Get the display mode of this label.

        :return: A str, either one of "text", "image", "center", "top",
         "left", "bottom", or "right".
        """
        return str(self.cget("compound"))

    @display_mode.setter
    def display_mode(self, new_mode: str) -> None:
        """
        Set the display mode of this label.

        :param new_mode: A str, either one of "text", "image", "center",
         "top", "left", "bottom", or "right".
        :return: None.
        """
        self.configure(compound=new_mode)

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

    def apply_style(self, style_name: str) -> None:
        """
        Apply a theme to this label.

        :param style_name: The name of the theme as a str, ex. "Warning"
        :return: None.
        """
        self.configure(style=f"{style_name}.{self._style_root}")
