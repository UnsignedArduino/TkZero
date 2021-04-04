"""
Create an additional window. Note that you will first need to initiate a main window to pass in!
"""
import tkinter as tk
from tkinter import ttk
from TkZero import Vector
from TkZero import Platform
from typing import Union, Any, Callable


class Window(tk.Toplevel):
    """
    The window class.
    """
    def __init__(self, parent: Union[tk.Tk, tk.Toplevel]):
        """
        Create a window. (tk.Toplevel)

        :param parent: The parent, either a tk.Tk instance of a tk.Toplevel instance.
        """
        master = parent
        cnf = {}
        """Construct a toplevel widget with the parent MASTER.

        Valid resource names: background, bd, bg, borderwidth, class,
        colormap, container, cursor, height, highlightbackground,
        highlightcolor, highlightthickness, menu, relief, screen, takefocus,
        use, visual, width."""
        extra = ()
        for wmkey in ['screen', 'class_', 'class', 'visual',
                      'colormap']:
            if wmkey in cnf:
                val = cnf[wmkey]
                # TBD: a hack needed because some keys
                # are not valid as keyword arguments
                if wmkey[-1] == '_':
                    opt = '-' + wmkey[:-1]
                else:
                    opt = '-' + wmkey
                extra = extra + (opt, val)
                del cnf[wmkey]
        tk.BaseWidget.__init__(self, master, "toplevel", cnf, {}, extra)
        root = self._root()
        self.iconname(root.iconname())
        self.title = "Window"
        self.protocol("WM_DELETE_WINDOW", self.destroy)

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

    def close(self) -> None:
        """
        Close the window - this usually stops the whole program.

        :return:
        """
        self.destroy()
