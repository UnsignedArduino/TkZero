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
        end = self.index(tk.END)
        if end is not None:
            for index in range(int(end) + 1):
                self.delete(0)
        self._items = new_items
        for index, item in enumerate(self._items):
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
        self.menu = Menu(parent=menu)
        menu.add_cascade(menu=self.menu, label=self.label, underline=self.underline)
        for item in self.items:
            item.create(menu=self.menu)
