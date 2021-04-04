"""
Create the main window. Note that this should only be called once in your program!
"""
import tkinter as tk
from tkinter import ttk
from TkZero import Vector
from TkZero import Platform
from typing import Union, Any, Callable


class MainWindow(tk.Tk):
    """
    The main window class.
    """
    def __init__(self):
        super().__init__()
        self.title = "Main Window"
        self.on_close = None
        self.protocol("WM_DELETE_WINDOW", self.close)

    @property
    def title(self) -> str:
        """
        Return the title of the window.

        :return: A str of the title.
        """
        return self.wm_title()

    @title.setter
    def title(self, new_title: str) -> None:
        """
        Set the title of the window.

        :param new_title: A str of the new title for the window.
        :return: None.
        """
        if not isinstance(new_title, str):
            raise TypeError(f"new_title is not a str! (type passed in: {repr(type(new_title))})")
        self.wm_title(new_title)

    @property
    def size(self) -> Vector.Size:
        """
        Return the size of the window.

        :return: A TkZero.Vector.Size with the width and height attributes.
        """
        self.update()
        return Vector.Size(width=self.winfo_width(), height=self.winfo_height())

    @size.setter
    def size(self, new_size: Vector.Size) -> None:
        """
        Set the size of the window.

        :param new_size: A TkZero.Vector.Size with the width and height attributes set to the size you want.
        :return: None.
        """
        if not isinstance(new_size.width, int):
            raise TypeError(f"new_size.width is not a int! (type passed in: {repr(type(new_size.width))})")
        if not isinstance(new_size.height, int):
            raise TypeError(f"new_size.height is not a int! (type passed in: {repr(type(new_size.height))})")
        self.geometry(f"{new_size.width}x{new_size.height}")

    @property
    def position(self) -> Vector.Position:
        """
        Return the position of the window.

        :return: A TkZero.Vector.Position with the x and y attributes.
        """
        return Vector.Position(x=self.winfo_x(), y=self.winfo_y())

    @position.setter
    def position(self, new_position: Vector.Position) -> None:
        """
        Set the **top-left** position of the window.

        :param new_position: A TkZero.Vector.Position with the new x and y attributes
        :return: None.
        """
        if not isinstance(new_position.x, int):
            raise TypeError(f"new_position.x is not a int! (type passed in: {repr(type(new_position.x))})")
        if not isinstance(new_position.y, int):
            raise TypeError(f"new_position.y is not a int! (type passed in: {repr(type(new_position.y))})")
        self.geometry(f"{self.size.width}x{self.size.height}+{new_position.x}+{new_position.y}")

    def minimize(self) -> None:
        """
        Minimize the window.

        :return: None.
        """
        self.iconify()

    def is_minimized(self) -> bool:
        """
        Is this window minimized?

        :return: A bool on whether this window is minimized.
        """
        return self.wm_state() == "iconic"

    def restore(self) -> None:
        """
        Restore the window.

        :return: None.
        """
        self.deiconify()

    def is_restored(self) -> bool:
        """
        Is this window **not** minimized?

        :return: A bool on whether this window is not minimized.
        """
        return not self.is_minimized()

    def maximize(self) -> None:
        """
        Maximize the window.

        :return: None.
        """
        if Platform.on_x11(self):
            self.attributes("-zoomed", True)
        else:
            self.state("zoomed")

    def is_maximized(self) -> bool:
        """
        Is this window maximized?

        :return: A bool on whether this window is maximized.
        """
        if Platform.on_x11(self):
            return self.attributes("-zoomed")
        else:
            return self.wm_state() == "zoomed"

    def full_screen(self, full_screen: bool) -> None:
        """
        Set to full-screen or not.

        :param full_screen: Whether to full-screen the window or not.
        :return: None.
        """
        if not isinstance(full_screen, bool):
            raise TypeError(f"full_screen is not a bool! (type passed in: {repr(type(full_screen))})")
        self.attributes("-fullscreen", full_screen)

    def is_full_screen(self) -> bool:
        """
        Is this window full-screen?

        :return: A bool on whether this window is full-screen.
        """
        return self.attributes("-fullscreen")

    @property
    def on_close(self) -> Union[Callable, None]:
        """
        Return the function that will be called when the user tries to close the window. If no function was assigned,
        return None.

        :return: A function or None.
        """
        return self._on_close

    @on_close.setter
    def on_close(self, new_func: Callable) -> None:
        """
        Set the function that will be called

        :param new_func: A function that will be called instead of destroying the window.
        :return: None.
        """
        self._on_close = new_func

    def close(self) -> None:
        """
        Close the window - this usually stops the whole program.

        :return:
        """
        if self.on_close is not None:
            self.on_close()
        else:
            self.destroy()
