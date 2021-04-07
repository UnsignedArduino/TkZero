"""
Create a theme.
"""
import tkinter as tk
from tkinter import ttk
from typing import Union, Any, Callable


class WidgetStyleRoots:
    Frame = "TFrame"
    Label = "TLabel"
    Button = "TButton"


def define_style(style_root: str, style_name: str, **kwargs) -> None:
    """
    Define a style that you can use.

    :param style_root: The widget that this style will apply to, ex. "TFrame". Should be a str.
    :param style_name: The name of the style, ex. "Warning". Should be a str. Then when you define, ex. a Frame, then
     you can call apply_style("Warning")
    :param kwargs: The named arguments for the style. (Like background="red")
    :return: None.
    """
    style = ttk.Style()
    style.configure(f"{style_name}.{style_root}", **kwargs)
