"""
Show standard dialogs. You can also sub-class a dialog to make your own.
"""

import tkinter as tk
from pathlib import Path
from tkinter import colorchooser
from tkinter import filedialog as fd
from tkinter import messagebox as mbox
from typing import Union, Tuple

from TkZero import Window


def open_file(
    initial_dir: Path = None,
    title: str = None,
    file_types: Tuple[Tuple[str, str], ...] = None,
) -> Union[Path, None]:
    """
    Ask the user to open a file.

    :param initial_dir: The directory to start in. Should be a pathlib.Path
     and defaults to None.
    :param title: The title of the dialog. Should be a str and defaults to
     None.
    :param file_types: The filetypes allowed. Should be a tuple of tuples of
     str (ex. (("Text files, "*.txt"), ("All files", "*.*")) and defaults to
     None.
    :return: A pathlib.Path of the path, or None if user canceled it.
    """
    file_path = fd.askopenfilename(
        initialdir=str(initial_dir) if initial_dir is not None else None,
        title=title,
        filetypes=file_types if file_types is not None else (),
    )
    return Path(file_path) if file_path else None


def save_file(
    initial_dir: Path = None,
    title: str = None,
    file_types: Tuple[Tuple[str, str], ...] = None,
) -> Union[Path, None]:
    """
    Ask the user to save a file.

    :param initial_dir: The directory to start in. Should be a pathlib.Path
     and defaults to None.
    :param title: The title of the dialog. Should be a str and defaults to
     None.
    :param file_types: The filetypes allowed. Should be a tuple of tuples of
     str (ex. (("Text files, "*.txt"), ("All files", "*.*")) and defaults to
     None.
    :return: A pathlib.Path of the path, or None if user canceled it.
    """
    file_path = fd.asksaveasfilename(
        initialdir=str(initial_dir) if initial_dir is not None else None,
        title=title,
        filetypes=file_types if file_types is not None else (),
    )
    return Path(file_path) if file_path else None


def select_directory(initial_dir: Path = None, title: str = None) -> Union[Path, None]:
    """
    Ask the user to select a directory.

    :param initial_dir: The directory to start in. Should be a pathlib.Path
     and defaults to None.
    :param title: The title of the dialog. Should be a str and defaults to
     None.
    :return: A pathlib.Path of the path, or None if user canceled it.
    """
    file_path = fd.askdirectory(initialdir=str(initial_dir), title=title)
    return Path(file_path) if file_path else None


def choose_color(
    initial_color: str = "ffffff", as_rgb: bool = False
) -> Union[Union[str, Tuple[float]], None]:
    """
    Ask the user to select a color.

    :param initial_color: The inital color to start with. Should be a str and
     defaults to "ffffff" (white)
    :param as_rgb: A bool on whether to return it as a tuple of floats or the
     hex color string.
    :return: A str of the color (ex. "ff0000" which is red) or a tuple of
     floats (ex. (255.0, 0.0, 0.0) for red) if as_rgb is True or None if user
     canceled or dialog failed? (need repro)
    """
    color = colorchooser.askcolor(f"#{initial_color}")
    try:
        return color[0] if as_rgb else color[1][1:]
    except TypeError:
        return None


def show_info(
    parent: Union[tk.Widget, Union[tk.Tk, tk.Toplevel]],
    title: str,
    message: str,
    detail: str = None,
) -> None:
    """
    Show a info box.

    :param parent: The parent widget - should be a tk.Tk / tk.Toplevel.
    :param title: The title of the info box - should be a str.
    :param message: The message of the info box - should be a str.
    :param detail: The detail of the info box (displayed under message) -
     should be a str and defaults to None.
    :return: None.
    """
    mbox.showinfo(parent=parent, title=title, message=message, detail=detail)


def show_warning(
    parent: Union[tk.Widget, Union[tk.Tk, tk.Toplevel]],
    title: str,
    message: str,
    detail: str = None,
) -> None:
    """
    Show a warning box.

    :param parent: The parent widget - should be a tk.Tk / tk.Toplevel.
    :param title: The title of the warning box - should be a str.
    :param message: The message of the warning box - should be a str.
    :param detail: The detail of the warning box (displayed under message) -
     should be a str and defaults to None.
    :return: None.
    """
    mbox.showwarning(parent=parent, title=title, message=message, detail=detail)


