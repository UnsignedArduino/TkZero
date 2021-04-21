"""
Creates a themed Combobox.
"""

import tkinter as tk
from tkinter import ttk
from typing import Union, Callable

from TkZero.Platform import on_aqua


class Combobox(ttk.Combobox):
    def __init__(self, parent: Union[tk.Widget, Union[tk.Tk, tk.Toplevel]], values: tuple[str, ...] = (),
                 width: int = None, show: str = None, validate: Callable = None, command: Callable = None):
        """
        Initiate a ttk.Combobox.

        :param parent: The parent of the combobox.
        :param values: The default values you can choose, should be a tuple of str. Defaults to ()
        :param width: The width of the combobox. Defaults to None.
        :param show: The character to show instead of the actual text. Defaults to None.
        :param validate: The function to use for validation. Will be passed in a positional argument with the text as
         a str (like `validate(contents)`) and should return a bool - True if passed otherwise False.
        :param command: The command to run when the value of the combobox changes. Defaults to None.
        """
        if not isinstance(parent, (tk.Widget, tk.Tk, tk.Toplevel)):
            raise TypeError(f"parent is not a Union[tk.Widget, Union[tk.Tk, tk.Toplevel]]! "
                            f"(type passed in: {repr(type(parent))})")
        if not isinstance(values, tuple):
            raise TypeError(f"values is not a tuple! (type passed in: {repr(type(values))})")
        if not isinstance(width, int) and width is not None:
            raise TypeError(f"width is not a int! (type passed in: {repr(type(width))})")
        if not isinstance(show, str) and show is not None:
            raise TypeError(f"show is not a str! (type passed in: {repr(type(show))})")
        self._variable = tk.StringVar(value="")
        if command is not None:
            self._variable.trace_add("write", lambda *args: command())
        super().__init__(master=parent, width=width, textvariable=self._variable, show=show,
                         validatecommand=(parent.register(validate), "%p") if validate is not None else None)
        self._style_root = "TCombobox"
        self._enabled = True
        self._readonly = False
        if on_aqua(self):
            self.bind("<2>", lambda event: self._popup(event=event))
            self.bind("<Control-1>", lambda event: self._popup(event=event))
        else:
            self.bind("<3>", lambda event: self._popup(event=event))
        if values is not None:
            self["values"] = values
        self._make_context_menu()

    @property
    def value(self) -> str:
        """
        Get the text in this combobox.

        :return: A str of the text in this entry.
        """
        return self.get()

    @value.setter
    def value(self, new_text: str) -> None:
        """
        Set the text on this combobox.

        :param new_text: The new text.
        :return: None.
        """
        if not isinstance(new_text, str):
            raise TypeError(f"new_text is not a str! (type passed in: {repr(type(new_text))})")
        self.delete(0, tk.END)
        self.insert(0, new_text)

    @property
    def values(self) -> tuple[str]:
        """
        Get the default options you can select.

        :return: A str of the text in this entry.
        """
        return self["values"] if self["values"] else ()

    @values.setter
    def values(self, new_values: tuple[str]) -> None:
        """
        Set the default options text on this combobox.

        :param new_values: The new options, as a tuple of str.
        :return: None.
        """
        if not isinstance(new_values, tuple):
            raise TypeError(f"new_values is not a tuple! (type passed in: {repr(type(new_values))})")
        self["values"] = new_values

    @property
    def enabled(self) -> bool:
        """
        Get whether this combobox is in normal mode or disabled mode. (grayed out and cannot interact with)

        :return: A bool, True if normal otherwise False.
        """
        return self._enabled

    @enabled.setter
    def enabled(self, new_state: bool) -> None:
        """
        Set whether this combobox is in normal mode or disabled mode. (grayed out and cannot interact with)

        :param new_state: The new state (a bool) True for enabled and False for disabled.
        :return: None.
        """
        if not isinstance(new_state, bool):
            raise TypeError(f"new_state is not a bool! (type passed in: {repr(type(new_state))})")
        self._enabled = new_state
        self._readonly = False
        self.state(["!disabled" if self._enabled else "disabled"])

    @property
    def read_only(self) -> bool:
        """
        Get whether this combobox is read only mode. (cannot type in selection manually - must select from pre-defined
        values)

        :return: A bool, True if read only otherwise False.
        """
        return self._readonly

    @read_only.setter
    def read_only(self, new_state: bool) -> None:
        """
        Set whether this combobox is in read only mode (cannot type in selection manually - must select from pre-defined
        values)

        :param new_state: The new state (a bool) True for normal and False for read only.
        :return: None.
        """
        if not isinstance(new_state, bool):
            raise TypeError(f"new_state is not a bool! (type passed in: {repr(type(new_state))})")
        self._enabled = True
        self._readonly = new_state
        self.state(["readonly" if self._readonly else "!readonly"])

    def _make_context_menu(self) -> None:
        """
        Initiate the context menu.

        :return: None.
        """
        self._context_menu = tk.Menu(self, tearoff=0)
        self._context_menu.add_command(label="Copy", command=self.copy_contents, underline=0,
                                       accelerator="Command-C" if on_aqua(self) else "Control+C")
        self._context_menu.add_command(label="Cut", command=self.cut_contents,
                                       accelerator="Command-X" if on_aqua(self) else "Control+X")
        self._context_menu.add_command(label="Paste", command=self.paste_contents, underline=0,
                                       accelerator="Command-V" if on_aqua(self) else "Control+V")
        self._context_menu.add_separator()
        self._context_menu.add_command(label="Delete", command=self.delete_contents,
                                       accelerator="Delete")
        self._context_menu.add_separator()
        self._context_menu.add_command(label="Select all", command=self.select_all_contents, underline=7,
                                       accelerator="Command-A" if on_aqua(self) else "Control+A")

    def _update_context_menu_states(self) -> None:
        """
        Update the context menu states, like whether to allow copying or not.

        :return: None.
        """
        if not self.enabled:
            self._context_menu.entryconfigure("Copy", state=tk.DISABLED)
            self._context_menu.entryconfigure("Cut", state=tk.DISABLED)
            self._context_menu.entryconfigure("Paste", state=tk.DISABLED)
            self._context_menu.entryconfigure("Delete", state=tk.DISABLED)
            self._context_menu.entryconfigure("Select all", state=tk.DISABLED)
            return
        if self.read_only:
            self._context_menu.entryconfigure("Copy", state=tk.NORMAL)
            self._context_menu.entryconfigure("Cut", state=tk.DISABLED)
            self._context_menu.entryconfigure("Paste", state=tk.DISABLED)
            self._context_menu.entryconfigure("Delete", state=tk.DISABLED)
            self._context_menu.entryconfigure("Select all", state=tk.NORMAL)
            return
        if self.selection_present():
            self._context_menu.entryconfigure("Copy", state=tk.NORMAL)
            self._context_menu.entryconfigure("Cut", state=tk.NORMAL)
            self._context_menu.entryconfigure("Paste", state=tk.NORMAL)
            self._context_menu.entryconfigure("Delete", state=tk.NORMAL)
            self._context_menu.entryconfigure("Select all", state=tk.DISABLED)
        else:
            self._context_menu.entryconfigure("Copy", state=tk.DISABLED)
            self._context_menu.entryconfigure("Cut", state=tk.DISABLED)
            self._context_menu.entryconfigure("Paste", state=tk.NORMAL)
            self._context_menu.entryconfigure("Delete", state=tk.DISABLED)
            self._context_menu.entryconfigure("Select all", state=tk.NORMAL)

    def _popup(self, event) -> None:
        """
        Try to pop up the context menu.

        :param event: An object that Tk passes in with information about the event that we need.
        :return: None.
        """
        self._update_context_menu_states()
        if self.enabled:
            try:
                self._context_menu.tk_popup(event.x_root, event.y_root, 0)
            finally:
                self._context_menu.grab_release()

    def select_all_contents(self) -> None:
        """
        Select everything.

        :return: None.
        """
        self.select_range(0, tk.END)

    def delete_contents(self) -> None:
        """
        Delete the highlighted things.

        :return: None.
        """
        if self.selection_present():
            self.delete(tk.SEL_FIRST, tk.SEL_LAST)

    def paste_contents(self) -> None:
        """
        Paste into the entry.

        :return: None.
        """
        self.delete_contents()
        self.insert(self.index(tk.INSERT), self.clipboard_get())

    def cut_contents(self) -> None:
        """
        Cut the highlighted contents.

        :return: None.
        """
        if self.selection_present():
            self.clipboard_clear()
            self.clipboard_append(self.selection_get())
            self.update()
            self.delete(tk.SEL_FIRST, tk.SEL_LAST)
            self.select_clear()

    def copy_contents(self) -> None:
        """
        Copy the highlighted contents.

        :return: None.
        """
        if self.selection_present():
            self.clipboard_clear()
            self.clipboard_append(self.selection_get())
            self.update()

    def apply_style(self, style_name: str) -> None:
        """
        Apply a theme to this combobox.

        :param style_name: The name of the theme as a str, ex. "Warning"
        :return: None.
        """
        if not isinstance(style_name, str):
            raise TypeError(f"style_name is not a str! (type passed in: {repr(type(style_name))})")
        self.configure(style=f"{style_name}.{self._style_root}")
