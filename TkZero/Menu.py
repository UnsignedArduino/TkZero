"""
Creates menus.
"""

import tkinter as tk
from typing import Union, Callable, Any


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
    Names for the system menus you can override - if you pass on of these in
    it would override/extend that menu.
    Application - the application menu on aqua. Should only be used on aqua
     windowing systems. (macOS)
    Help - the help menu on aqua and x11. On the win32 window manager, just
     define a "Help" menu last.
    Window - the window menu on macOS. Anything added to this menu will before
     the list of windows in your program. (Tk takes care of that)
    System - the menu that pops up when clicking on a Window's icon on the
     win32 window manager. Anything added will be under the list of standard
     commands already provided.
    """

    Application = "apple"
    Help = "help"
    Window = "window"
    System = "system"


class Menu(tk.Menu):
    def __init__(
        self,
        parent: Union[tk.Menu, Union[tk.Tk, tk.Toplevel]],
        is_menubar: bool = False,
        command: Callable = None,
    ):
        """
        Initiate a tk.Menu

        :param parent: The parent of the menu.
        :param is_menubar: Whether this menu should be the menu bar that you
         attach menus too. Defaults to False.
        :param command: The command to run before actually showing it - useful
         for updating the menu items.
        """
        if not isinstance(parent, (tk.Menu, tk.Tk, tk.Toplevel)):
            raise TypeError(
                f"parent is not a Union[tk.Menu, Union[tk.Tk, tk.Toplevel]]! "
                f"(type passed in: {repr(type(parent))})"
            )
        if not isinstance(is_menubar, bool):
            raise TypeError(
                f"is_menubar is not a bool! "
                f"(type passed in: {repr(type(is_menubar))})"
            )
        super().__init__(master=parent, postcommand=command, tearoff=0)
        self.is_menubar = is_menubar
        self._items = None
        if is_menubar:
            parent.configure(menu=self)

    @property
    def items(self) -> list[Any]:
        """
        Get the items in this menu.

        :return: A list of MenuCommand, MenuSeparator, MenuCheckbutton,
         MenuRadiobutton, and MenuCascade.
        """
        return self._items

    @items.setter
    def items(self, new_items: list[Any]) -> None:
        """
        Set the items in this menu.

        :param new_items: A list of MenuCommand, MenuSeparator,
         MenuCheckbutton, MenuRadiobutton, and MenuCascade.
        :return: None.
        """
        if not isinstance(new_items, list):
            raise TypeError(
                f"new_items is not a list! "
                f"(type passed in: {repr(type(new_items))})"
            )
        end = self.index(tk.END)
        if end is not None:
            for index in range(int(end) + 1):
                self.delete(0)
        self._items = new_items
        for index, item in enumerate(self._items):
            if not isinstance(
                item,
                (
                    MenuCommand,
                    MenuSeparator,
                    MenuCheckbutton,
                    MenuRadiobutton,
                    MenuCascade,
                ),
            ):
                raise TypeError(
                    f"Item #{index}/{len(self._items)} in "
                    f"new_items is not a "
                    f"MenuCommand, MenuSeparator, "
                    f"MenuCheckbutton, MenuRadiobutton, "
                    f"or a MenuCascade! "
                    f"(type of item #{index}: "
                    f"{repr(type(item))})"
                )
            item.create(menu=self)


class MenuCommand:
    """
    A simple menu command object.
    """

    def __init__(
        self,
        label: str = "",
        command: Callable = lambda: None,
        enabled: bool = True,
        underline: int = None,
        accelerator: str = None,
    ):
        if not isinstance(label, str):
            raise TypeError(
                f"label is not a str! " f"(type passed in: {repr(type(label))})"
            )
        if not isinstance(enabled, bool):
            raise TypeError(
                f"enabled is not a bool! " f"(type passed in: {repr(type(enabled))})"
            )
        if not isinstance(underline, int) and underline is not None:
            raise TypeError(
                f"underline is not a int! " f"(type passed in: {repr(type(underline))})"
            )
        if not isinstance(accelerator, str) and accelerator is not None:
            raise TypeError(
                f"accelerator is not a str! "
                f"(type passed in: {repr(type(accelerator))})"
            )
        self.label = label
        self.command = command
        self.enabled = enabled
        self.underline = underline
        if self.underline:
            if self.underline >= len(self.label):
                raise ValueError(
                    f"underline cannot be greater then "
                    f"{len(self.label)}! "
                    f"(passed in: {self.underline})"
                )
            if self.underline < 0:
                raise ValueError(
                    f"underline cannot less then 0! " f"(passed in: {self.underline})"
                )
        self.accelerator = accelerator

    def create(self, menu: Menu):
        """
        Actually add this menu command to the specified menu.

        :param menu: A TkZero.Menu.Menu to add too.
        :return: None.
        """
        if not isinstance(menu, (Menu, tk.Menu)):
            raise TypeError(
                f"menu is not a TkZero.Menu.Menu or a Menu!"
                f"(type passed in: {repr(type(menu))})"
            )
        if hasattr(menu, "is_menubar") and menu.is_menubar:
            raise ValueError(
                f"This menu seems to be a menu bar so I can't" f"be added to it!"
            )
        menu.add_command(
            label=self.label,
            command=self.command,
            state=tk.NORMAL if self.enabled else tk.DISABLED,
            underline=self.underline,
            accelerator=self.accelerator,
        )


class MenuSeparator:
    """
    A simple menu separator object.
    """

    def create(self, menu: Menu):
        """
        Actually add this menu command to the specified menu.

        :param menu: A TkZero.Menu.Menu to add too.
        :return: None.
        """
        if not isinstance(menu, (Menu, tk.Menu)):
            raise TypeError(
                f"menu is not a TkZero.Menu.Menu or tk.Menu! "
                f"(type passed in: {repr(type(menu))})"
            )
        if hasattr(menu, "is_menubar") and menu.is_menubar:
            raise ValueError(
                f"This menu seems to be a menu bar so I can't" f"be added to it!"
            )
        menu.add_separator()


class MenuCheckbutton:
    """
    A simple menu checkbutton object.
    """

    def __init__(
        self,
        label: str = "",
        variable: tk.Variable = None,
        on_value: Union[str, Union[bool, Union[int, float]]] = True,
        off_value: Union[str, Union[bool, Union[int, float]]] = False,
        enabled: bool = True,
        underline: int = None,
        accelerator: str = None,
    ):
        if not isinstance(label, str):
            raise TypeError(
                f"label is not a str! " f"(type passed in: {repr(type(label))})"
            )
        if not isinstance(variable, tk.Variable) and variable is not None:
            raise TypeError(
                f"variable is not a tk.Variable! "
                f"(type passed in: {repr(type(variable))})"
            )
        if not isinstance(on_value, (str, bool, int, float)):
            raise TypeError(
                f"on_value is not a str, bool, int, or float! "
                f"(type passed in: {repr(type(on_value))})"
            )
        if not isinstance(off_value, (str, bool, int, float)):
            raise TypeError(
                f"off_value is not a str, bool, int, or float! "
                f"(type passed in: {repr(type(off_value))})"
            )
        if not isinstance(enabled, bool):
            raise TypeError(
                f"enabled is not a bool! " f"(type passed in: {repr(type(enabled))})"
            )
        if not isinstance(underline, int) and underline is not None:
            raise TypeError(
                f"underline is not a int! " f"(type passed in: {repr(type(underline))})"
            )
        if not isinstance(accelerator, str) and accelerator is not None:
            raise TypeError(
                f"accelerator is not a str! "
                f"(type passed in: {repr(type(accelerator))})"
            )
        self.label = label
        self.variable = variable
        self.on_value = on_value
        self.off_value = off_value
        self.enabled = enabled
        self.underline = underline
        if self.underline:
            if self.underline >= len(self.label):
                raise ValueError(
                    f"underline cannot be greater then "
                    f"{len(self.label)}! "
                    f"(passed in: {self.underline})"
                )
            if self.underline < 0:
                raise ValueError(
                    f"underline cannot less then 0! " f"(passed in: {self.underline})"
                )
        self.accelerator = accelerator

    def create(self, menu: Menu):
        """
        Actually add this menu checkbutton to the specified menu.

        :param menu: A TkZero.Menu.Menu to add too.
        :return: None.
        """
        if not isinstance(menu, Menu):
            raise TypeError(
                f"menu is not a tk.Menu! " f"(type passed in: {repr(type(menu))})"
            )
        if menu.is_menubar:
            raise ValueError(
                f"This menu seems to be a menu bar so I can't" f"be added to it!"
            )
        menu.add_checkbutton(
            label=self.label,
            variable=self.variable,
            onvalue=self.on_value,
            offvalue=self.off_value,
            state=tk.NORMAL if self.enabled else tk.DISABLED,
            underline=self.underline,
            accelerator=self.accelerator,
        )


class MenuRadiobutton:
    """
    A simple menu radiobutton object.
    """

    def __init__(
        self,
        value: Union[str, Union[bool, Union[int, float]]],
        label: str = "",
        variable: tk.Variable = None,
        enabled: bool = True,
        underline: int = None,
        accelerator: str = None,
    ):
        if not isinstance(value, (str, bool, int, float)):
            raise TypeError(
                f"onvalue_value is not a str, bool, int, or float! "
                f"(type passed in: {repr(type(value))})"
            )
        if not isinstance(variable, tk.Variable) and variable is not None:
            raise TypeError(
                f"variable is not a tk.Variable! "
                f"(type passed in: {repr(type(variable))})"
            )
        if not isinstance(label, str):
            raise TypeError(
                f"label is not a str! " f"(type passed in: {repr(type(label))})"
            )
        if not isinstance(enabled, bool):
            raise TypeError(
                f"enabled is not a bool! " f"(type passed in: {repr(type(enabled))})"
            )
        if not isinstance(underline, int) and underline is not None:
            raise TypeError(
                f"underline is not a int! " f"(type passed in: {repr(type(underline))})"
            )
        if not isinstance(accelerator, str) and accelerator is not None:
            raise TypeError(
                f"accelerator is not a str! "
                f"(type passed in: {repr(type(accelerator))})"
            )
        self.label = label
        self.variable = variable
        self.value = value
        self.enabled = enabled
        self.underline = underline
        if self.underline:
            if self.underline >= len(self.label):
                raise ValueError(
                    f"underline cannot be greater then "
                    f"{len(self.label)}! "
                    f"(passed in: {self.underline})"
                )
            if self.underline < 0:
                raise ValueError(
                    f"underline cannot less then 0! " f"(passed in: {self.underline})"
                )
        self.accelerator = accelerator

    def create(self, menu: Menu):
        """
        Actually add this menu radiobutton to the specified menu.

        :param menu: A TkZero.Menu.Menu to add too.
        :return: None.
        """
        if not isinstance(menu, Menu):
            raise TypeError(
                f"menu is not a tk.Menu! " f"(type passed in: {repr(type(menu))})"
            )
        if menu.is_menubar:
            raise ValueError(
                f"This menu seems to be a menu bar so I can't" f"be added to it!"
            )
        menu.add_radiobutton(
            label=self.label,
            variable=self.variable,
            value=self.value,
            state=tk.NORMAL if self.enabled else tk.DISABLED,
            underline=self.underline,
            accelerator=self.accelerator,
        )


class MenuCascade:
    """
    A simple menu cascade object.
    """

    def __init__(
        self,
        label: str = "",
        items: list[
            Union[
                MenuCommand,
                Union[
                    MenuSeparator, Union[MenuCheckbutton, Union[MenuRadiobutton, Any]]
                ],
            ],
            ...,
        ] = [],
        enabled: bool = True,
        underline: int = None,
    ):
        if not isinstance(label, str):
            raise TypeError(
                f"label is not a str! " f"(type passed in: {repr(type(label))})"
            )
        if not isinstance(items, list):
            raise TypeError(
                f"items is not a list! " f"(type passed in: {repr(type(items))})"
            )
        if not isinstance(enabled, bool):
            raise TypeError(
                f"enabled is not a bool! " f"(type passed in: {repr(type(enabled))})"
            )
        if not isinstance(underline, int) and underline is not None:
            raise TypeError(
                f"underline is not a int! " f"(type passed in: {repr(type(underline))})"
            )
        self.menu = None
        self.label = label
        self.enabled = enabled
        self.items = items
        self.underline = underline
        if self.underline:
            if self.underline >= len(self.label):
                raise ValueError(
                    f"underline cannot be greater then "
                    f"{len(self.label)}! "
                    f"(passed in: {self.underline})"
                )
            if self.underline < 0:
                raise ValueError(
                    f"underline cannot less then 0! " f"(passed in: {self.underline})"
                )

    def create(self, menu: Menu):
        """
        Actually add this menu cascade to the specified menu.

        :param menu: A TkZero.Menu.Menu to add too.
        :return: None.
        """
        if not isinstance(menu, Menu):
            raise TypeError(
                f"menu is not a tk.Menu! " f"(type passed in: {repr(type(menu))})"
            )
        self.menu = Menu(parent=menu)
        menu.add_cascade(menu=self.menu, label=self.label, underline=self.underline)
        for item in self.items:
            item.create(menu=self.menu)
