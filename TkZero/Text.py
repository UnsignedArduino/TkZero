"""
Creates a "classic" Text.
"""

import tkinter as tk
from typing import Union

from TkZero.Platform import on_aqua


class TextWrap:
    """
    The ways a tk.Text can wrap.
    NoWrapping - no wrapping.
    CharWrapping - wrap at any character and can br
     eak randomly.
    WordWrapping - wrap at word
     spaces.
    """

    NoWrapping = tk.NONE
    CharWrapping = tk.CHAR
    WordWrapping = tk.WORD


class Text(tk.Text):
    def __init__(
        self,
        parent: Union[tk.Widget, Union[tk.Tk, tk.Toplevel]],
        width: int = None,
        height: int = None,
        wrapping: str = TextWrap.WordWrapping,
    ):
        """
        Initiate a tk.Text.

        :param parent: The parent of the text.
        :param width: The width of the text. Defaults to None.
        :param height: The width of the text. Defaults to None.
        :param wrapping: How to wrap words in the text. Defaults to
         TextWrap.WordWrapping
        """
        super().__init__(
            master=parent,
            width=width,
            height=height,
            wrap=wrapping,
            undo=True,
            maxundo=50_000,
        )
        self._enabled = True
        self._readonly = False
        self.enable_automatically = True
        if on_aqua(self):
            self.bind("<2>", lambda event: self._popup(event=event))
            self.bind("<Control-1>", lambda event: self._popup(event=event))
        else:
            self.bind("<3>", lambda event: self._popup(event=event))
        self._make_context_menu()
        # https://stackoverflow.com/a/40618152/10291933
        self._orig = self._w + "_orig"
        self.tk.call("rename", self._w, self._orig)
        self.tk.createcommand(self._w, self._proxy)
        self._hovering_over = False
        self.bind("<Enter>", lambda _: self._set_hover_state(True))
        self.bind("<Leave>", lambda _: self._set_hover_state(False))

    def _proxy(self, command, *args):
        cmd = (self._orig, command) + args
        try:
            if command in ("insert", "delete", "replace") and self._readonly:
                return
            result = self.tk.call(cmd)
        except tk.TclError:
            return
        if command in ("insert", "delete", "replace"):
            self.event_generate("<<TextModified>>")
        return result

    @property
    def text(self) -> str:
        """
        Get the text in this text.

        :return: A str of the text.
        """
        return self.get("1.0", tk.END)

    @text.setter
    def text(self, new_text: str) -> None:
        """
        Set the text on this entry.

        :param new_text: The new text.
        :return: None.
        """
        last_state = "read_only" if self._readonly else self["state"]
        if self.enable_automatically:
            self.enabled = True
        self.delete("1.0", tk.END)
        self.insert("1.0", new_text)
        if self.enable_automatically:
            if last_state == "read_only":
                self.read_only = True
            else:
                self.configure(state=last_state)

    @property
    def cursor(self) -> str:
        """
        Get the editing cursor position.

        :return: A string, like "1.0".
        """
        return self.index(tk.INSERT)

    @cursor.setter
    def cursor(self, new_pos: str) -> None:
        """
        Set the editing cursor position.

        :param new_pos: A string, like "1.0".
        :return: None.
        """
        self.mark_set(tk.INSERT, new_pos)

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
        self._readonly = False
        self.configure(state=tk.NORMAL if self._enabled else tk.DISABLED)

    @property
    def read_only(self) -> bool:
        """
        Get whether this widget is in read only mode. (can copy and paste but
        cannot edit)

        :return: A bool, True if read only otherwise False.
        """
        return self._readonly

    @read_only.setter
    def read_only(self, new_state: bool) -> None:
        """
        Set whether this widget is in read only mode. (can copy and paste but
        cannot edit)

        :param new_state: The new state (a bool) True for normal and False for
         read only.
        :return: None.
        """
        self.enabled = True
        self._readonly = new_state

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

    def _make_context_menu(self) -> None:
        """
        Initiate the context menu.

        :return: None.
        """
        self._context_menu = tk.Menu(self, tearoff=0)
        self._context_menu.add_command(
            label="Undo",
            command=self.undo_contents,
            underline=0,
            accelerator="Command-Z" if on_aqua(self) else "Control+Z",
        )
        self._context_menu.add_command(
            label="Redo",
            command=self.redo_contents,
            underline=0,
            accelerator="Command-Y" if on_aqua(self) else "Control+Y",
        )
        self._context_menu.add_separator()
        self._context_menu.add_command(
            label="Copy",
            command=self.copy_contents,
            underline=0,
            accelerator="Command-C" if on_aqua(self) else "Control+C",
        )
        self._context_menu.add_command(
            label="Cut",
            command=self.cut_contents,
            accelerator="Command-X" if on_aqua(self) else "Control+X",
        )
        self._context_menu.add_command(
            label="Paste",
            command=self.paste_contents,
            underline=0,
            accelerator="Command-V" if on_aqua(self) else "Control+V",
        )
        self._context_menu.add_separator()
        self._context_menu.add_command(
            label="Delete", command=self.delete_contents, accelerator="Delete"
        )
        self._context_menu.add_separator()
        self._context_menu.add_command(
            label="Select all",
            command=self.select_all_contents,
            underline=7,
            accelerator="Command-A" if on_aqua(self) else "Control+A",
        )

    def _update_context_menu_states(self) -> None:
        """
        Update the context menu states, like whether to allow copying or not.

        :return: None.
        """
        if not self.enabled:
            self._context_menu.entryconfigure("Undo", state=tk.DISABLED)
            self._context_menu.entryconfigure("Redo", state=tk.DISABLED)
            self._context_menu.entryconfigure("Copy", state=tk.DISABLED)
            self._context_menu.entryconfigure("Cut", state=tk.DISABLED)
            self._context_menu.entryconfigure("Paste", state=tk.DISABLED)
            self._context_menu.entryconfigure("Delete", state=tk.DISABLED)
            self._context_menu.entryconfigure("Select all", state=tk.DISABLED)
            return
        if self.tag_ranges(tk.SEL):
            self._context_menu.entryconfigure("Undo", state=tk.DISABLED)
            self._context_menu.entryconfigure("Redo", state=tk.DISABLED)
            self._context_menu.entryconfigure("Copy", state=tk.NORMAL)
            self._context_menu.entryconfigure("Cut", state=tk.NORMAL)
            self._context_menu.entryconfigure("Paste", state=tk.NORMAL)
            self._context_menu.entryconfigure("Delete", state=tk.NORMAL)
            self._context_menu.entryconfigure("Select all", state=tk.DISABLED)
        else:
            self._context_menu.entryconfigure(
                "Undo", state=tk.NORMAL if self.can_undo() else tk.DISABLED
            )
            self._context_menu.entryconfigure(
                "Redo", state=tk.NORMAL if self.can_redo() else tk.DISABLED
            )
            self._context_menu.entryconfigure("Copy", state=tk.DISABLED)
            self._context_menu.entryconfigure("Cut", state=tk.DISABLED)
            self._context_menu.entryconfigure("Paste", state=tk.NORMAL)
            self._context_menu.entryconfigure("Delete", state=tk.DISABLED)
            self._context_menu.entryconfigure("Select all", state=tk.NORMAL)

    def _popup(self, event) -> None:
        """
        Try to pop up the context menu.

        :param event: An object that Tk passes in with information about the
         event that we need.
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
        self.tag_add(tk.SEL, "1.0", tk.END)
        self.mark_set(tk.INSERT, "1.0")
        self.see(tk.INSERT)

    def delete_contents(self) -> None:
        """
        Delete the highlighted things.

        :return: None.
        """
        if self.tag_ranges(tk.SEL):
            self.delete(tk.SEL_FIRST, tk.SEL_LAST)
            self.add_undo_separator()

    def paste_contents(self) -> None:
        """
        Paste into the entry.

        :return: None.
        """
        self.delete_contents()
        self.insert(self.index(tk.INSERT), self.clipboard_get())
        self.add_undo_separator()

    def cut_contents(self) -> None:
        """
        Cut the highlighted contents.

        :return: None.
        """
        if self.tag_ranges(tk.SEL):
            self.clipboard_clear()
            self.clipboard_append(self.selection_get())
            self.add_undo_separator()
            self.update()
            self.delete_contents()

    def copy_contents(self) -> None:
        """
        Copy the highlighted contents.

        :return: None.
        """
        if self.tag_ranges(tk.SEL):
            self.clipboard_clear()
            self.clipboard_append(self.selection_get())
            self.add_undo_separator()
            self.update()

    def undo_contents(self) -> None:
        """
        Do an undo.

        :return: None.
        """
        if self.can_undo():
            self.edit_undo()
            self.update()

    def can_undo(self) -> bool:
        """
        Return a bool on whether we can undo or not.

        :return: A bool.
        """
        # https://tcl.tk/man/tcl8.6/TkCmd/text.htm#:~:text=false-,pathname%20edit%20canundo,-Returns
        return bool(self.tk.call(self, "edit", "canundo"))

    def redo_contents(self) -> None:
        """
        Do a redo.

        :return: None.
        """
        if self.can_redo():
            self.edit_redo()
            self.update()

    def can_redo(self) -> bool:
        """
        Return a bool on whether we can redo or not.

        :return: A bool.
        """
        # https://tcl.tk/man/tcl8.6/TkCmd/text.htm#:~:text=supported-,pathname%20edit%20canredo,-Returns
        return bool(self.tk.call(self, "edit", "canredo"))

    def add_undo_separator(self) -> None:
        """
        Inserts a separator on the undo stack.

        :return: None.
        """
        self.tk.call(self, "edit", "separator")
