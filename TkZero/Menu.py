"""
Creates menus.
"""

import tkinter as tk
from typing import Union, Callable


class DisplayModes:
    """
    The display modes for menus.
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


class SystemMenuNames:
    """
    Names for the system menus you can override - if you pass on of these in it would override/extend that menu.
    Application - the application menu on aqua. Should only be used on aqua windowing systems. (macOS)
    Help - the help menu on aqua and x11. On the win32 window manager, just define a "Help" menu last.
    Window - the window menu on macOS. Anything added to this menu will before the list of windows in your program.
     (Tk takes care of that)
    System - the menu that pops up when clicking on a Window's icon on the win32 window manager. Anything added will
     be under the list of standard commands already provided.
    """
    Application = "apple"
    Help = "help"
    Window = "window"
    System = "system"


class Menu(tk.Menu):
    def __init__(self, parent: Union[tk.Tk, tk.Toplevel], is_menubar: bool = False, command: Callable = None):
        """
        Initiate a tk.Menu

        :param parent: The parent of the menu.
        :param is_menubar: Whether this menu should be the menu bar that you attach menus too. Defaults to False.
        :param command: The command to run before actually showing it - useful for updating the menu items.
        """
        if not isinstance(parent, (tk.Tk, tk.Toplevel)):
            raise TypeError(f"parent is not a Union[tk.Tk, tk.Toplevel]! "
                            f"(type passed in: {repr(type(parent))})")
        if not isinstance(is_menubar, bool):
            raise TypeError(f"is_menubar is not a bool! (type passed in: {repr(type(is_menubar))})")
        super().__init__(master=parent, postcommand=command, tearoff=0)
        if is_menubar:
            parent.configure(menu=self)
