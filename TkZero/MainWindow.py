"""
Create the main window. Note that this should only be called once in your
program!
"""

import tkinter as tk
from threading import Thread
from typing import Union, Callable

from PIL import ImageTk

from TkZero import Platform
from TkZero import Vector
from TkZero.Menu import Menu


class MainWindow(tk.Tk):
    """
    The main window class.
    """

    def __init__(self):
        super().__init__()
        self.title = "Main Window"
        self._icon = None
        self._on_close = None
        self.protocol("WM_DELETE_WINDOW", self.close)
        self._enabled = True
        if Platform.on_aqua(self):
            Menu(self, is_menubar=True)

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
            raise TypeError(
                f"new_title is not a str! " f"(type passed in: {repr(type(new_title))})"
            )
        self.wm_title(new_title)

    @property
    def icon(self) -> Union[tk.PhotoImage, ImageTk.PhotoImage, None]:
        """
        Get the icon of the window. Will return None if the icon was never set
        before.

        :return: A tk.PhotoImage, a PIL.ImageTk.PhotoImage, or None.
        """
        return self._icon

    @icon.setter
    def icon(self, new_icon: Union[tk.PhotoImage, ImageTk.PhotoImage]) -> None:
        """
        Set the icon of the window.

        :param new_icon: A tk.PhotoImage or a PIL.ImageTk.PhotoImage.
        :return: None.
        """
        if not isinstance(new_icon, (tk.PhotoImage, ImageTk.PhotoImage)):
            raise TypeError(
                f"new_icon is not a tk.PhotoImage or an ImageTk.PhotoImage!"
                f"(type passed in: {repr(type(new_icon))})"
            )
        self._icon = new_icon
        self.tk.call("wm", "iconphoto", self, new_icon)

    @property
    def size(self) -> Vector.Size:
        """
        Return the size of the window.

        :return: A TkZero.Vector.Size with the width and height attributes.
        """
        self.update()
        return Vector.Size(width=self.winfo_width(), height=self.winfo_height())

    @size.setter
    def size(self, new_size: Union[Vector.Size, tuple[int, int]]) -> None:
        """
        Set the size of the window.

        :param new_size: A TkZero.Vector.Size or a tuple with the width and
        height attributes set to the size you want.
        :return: None.
        """
        if not isinstance(new_size, (Vector.Size, tuple)):
            raise TypeError(
                f"new_size is not a Vector.Size or a tuple! "
                f"(type passed in: {repr(type(new_size))})"
            )
        if isinstance(new_size, tuple):
            if len(new_size) != 2:
                raise ValueError(
                    f"new_size has "
                    f"{'more than' if len(new_size) > 2 else 'less than'}"
                    f" 2 values! (got: {len(new_size)})"
                )
            for index, axis in enumerate(new_size):
                if not isinstance(axis, int):
                    raise TypeError(
                        f"new_size[{index}] is not an int! "
                        f"(type passed in: {repr(type(axis))})"
                    )
        if isinstance(new_size, tuple):
            self.geometry(f"{new_size[0]}x{new_size[1]}")
        else:
            self.geometry(f"{new_size.width}x{new_size.height}")
        self.update()

    @property
    def position(self) -> Vector.Position:
        """
        Return the position of the window.

        :return: A TkZero.Vector.Position with the x and y attributes.
        """
        self.update()
        return Vector.Position(x=self.winfo_x(), y=self.winfo_y())

    @position.setter
    def position(self, new_position: Union[Vector.Position, tuple[int, int]]) -> None:
        """
        Set the **top-left** position of the window.

        :param new_position: A TkZero.Vector.Position or a tuple with the new
         x and y attributes.
        :return: None.
        """
        if not isinstance(new_position, (Vector.Position, tuple)):
            raise TypeError(
                f"new_position is not a Vector.Position or a tuple! "
                f"(type passed in: {repr(type(new_position))})"
            )
        if isinstance(new_position, tuple):
            if len(new_position) != 2:
                raise ValueError(
                    f"new_position has "
                    f"{'more than' if len(new_position) > 2 else 'less than'}"
                    f" 2 values! (got: {len(new_position)})"
                )
            for index, axis in enumerate(new_position):
                if not isinstance(axis, int):
                    raise TypeError(
                        f"new_position[{index}] is not an int! "
                        f"(type passed in: {repr(type(axis))})"
                    )
        if isinstance(new_position, tuple):
            self.geometry(
                f"{self.size.width}x{self.size.height}+"
                f"{new_position[0]}+{new_position[1]}"
            )
        else:
            self.geometry(
                f"{self.size.width}x{self.size.height}+"
                f"{new_position.x}+{new_position.y}"
            )

    @property
    def minimized(self) -> bool:
        """
        Is this window minimized?

        :return: A bool on whether this window is minimized.
        """
        return self.wm_state() == "iconic"

    @minimized.setter
    def minimized(self, to_minimize: bool) -> None:
        """
        Minimize the window.

        :param to_minimize: A bool on whether to minimize or to restore it.
        :return: None.
        """
        if not isinstance(to_minimize, bool):
            raise TypeError(
                f"to_minimize is not a bool! "
                f"(type passed in: {repr(type(to_minimize))})"
            )
        if to_minimize:
            self.iconify()
        else:
            self.deiconify()

    @property
    def restored(self) -> bool:
        """
        Is this window **not** minimized?

        :return: A bool on whether this window is not minimized.
        """
        return not self.minimized

    @restored.setter
    def restored(self, to_restore: bool) -> None:
        """
        Restore the window.

        :param to_restore: A bool on whether to restore or to minimize it.
        :return: None.
        """
        if not isinstance(to_restore, bool):
            raise TypeError(
                f"to_restore is not a bool! "
                f"(type passed in: {repr(type(to_restore))})"
            )
        if to_restore:
            self.deiconify()
        else:
            self.iconify()

    @property
    def maximized(self) -> bool:
        """
        Is this window maximized?

        :return: A bool on whether this window is maximized.
        """
        if Platform.on_x11(self):
            return self.attributes("-zoomed")
        else:
            return self.wm_state() == "zoomed"

    @maximized.setter
    def maximized(self, to_mazimize: bool) -> None:
        """
        Maximize the window.

        :param to_mazimize: Whether to maximize the window or minimize it.
        :return: None.
        """
        if not isinstance(to_mazimize, bool):
            raise TypeError(
                f"to_mazimize is not a bool! "
                f"(type passed in: {repr(type(to_mazimize))})"
            )
        if to_mazimize:
            if Platform.on_x11(self):
                self.attributes("-zoomed", True)
            else:
                self.state("zoomed")
        else:
            self.iconify()

    @property
    def full_screen(self) -> bool:
        """
        Is this window full-screen?

        :return: A bool on whether this window is full-screen.
        """
        return self.attributes("-fullscreen")

    @full_screen.setter
    def full_screen(self, full_screen: bool) -> None:
        """
        Set to full-screen or not.

        :param full_screen: Whether to full-screen the window or not.
        :return: None.
        """
        if not isinstance(full_screen, bool):
            raise TypeError(
                f"full_screen is not a bool! "
                f"(type passed in: {repr(type(full_screen))})"
            )
        self.attributes("-fullscreen", full_screen)

    def bind_to_event(
        self,
        event: str,
        func: Callable = None,
        run_in_thread: bool = False,
        add: bool = False,
    ) -> Union[None, list[str]]:
        """
        Bind a event to a function.

        :param event: A str of the event.
        :param func: A function to call when the even happens. If none is
         passed in then a list of binds will be returned.
        :param run_in_thread: Whether to run the function in a thread when
         called. No arguments will be passed in. It will also be made as a
         daemon thread. (will be terminated if main thread terminates)
        :param add: Whether to add the function to a list of functions to be
         called or replace the function that was previously bound to this
         sequence if any.
        :return: A list of functions (As Tk function str) that would be called
         when this event is triggered or None when binding one.
        """
        if not isinstance(event, str):
            raise TypeError(
                f"event is not a str! (type passed in: {repr(type(event))})"
            )
        if not isinstance(run_in_thread, bool):
            raise TypeError(
                f"run_in_thread is not a bool! "
                f"(type passed in: {repr(type(run_in_thread))})"
            )
        if not isinstance(add, bool):
            raise TypeError(
                f"add is not a bool! " f"(type passed in: {repr(type(add))})"
            )
        if run_in_thread:
            func = Thread(target=func, args=(), daemon=True).start
        binds = self.bind(event, func, add)
        if binds is not None and type(binds) is not list:
            binds = [binds]
        return binds

    def generate_event(self, event: str) -> None:
        """
        Generate an event.

        :param event: The event to generate ("<<MyOwnEvent>>")
        :return: None.
        """
        self.event_generate(event)

    def _enable_children(
        self, parent: Union[tk.Widget, tk.Tk] = None, enable: bool = True
    ) -> None:
        """
        Enable or disable the children.

        :param parent: A tk.Widget that is our parent. If None then default to
         self.
        :param enable: Whether to enable or disable the children.
        :return: None.
        """
        if not isinstance(parent, tk.Widget) and parent is not None:
            raise TypeError(
                f"parent is not a tk.Widget! " f"(type passed in: {repr(type(parent))})"
            )
        if not isinstance(enable, bool):
            raise TypeError(
                f"enable is not a bool! (type passed in: {repr(type(enable))})"
            )
        if parent is None:
            parent = self
        for child in parent.winfo_children():
            if child.winfo_class() not in ("Frame", "LabelFrame"):
                try:
                    child.state(["!disabled" if enable else "disabled"])
                except AttributeError:
                    child.configure(state=tk.NORMAL if enable else tk.DISABLED)
            else:
                self._enable_children(parent, enable)

    @property
    def enabled(self) -> bool:
        """
        Get whether this widget is in normal mode or disabled mode. (grayed
        out and cannot interact with)

        :return: A bool, True if normal otherwise False.
        """
        return self._enabled

    @enabled.setter
    def enabled(self, new_state: bool) -> None:
        """
        Set whether this widget is in normal mode or disabled mode. (grayed
        out and cannot interact with)

        :param new_state: The new state (a bool) True for enabled and False
         for disabled.
        :return: None.
        """
        if not isinstance(new_state, bool):
            raise TypeError(
                f"new_state is not a bool! "
                f"(type passed in: {repr(type(new_state))})"
            )
        self._enabled = new_state
        self._enable_children(enable=self._enabled)

    @property
    def on_close(self) -> Union[Callable, None]:
        """
        Return the function that will be called when the user tries to close
        the window. If no function was assigned, return None.

        :return: A function or None.
        """
        return self._on_close

    @on_close.setter
    def on_close(self, new_func: Callable) -> None:
        """
        Set the function that will be called

        :param new_func: A function that will be called instead of destroying
         the window.
        :return: None.
        """
        self._on_close = new_func

    def close(self) -> None:
        """
        Close the window - this usually stops the whole program.

        :return:
        """
        if self._on_close is not None:
            self._on_close()
        else:
            self.destroy()
