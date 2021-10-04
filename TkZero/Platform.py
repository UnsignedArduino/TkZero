"""
Get the windowing system.
"""

import tkinter as tk
from typing import Union


class WindowingSystem:
    """
    A bunch of variables on the possible windowing systems.
    """

    X11 = "x11"
    WIN32 = "win32"
    AQUA = "aqua"


def on_platform(
    widget: Union[tk.Widget, Union[tk.Tk, tk.Toplevel]], system: str
) -> bool:
    """
    Return a bool if we are on the windowing system passed in.

    :param widget: A Tkinter thing that we need to use so we can call into Tk.
     (Probably something like root or self)
    :param system: A str of "x11", "win32", or "aqua".
    :return: A bool on whether we are on the system passed in.
    """
    return widget.tk.call("tk", "windowingsystem") == system


def on_x11(widget: Union[tk.Widget, Union[tk.Tk, tk.Toplevel]]) -> bool:
    """
    Return whether we are on an X11 windowing system. (Usually Linux)

    :param widget: A Tkinter thing that we need to use so we can call into Tk.
     (Probably something like root or self)
    :return: A bool on whether we are on an X11 windowing system.
    """
    return on_platform(widget=widget, system=WindowingSystem.X11)


def on_win32(widget: Union[tk.Widget, Union[tk.Tk, tk.Toplevel]]) -> bool:
    """
    Return whether we are on a win32 windowing system. (Usually Windows)

    :param widget: A Tkinter thing that we need to use so we can call into Tk.
     (Probably something like root or self)
    :return: A bool on whether we are on a win32 windowing system.
    """
    return on_platform(widget=widget, system=WindowingSystem.WIN32)


def on_aqua(widget: Union[tk.Widget, Union[tk.Tk, tk.Toplevel]]) -> bool:
    """
    Return whether we are on an aqua windowing system. (Usually macOS)

    :param widget: A Tkinter thing that we need to use so we can call into Tk.
     (Probably something like root or self)
    :return: A bool on whether we are on an aqau windowing system.
    """
    return on_platform(widget=widget, system=WindowingSystem.AQUA)
