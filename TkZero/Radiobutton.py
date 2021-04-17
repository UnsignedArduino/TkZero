"""
Creates a themed Radiobutton.
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


class Radiobutton(ttk.Radiobutton):
    def __init__(self, parent: Union[tk.Widget, Union[tk.Tk, tk.Toplevel]], text: str = "",
                 image: Union[PhotoImage, tk.PhotoImage] = None, variable: tk.Variable = None,
                 value: Union[int, Union[float, Union[str, bool]]] = None,
                 command: Callable = None):
        """
        Initiate a ttk.Radiobutton.

        :param parent: The parent of the radiobutton.
        :param text: The text of the radiobutton. Defaults to "".
        :param image: The image on the radiobutton. Defaults to None.
        :param variable: The variable to connect to. (Should be a tk.Variable like a tk.StringVar) Defaults to None.
        :param value: The value to set the variable when selected. Defaults to None.
        :param command: The command to run when toggled. Defaults to None.
        """
        if not isinstance(parent, (tk.Widget, tk.Tk, tk.Toplevel)):
            raise TypeError(f"parent is not a Union[tk.Widget, Union[tk.Tk, tk.Toplevel]]! "
                            f"(type passed in: {repr(type(parent))})")
        if not isinstance(text, str):
            raise TypeError(f"text is not a str! (type passed in: {repr(type(text))})")
        if not isinstance(image, (PhotoImage, tk.PhotoImage)) and image is not None:
            raise TypeError(f"image is not a Union[PhotoImage, tk.PhotoImage]! (type passed in: {repr(type(image))})")
        if not isinstance(variable, tk.Variable) and variable is not None:
            raise TypeError(f"variable is not a tk.Variable! (type passed in: {repr(type(variable))})")
        if not isinstance(value, (int, float, str, bool)) and value is not None:
            raise TypeError(f"value is not a Union[int, Union[float, Union[str, bool]]]! "
                            f"(type passed in: {repr(type(value))})")
        super().__init__(master=parent, command=command, variable=variable, value=value)
        self._style_root = "TRadiobutton"
        self._photo_image = None
        self._enabled = True
        self.text = text
        if image is not None:
            self.image = image
        self.value = False

    @property
    def text(self) -> str:
        """
        Get the text on this radiobutton.

        :return: A str of the text on this radiobutton.
        """
        return self.cget("text")

    @text.setter
    def text(self, new_text: str) -> None:
        """
        Set the text on this radiobutton.

        :param new_text: The new text.
        :return: None.
        """
        if not isinstance(new_text, str):
            raise TypeError(f"new_text is not a str! (type passed in: {repr(type(new_text))})")
        self.configure(text=new_text)

    @property
    def image(self) -> Union[PhotoImage, None]:
        """
        Get the PIL.ImageTk.PhotoImage on this radiobutton. Returns None if none was ever set.

        :return: A PIL.ImageTk.PhotoImage or a tk.PhotoImage or None.
        """
        return self._photo_image

    @image.setter
    def image(self, new_image: Union[PhotoImage, tk.PhotoImage]) -> None:
        """
        Set the PIL.ImageTk.PhotoImage on this radiobutton.

        :param new_image: A PIL.ImageTk.PhotoImage or None.
        :return: None.
        """
        if not isinstance(new_image, (PhotoImage, tk.PhotoImage)):
            raise TypeError(f"new_image is not a PIL.ImageTk.PhotoImage or a tk.PhotoImage! (type passed in: "
                            f"{repr(type(new_image))})")
        self._photo_image = new_image
        self.configure(image=self._photo_image)

    @property
    def display_mode(self) -> str:
        """
        Get the display mode of this radiobutton.

        :return: A str, either one of "text", "image", "center", "top", "left", "bottom", or "right".
        """
        return str(self.cget("compound"))

    @display_mode.setter
    def display_mode(self, new_mode: str) -> None:
        """
        Set the display mode of this radiobutton.

        :param new_mode: A str, either one of "text", "image", "center", "top", "left", "bottom", or "right".
        :return: None.
        """
        if not isinstance(new_mode, str):
            raise TypeError(f"new_mode is not a str! (type passed in: {repr(type(new_mode))})")
        self.configure(compound=new_mode)

    @property
    def enabled(self) -> bool:
        """
        Get whether this widget is in normal mode or disabled mode. (grayed out and cannot interact with)

        :return: A bool, True if normal otherwise False.
        """
        return self._enabled

    @enabled.setter
    def enabled(self, new_state: bool) -> None:
        """
        Set whether this widget is in normal mode or disabled mode. (grayed out and cannot interact with)

        :param new_state: The new state (a bool) True for enabled and False for disabled.
        :return: None.
        """
        if not isinstance(new_state, bool):
            raise TypeError(f"new_state is not a bool! (type passed in: {repr(type(new_state))})")
        self._enabled = new_state
        self.state(["!disabled" if self._enabled else "disabled"])

    def apply_style(self, style_name: str) -> None:
        """
        Apply a theme to this checkbutton.

        :param style_name: The name of the theme as a str, ex. "Warning"
        :return: None.
        """
        if not isinstance(style_name, str):
            raise TypeError(f"style_name is not a str! (type passed in: {repr(type(style_name))})")
        self.configure(style=f"{style_name}.{self._style_root}")
