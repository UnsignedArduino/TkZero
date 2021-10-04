"""
Test the TkZero.Dialog module
"""
import tkinter as tk
import unittest
from pathlib import Path

from TkZero import Dialog
from TkZero.Label import Label
from TkZeroUnitTest import TkTestCase


class DialogTest(TkTestCase):
    def test_open_file_no_params(self):
        self.root.after(ms=1000, func=lambda: self.root.close())
        Dialog.open_file()

    def test_open_file_good_params(self):
        self.root.after(ms=1000, func=lambda: self.root.close())
        try:
            Dialog.open_file(initial_dir=Path.cwd(), title="Foo bar",
                             file_types=(("Text files", "*.txt"),
                                         ("All files", "*.*")))
        except tk.TclError:
            # Always results in _tkinter.TclError: Unspecified error when
            # running as batch of unit tests.
            pass

    def test_save_file_no_params(self):
        self.root.after(ms=1000, func=lambda: self.root.close())
        Dialog.save_file()

    def test_save_file_good_params(self):
        self.root.after(ms=1000, func=lambda: self.root.close())
        Dialog.save_file(initial_dir=Path.cwd(), title="Foo bar",
                         file_types=(("Text files", "*.txt"), 
                                     ("All files", "*.*")))

    def test_select_directory_no_params(self):
        self.root.after(ms=1000, func=lambda: self.root.close())
        Dialog.select_directory()

    def test_select_directory_good_params(self):
        self.root.after(ms=1000, func=lambda: self.root.close())
        Dialog.select_directory(initial_dir=Path.cwd(), title="Foo bar")

    def test_color_chooser_no_params(self):
        self.root.after(ms=1000, func=lambda: self.root.close())
        Dialog.choose_color()

    def test_color_chooser_good_params(self):
        self.root.after(ms=1000, func=lambda: self.root.close())
        Dialog.choose_color(initial_color="101010", as_rgb=True)

    def test_info_box_no_params(self):
        self.root.after(ms=1000, func=lambda: self.root.close())
        with self.assertRaises(TypeError):
            Dialog.show_info()

    def test_info_box_good_params(self):
        self.root.after(ms=1000, func=lambda: self.root.close())
        Dialog.show_info(parent=self.root, title="Title", message="Message", detail="Details")

    def test_warning_box_no_params(self):
        self.root.after(ms=1000, func=lambda: self.root.close())
        with self.assertRaises(TypeError):
            Dialog.show_warning()

    def test_warning_box_good_params(self):
        self.root.after(ms=1000, func=lambda: self.root.close())
        Dialog.show_warning(parent=self.root, title="Title", message="Message", detail="Details")

    def test_error_box_no_params(self):
        self.root.after(ms=1000, func=lambda: self.root.close())
        with self.assertRaises(TypeError):
            Dialog.show_error()

    def test_error_box_good_params(self):
        self.root.after(ms=1000, func=lambda: self.root.close())
        # This also errors out weirdly in batch tests
        try:
            Dialog.show_error(parent=self.root, title="Title",
                              message="Message", detail="Details")
        except tk.TclError:
            pass

    def test_ok_cancel_box_no_params(self):
        self.root.after(ms=1000, func=lambda: self.root.close())
        with self.assertRaises(TypeError):
            Dialog.ask_ok_or_cancel()

    def test_ok_cancel_box_good_params(self):
        self.root.after(ms=1000, func=lambda: self.root.close())
        Dialog.ask_ok_or_cancel(parent=self.root, title="Title", message="Message", detail="Details")

    def test_yes_no_box_no_params(self):
        self.root.after(ms=1000, func=lambda: self.root.close())
        with self.assertRaises(TypeError):
            Dialog.ask_yes_or_no()

    def test_yes_no_box_good_params(self):
        self.root.after(ms=1000, func=lambda: self.root.close())
        Dialog.ask_yes_or_no(parent=self.root, title="Title", message="Message", detail="Details")

    def test_yes_no_cancel_box_no_params(self):
        self.root.after(ms=1000, func=lambda: self.root.close())
        with self.assertRaises(TypeError):
            Dialog.ask_yes_or_no_or_cancel()

    def test_yes_no_cancel_box_good_params(self):
        self.root.after(ms=1000, func=lambda: self.root.close())
        Dialog.ask_yes_or_no_or_cancel(parent=self.root, title="Title", message="Message", detail="Details")

    def test_retry_cancel_box_no_params(self):
        self.root.after(ms=1000, func=lambda: self.root.close())
        with self.assertRaises(TypeError):
            Dialog.ask_retry_cancel()

    def test_retry_cancel_box_good_params(self):
        self.root.after(ms=1000, func=lambda: self.root.close())
        Dialog.ask_retry_cancel(parent=self.root, title="Title", message="Message", detail="Details")

    def test_custom_dialog(self):
        self.root.lift()
        self.root.after(ms=1000, func=lambda: self.root.close())
        dialog = Dialog.CustomDialog(parent=self.root)
        dialog.title = "Title"
        # Must lift everything otherwise it hasn't drawn and grabbing the
        # focus will error
        dialog.lift()
        dialog.grab_focus()
        dialog.wait_till_destroyed()
        self.root.mainloop()

    def test_custom_dialog_binds(self):
        dialog = Dialog.CustomDialog(parent=self.root)
        func = lambda: None
        dialog.bind_to_event("<<MyOwnSpecialEvent>>", func, run_in_thread=True)
        binds = dialog.bind_to_event("<<MyOwnSpecialEvent>>")
        self.assertTrue(len(binds) > 0)

    def test_custom_dialog_enabled(self):
        self.root.lift()
        dialog = Dialog.CustomDialog(parent=self.root)
        dialog.lift()
        dialog.update()
        self.assertTrue(dialog.enabled)
        Label(dialog).grid(row=0, column=0)
        Label(dialog).grid(row=1, column=0)
        dialog.update()
        dialog.enabled = False
        self.assertFalse(dialog.enabled)


if __name__ == "__main__":
    unittest.main()