def show_error(
    parent: Union[tk.Widget, Union[tk.Tk, tk.Toplevel]],
    title: str,
    message: str,
    detail: str = None,
) -> None:
    """
    Show an error box.

    :param parent: The parent widget - should be a tk.Tk / tk.Toplevel.
    :param title: The title of the error box - should be a str.
    :param message: The message of the error box - should be a str.
    :param detail: The detail of the error box (displayed under message) -
     should be a str and defaults to None.
    :return: None.
    """
    mbox.showerror(parent=parent, title=title, message=message, detail=detail)


def ask_ok_or_cancel(
    parent: Union[tk.Widget, Union[tk.Tk, tk.Toplevel]],
    title: str,
    message: str,
    detail: str = None,
) -> bool:
    """
    Show the user a prompt with the buttons "Ok" or "Cancel".

    :param parent: The parent widget - should be a tk.Tk / tk.Toplevel.
    :param title: The title of the box - should be a str.
    :param message: The message of the box - should be a str.
    :param detail: The detail of the box (displayed under message) - should be
     a str and defaults to None.
    :return: True if the user clicks Ok else False.
    """
    return mbox.askokcancel(parent=parent, title=title, message=message, detail=detail)


def ask_yes_or_no(
    parent: Union[tk.Widget, Union[tk.Tk, tk.Toplevel]],
    title: str,
    message: str,
    detail: str = None,
) -> bool:
    """
    Show the user a prompt with the buttons "Yes" or "No".

    :param parent: The parent widget - should be a tk.Tk / tk.Toplevel.
    :param title: The title of the box - should be a str.
    :param message: The message of the box - should be a str.
    :param detail: The detail of the box (displayed under message) - should be
     a str and defaults to None.
    :return: True if the user clicks Yes else No.
    """
    return mbox.askyesno(parent=parent, title=title, message=message, detail=detail)


def ask_yes_or_no_or_cancel(
    parent: Union[tk.Widget, Union[tk.Tk, tk.Toplevel]],
    title: str,
    message: str,
    detail: str = None,
) -> Union[bool, None]:
    """
    Show the user a prompt with the buttons "Yes" or "No" or "Cancel".

    :param parent: The parent widget - should be a tk.Tk / tk.Toplevel.
    :param title: The title of the box - should be a str.
    :param message: The message of the box - should be a str.
    :param detail: The detail of the box (displayed under message) - should be
     a str and defaults to None.
    :return: True if the user clicks Yes, False if the user clicks No, and
     None if the user clicks Cancel.
    """
    return mbox.askyesnocancel(
        parent=parent, title=title, message=message, detail=detail
    )


def ask_retry_cancel(
    parent: Union[tk.Widget, Union[tk.Tk, tk.Toplevel]],
    title: str,
    message: str,
    detail: str = None,
) -> bool:
    """
    Show the user a prompt with the buttons "Retry" or "Cancel".

    :param parent: The parent widget - should be a tk.Tk / tk.Toplevel.
    :param title: The title of the box - should be a str.
    :param message: The message of the box - should be a str.
    :param detail: The detail of the box (displayed under message) - should be
     a str and defaults to None.
    :return: True if the user clicks Retry otherwise False.
    """
    return mbox.askretrycancel(
        parent=parent, title=title, message=message, detail=detail
    )


class CustomDialog(Window.Window):
    def __init__(self, parent: Union[tk.Tk, tk.Toplevel]):
        """
        Create a custom dialog. (tk.Toplevel)
        First create an instance of this dialog. Then grid all your widgets
        into place. Then call grab_focus() (if needed) and then
        wait_till_destroyed. (if needed)

        :param parent: The parent, either a tk.Tk instance or a tk.Toplevel
         instance.
        """
        super().__init__(parent=parent)
        self.transient(master=parent)

    def grab_focus(self) -> None:
        """
        Grab all focus to this window.

        :return: None.
        """
        self.wait_visibility()
        self.grab_set()

    def release_focus(self) -> None:
        """
        Release the focus.

        :return: None.
        """
        self.grab_release()

    def wait_till_destroyed(self) -> None:
        """
        Pause here and wait until destroyed.

        :return: None.
        """
        self.wait_window()

    def destroy(self) -> None:
        """
        Destroy itself and all it's children. This will also release the focus.

        :return: None.
        """
        self.release_focus()
        super().destroy()
