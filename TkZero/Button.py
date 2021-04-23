"""
Creates a themed Button.
"""

import tkinter as tk
from tkinter import ttk
from typing import Union, Callable

from PIL.ImageTk import PhotoImage


class DisplayModes:
    """
    The display modes for buttons.

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


class Button(ttk.Button):
    def __init__(
        self,
        parent: Union[tk.Widget, Union[tk.Tk, tk.Toplevel]],
        text: str = "",
        image: Union[PhotoImage, tk.PhotoImage] = None,
        command: Callable = None,
    ):
        """
        Initiate a ttk.Button.

        :param parent: The parent of the button.
        :param text: The text of the button. Defaults to "".
        :param image: The image on the label. Defaults to None.
        :param command: The command to run when pressed. Defaults to None.
        """
        if not isinstance(parent, (tk.Widget, tk.Tk, tk.Toplevel)):
            raise TypeError(
                f"parent is not a Union[tk.Widget, Union[tk.Tk, tk.Toplevel]]! "
                f"(type passed in: {repr(type(parent))})"
            )
        if not isinstance(text, str):
            raise TypeError(f"text is not a str! (type passed in: {repr(type(text))})")
        if not isinstance(image, (PhotoImage, tk.PhotoImage)) and image is not None:
            raise TypeError(
                f"image is not a Union[PhotoImage, tk.PhotoImage]! (type passed in: {repr(type(image))})"
            )
        super().__init__(master=parent, command=command)
        self._style_root = "TButton"
        self._photo_image = None
        self._enabled = True
        self.text = text
        if image is not None:
            self.image = image

    @property
    def text(self) -> str:
        """
        Get the text on this button.

        :return: A str of the text on this button.
        """
        return self.cget("text")

    @text.setter
    def text(self, new_text: str) -> None:
        """
        Set the text on this button.

        :param new_text: The new text.
        :return: None.
        """
        if not isinstance(new_text, str):
            raise TypeError(
                f"new_text is not a str! (type passed in: {repr(type(new_text))})"
            )
        self.configure(text=new_text)

    @property
    def image(self) -> Union[PhotoImage, None]:
        """
        Get the PIL.ImageTk.PhotoImage on this button. Returns None if none was ever set.

        :return: A PIL.ImageTk.PhotoImage or a tk.PhotoImage or None.
        """
        return self._photo_image

    @image.setter
    def image(self, new_image: Union[PhotoImage, tk.PhotoImage]) -> None:
        """
        Set the PIL.ImageTk.PhotoImage on this button.

        :param new_image: A PIL.ImageTk.PhotoImage or None.
        :return: None.
        """
        if not isinstance(new_image, (PhotoImage, tk.PhotoImage)) and image is not None:
            raise TypeError(
                f"new_image is not a PIL.ImageTk.PhotoImage or a tk.PhotoImage! (type passed in: "
                f"{repr(type(new_image))})"
            )
        self._photo_image = new_image
        self.configure(image=self._photo_image)

    @property
    def display_mode(self) -> str:
        """
        Get the display mode of this button.

        :return: A str, either one of "text", "image", "center", "top", "left", "bottom", or "right".
        """
        return str(self.cget("compound"))

    @display_mode.setter
    def display_mode(self, new_mode: str) -> None:
        """
        Set the display mode of this button.

        :param new_mode: A str, either one of "text", "image", "center", "top", "left", "bottom", or "right".
        :return: None.
        """
        if not isinstance(new_mode, str):
            raise TypeError(
                f"new_mode is not a str! (type passed in: {repr(type(new_mode))})"
            )
        self.configure(compound=new_mode)

    @property
    def enabled(self) -> bool:
        """
        Whether this button is in normal mode or disabled mode. (grayed out and cannot interact with)

        :return: A bool, True if normal otherwise False.
        """
        return self._enabled

    @enabled.setter
    def enabled(self, new_state: bool) -> None:
        """
        Set whether this button is in normal mode or disabled mode. (grayed out and cannot interact with)

        :param new_state: The new state (a bool) True for enabled and False for disabled.
        :return: None.
        """
        if not isinstance(new_state, bool):
            raise TypeError(
                f"new_state is not a bool! (type passed in: {repr(type(new_state))})"
            )
        self._enabled = new_state
        self.state(["!disabled" if self._enabled else "disabled"])

    def apply_style(self, style_name: str) -> None:
        """
        Apply a theme to this button.

        :param style_name: The name of the theme as a str, ex. "Warning"
        :return: None.
        """
        if not isinstance(style_name, str):
            raise TypeError(
                f"style_name is not a str! (type passed in: {repr(type(style_name))})"
            )
        self.configure(style=f"{style_name}.{self._style_root}")
