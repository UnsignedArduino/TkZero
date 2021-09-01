"""
Creates a themed frame.
"""

import tkinter as tk
from tkinter import ttk
from typing import Union

from TkZero import Platform


class Frame(ttk.Frame):
    def __init__(self, parent: Union[tk.Widget, Union[tk.Tk, tk.Toplevel]]):
        """
        Initiate a ttk.Frame.

        :param parent: The parent of the frame.
        """
        if not isinstance(parent, (tk.Widget, tk.Tk, tk.Toplevel)):
            raise TypeError(
                f"parent is not a "
                f"Union[tk.Widget, Union[tk.Tk, tk.Toplevel]]! "
                f"(type passed in: {repr(type(parent))})"
            )
        super().__init__(master=parent)
        self._style_root = "TFrame"
        self._enabled = True
        self._hovering_over = False
        self.bind("<Enter>", lambda _: self._set_hover_state(True))
        self.bind("<Leave>", lambda _: self._set_hover_state(False))

    @property
    def width(self) -> int:
        """
        Get the width of the frame.

        :return: An int which is the width of the frame.
        """
        return self.cget("width")

    @width.setter
    def width(self, new_width: int) -> None:
        """
        Set the width of the frame.

        :param new_width: An int which should be the new width of the frame.
         Cannot be less than 1.
        :return: None.
        """
        if not isinstance(new_width, int):
            raise TypeError(
                f"new_height is not a int! "
                f"(type passed in: {repr(type(new_width))})"
            )
        if new_width < 1:
            raise ValueError(
                f"new_height is less than 1! " f"(value passed in: {repr(new_width)})"
            )
        self.configure(width=new_width)

    @property
    def height(self) -> int:
        """
        Get the height of the frame.

        :return: An int which is the height of the frame.
        """
        return self.cget("height")

    @height.setter
    def height(self, new_height: int) -> None:
        """
        Set the width of the frame.

        :param new_height: An int which should be the new height of the frame.
         Cannot be less than 1.
        :return: None.
        """
        if not isinstance(new_height, int):
            raise TypeError(
                f"new_height is not an int! "
                f"(type passed in: {repr(type(new_height))})"
            )
        if new_height < 1:
            raise ValueError(
                f"new_height is less than 1! " f"(value passed in: {repr(new_height)})"
            )
        self.configure(height=new_height)

    def _enable_children(
        self, parent: Union[tk.Widget, None] = None, enable: bool = True
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
        if not isinstance(new_state, bool):
            raise TypeError(
                f"new_state is not a bool! "
                f"(type passed in: {repr(type(new_state))})"
            )
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

    def apply_style(self, style_name: str) -> None:
        """
        Apply a theme to this frame.

        :param style_name: The name of the theme as a str, ex. "Warning"
        :return: None.
        """
        if not isinstance(style_name, str):
            raise TypeError(
                f"style_name is not a str! "
                f"(type passed in: {repr(type(style_name))})"
            )
        self.configure(style=f"{style_name}.{self._style_root}")


class ScrollableFrame(Frame):
    def __init__(
        self,
        parent: Union[tk.Widget, Union[tk.Tk, tk.Toplevel]],
        x_scrolling: bool = False,
        y_scrolling: bool = True,
    ):
        """
        Create a scrollable frame.
        MAKE SURE WHEN GRIDING WIDGETS TO THIS FRAME TO USE THE FRAME
        ATTRIBUTE INSTEAD OF THIS FRAME DIRECTLY.

        :param parent: The parent of this frame.
        :param x_scrolling: A bool on whether to add a scrollbar in the x
         direction.
        :param y_scrolling: A bool on whether to add a scrollbar in the y
         direction.
        """
        # https://blog.teclado.com/tkinter-scrollable-frames/
        super().__init__(parent)
        self.x_scrolling = x_scrolling
        self.y_scrolling = y_scrolling
        self.disable_warnings = False
        self.canvas = tk.Canvas(self, highlightthickness=0)
        if x_scrolling:
            x_scrollbar = ttk.Scrollbar(
                self, orient=tk.HORIZONTAL, command=self.canvas.xview
            )
        if y_scrolling:
            y_scrollbar = ttk.Scrollbar(
                self, orient=tk.VERTICAL, command=self.canvas.yview
            )
        self.frame = Frame(self.canvas)
        self.frame.bind(
            "<Configure>",
            lambda _: self.canvas.configure(scrollregion=self.canvas.bbox(tk.ALL)),
        )
        self.canvas.create_window((0, 0), window=self.frame, anchor=tk.NW)
        if x_scrolling:
            self.canvas.configure(xscrollcommand=x_scrollbar.set)
        if y_scrolling:
            self.canvas.configure(yscrollcommand=y_scrollbar.set)
        self.canvas.grid(row=0, column=0)
        if x_scrolling:
            x_scrollbar.grid(row=1, column=0, sticky=tk.NSEW)
        if y_scrolling:
            y_scrollbar.grid(row=0, column=1, sticky=tk.NSEW)
        # https://stackoverflow.com/a/37858368/10291933
        self.frame.bind("<Enter>", self._bind_to_mousewheel)
        self.frame.bind("<Leave>", self._unbind_to_mousewheel)
        self._shift_pressed = False
        # https://stackoverflow.com/a/8089241/10291933
        # http://www.tcl.tk/man/tcl8.4/TkCmd/keysyms.htm
        self.frame.bind_all("<Shift_L>", lambda _: self._set_shift_pressed(True))
        self.frame.bind_all("<Shift_R>", lambda _: self._set_shift_pressed(True))
        self.frame.bind_all(
            "<KeyRelease-Shift_L>", lambda _: self._set_shift_pressed(False)
        )
        self.frame.bind_all(
            "<KeyRelease-Shift_R>", lambda _: self._set_shift_pressed(False)
        )
        self._hovering_over = False
        self.frame.bind("<Enter>", lambda _: self._set_hover_state(True))
        self.frame.bind("<Leave>", lambda _: self._set_hover_state(False))

    def _set_shift_pressed(self, is_pressed: bool) -> None:
        """
        Set whether shift is pressed or not.

        :param is_pressed: A bool.
        :return: None.
        """
        self._shift_pressed = is_pressed

    def _bind_to_mousewheel(self, event) -> None:
        """
        Bind to the mousewheel.

        :param event: An event that Tkinter passes in.
        :return: None
        """
        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)

    def _unbind_to_mousewheel(self, event) -> None:
        """
        Unbind to the mousewheel.

        :param event: An event that Tkinter passes in.
        :return: None
        """
        self.canvas.unbind_all("<MouseWheel>")

    def _on_mousewheel(self, event) -> None:
        """
        A callback for the mousewheel to scroll.

        :param event: An event that Tkinter passes in.
        :return: None.
        """
        if Platform.on_aqua(self):
            scroll = str(int(-1 * event.delta))
        else:
            scroll = str(int(-1 * (event.delta / 120)))
        if self._shift_pressed:
            if self.x_scrolling:
                self.canvas.xview_scroll(scroll, tk.UNITS)
        else:
            if self.y_scrolling:
                self.canvas.yview_scroll(scroll, tk.UNITS)

    def _enable_children(
        self, parent: Union[tk.Widget, None] = None, enable: bool = True
    ) -> None:
        """
        Enable or disable the children.

        :param parent: A tk.Widget that is our parent. If None then default to
         self.
        :param enable: Whether to enable or disable the children.
        :return: None.
        """
        if parent is None:
            parent = self.frame
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
    def width(self) -> int:
        """
        Get the width of the frame.

        :return: An int which is the width of the frame.
        """
        return self.frame.width

    @width.setter
    def width(self, new_width: int) -> None:
        """
        Set the width of the frame.

        :param new_width: An int which should be the new width of the frame.
         Cannot be less than 1.
        :return: None.
        """
        if not isinstance(new_width, int):
            raise TypeError(
                f"new_height is not a int! "
                f"(type passed in: {repr(type(new_width))})"
            )
        if new_width < 1:
            raise ValueError(
                f"new_height is less than 1! " f"(value passed in: {repr(new_width)})"
            )
        self.frame.width = new_width
        self.canvas.configure(width=new_width)

    @property
    def height(self) -> int:
        """
        Get the height of the frame.

        :return: An int which is the height of the frame.
        """
        return self.frame.height

    @height.setter
    def height(self, new_height: int) -> None:
        """
        Set the width of the frame.

        :param new_height: An int which should be the new height of the frame.
         Cannot be less than 1.
        :return: None.
        """
        if not isinstance(new_height, int):
            raise TypeError(
                f"new_height is not an int! "
                f"(type passed in: {repr(type(new_height))})"
            )
        if new_height < 1:
            raise ValueError(
                f"new_height is less than 1! " f"(value passed in: {repr(new_height)})"
            )
        self.frame.height = new_height
        self.canvas.configure(height=new_height)

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

    def _warn(self, method: str):
        """
        DON'T USE THE GRID, PACK, OR PLACE METHODS ON THE SCROLLABLE FRAME
        DIRECTLY!!! Make sure to set the parents of your widgets to the frame
        attribute of this scrollable frame. You can see the ScrollableFrame
        example in the widget examples for an example.
        """
        if not self.disable_warnings:
            raise RuntimeWarning(
                f"It seems like you are {method}ing "
                "into the ScrollableFrame directly, which "
                "may not be what you want.\n"
                "Usually, you would set the parent of the "
                "widget it into the `frame` attribute of me, "
                "so instead of:\n"
                "my_label = Label(scrollable_frame, ...)\n"
                "You would do:\n"
                "my_label = Label(scrollable_frame.frame, "
                "...)\n"
                "You can turn this warning off by "
                "setting disable_warnings to True on me "
                "like:\n"
                "scrollable_frame.disable_warnings = True"
            )

    def apply_style(self, style_name: str) -> None:
        """
        Apply a theme to this frame.

        :param style_name: The name of the theme as a str, ex. "Warning"
        :return: None.
        """
        if not isinstance(style_name, str):
            raise TypeError(
                f"style_name is not a str! "
                f"(type passed in: {repr(type(style_name))})"
            )
        self.frame.configure(style=f"{style_name}.{self._style_root}")
