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
    style = ttk.Style()
    style.configure(f"{style_name}.{style_root}", **kwargs)
