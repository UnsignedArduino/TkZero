"""
Create an additional window. Note that you will first need to initiate a main
window to pass in!
"""

import tkinter as tk
from threading import Thread
from typing import Union, Callable, List, Tuple

from TkZero import Platform
from TkZero import Vector


class Window(tk.Toplevel):
    """
    The window class.
    """

    def __init__(self, parent: Union[tk.Tk, tk.Toplevel]):
        """
        Create a window. (tk.Toplevel)

        :param parent: The parent, either a tk.Tk instance or a tk.Toplevel
         instance.
        """
        tk.BaseWidget.__init__(self, parent, "toplevel")
        self.iconname(self._root().iconname())
        self.title = "Window"
        self.protocol("WM_DELETE_WINDOW", self.close)
        self._on_close = None
        self._enabled = True
        self._hovering_over = False
        self.bind("<Enter>", lambda _: self._set_hover_state(True))
        self.bind("<Leave>", lambda _: self._set_hover_state(False))

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
    def size(self, new_size: Union[Vector.Size, Tuple[int, int]]) -> None:
        """
        Set the size of the window.

        :param new_size: A TkZero.Vector.Size or a tuple with the width and
        height attributes set to the size you want.
        :return: None.
        """
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
    def position(self, new_position: Union[Vector.Position, Tuple[int, int]]) -> None:
        """
        Set the **top-left** position of the window.

        :param new_position: A TkZero.Vector.Position or a tuple with the new
         x and y attributes.
        :return: None.
        """
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
        self.attributes("-fullscreen", full_screen)

    def bind_to_event(
        self,
        event: str,
        func: Callable = None,
        run_in_thread: bool = False,
        add: bool = False,
    ) -> Union[None, List[str]]:
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
        self,
        parent: Union[tk.Widget, Union[tk.Toplevel, None]] = None,
        enable: bool = True,
    ) -> None:
        """
        Enable or disable the children.

        :param parent: A tk.Widget that is our parent. If None then default to
         self.
        :param enable: Whether to enable or disable the children.
        :return: None.
        """
        if parent is None:
            parent = self
        for child in parent.winfo_children():
            if child.winfo_class() not in ("TFrame", "TLabelFrame"):
                try:
                    child.state(["!disabled" if enable else "disabled"])
                except AttributeError:
                    child.configure(state=tk.NORMAL if enable else tk.DISABLED)
            else:
                if hasattr(child, "enabled"):
                    child.enabled = enable
                else:
                    self._enable_children(child, enable)

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
        self._enabled = new_state
        self._enable_children(enable=self._enabled)

    @property
    def hovering_over(self) -> bool:
        """
        Get whether the cursor is hovering over this widget or not.

        :return: A bool.
        """
        return self._hovering_over

    def _set_hover_state(self, is_hovering: bool) -> None:
        """
        Set whether we are hovering over this widget or not.

        :param is_hovering: A bool.
        :return: None.
        """
        self._hovering_over = is_hovering

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
        Set the function that will be called.

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
