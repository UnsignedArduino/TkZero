"""
Create a theme.
"""

import tkinter as tk
from pathlib import Path
from tkinter import ttk
from typing import Union


class WidgetStyleRoots:
    Button = "TButton"
    Checkbutton = "TCheckbutton"
    Combobox = "TCombobox"
    Entry = "TEntry"
    Frame = "TFrame"
    Label = "TLabel"
    Progressbar = "TProgressbar"
    Radiobutton = "TRadiobutton"
    Scale = "TScale"
    Scrollbar = "TScrollbar"
    Spinbox = "TSpinbox"


def import_theme(root: tk.Tk, path: Union[str, Path]) -> None:
    """
    `source` the theme file in Tk. You must call this before using your theme!

    :param root: The root instance of the GUI. Should be a tk.Tk
    :param path: The path to the theme file. Should be a str or a pathlib.Path
    :return: None.
    """
    if not isinstance(root, tk.Tk):
        raise TypeError(f"root is not a tk.Tk! (type passed in: {repr(type(root))})")
    if not isinstance(path, (str, Path)):
        raise TypeError(
            f"path is not a str or a pathlib.Path! "
            f"(type passed in: {repr(type(path))})"
        )
    path = str(Path(path).resolve())
    root.tk.call("source", path)


def use_theme(root: tk.Tk, theme: str) -> None:
    """
    Use an theme!

    :param root: The root instance of the GUI. Should be a tk.Tk
    :param theme: The name of the theme, either a built-in one or a theme
     that was "source"d.
    :return: None.
    """
    if not isinstance(root, tk.Tk):
        raise TypeError(f"root is not a tk.Tk! (type passed in: {repr(type(root))})")
    if not isinstance(theme, str):
        raise TypeError(
            f"theme is not a str! " f"(type passed in: {repr(type(theme))})"
        )
    style = ttk.Style()
    style.theme_use(theme)


def define_style(style_root: str, style_name: str, **kwargs) -> None:
    """
    Define a style that you can use.

    :param style_root: The widget that this style will apply to, ex. "TFrame".
     Should be a str.
    :param style_name: The name of the style, ex. "Warning". Should be a str.
     Then when you define, ex. a Frame, then you can call
     apply_style("Warning")
    :param kwargs: The named arguments for the style. (Like background="red")
    :return: None.
    """
    if not isinstance(style_root, str):
        raise TypeError(
            f"style_root is not a str! " f"(type passed in: {repr(type(style_root))})"
        )
    if not isinstance(style_name, str):
        raise TypeError(
            f"style_name is not a str! " f"(type passed in: {repr(type(style_name))})"
        )
    style = ttk.Style()
    style.configure(f"{style_name}.{style_root}", **kwargs)
