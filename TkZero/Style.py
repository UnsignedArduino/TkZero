"""
Create a theme.
"""

from tkinter import ttk


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


def define_style(style_root: str, style_name: str, **kwargs) -> None:
    """
    Define a style that you can use.

    :param style_root: The widget that this style will apply to, ex. "TFrame". Should be a str.
    :param style_name: The name of the style, ex. "Warning". Should be a str. Then when you define, ex. a Frame, then
     you can call apply_style("Warning")
    :param kwargs: The named arguments for the style. (Like background="red")
    :return: None.
    """
    if not isinstance(style_root, str):
        raise TypeError(f"style_root is not a str! (type passed in: {repr(type(style_root))})")
    if not isinstance(style_name, str):
        raise TypeError(f"style_name is not a str! (type passed in: {repr(type(style_name))})")
    style = ttk.Style()
    style.configure(f"{style_name}.{style_root}", **kwargs)
