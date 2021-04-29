"""
Test the TkZero.Dialog module
"""

import unittest
from pathlib import Path

from TkZero import Dialog
from TkZero.Label import Label
from TkZero.MainWindow import MainWindow


class DialogTest(unittest.TestCase):
    def test_open_file_no_params(self):
        root = MainWindow()
        root.minimize()
        root.after(ms=1000, func=lambda: root.close())
        Dialog.open_file()

    def test_open_file_good_params(self):
        root = MainWindow()
        root.minimize()
        root.after(ms=1000, func=lambda: root.close())
        Dialog.open_file(initial_dir=Path.cwd(), title="Foo bar",
                         file_types=(("Text files", "*.txt"), ("All files", "*.*")))

    def test_open_file_bad_params(self):
        root = MainWindow()
        root.minimize()
        root.after(ms=1000, func=lambda: root.close())
        with self.assertRaises(TypeError):
            Dialog.open_file(initial_dir=1)
        with self.assertRaises(TypeError):
            Dialog.open_file(title=lambda: None)
        with self.assertRaises(TypeError):
            Dialog.open_file(file_types=[0, 0, 0])

    def test_save_file_no_params(self):
        root = MainWindow()
        root.minimize()
        root.after(ms=1000, func=lambda: root.close())
        Dialog.save_file()

    def test_save_file_good_params(self):
        root = MainWindow()
        root.minimize()
        root.after(ms=1000, func=lambda: root.close())
        Dialog.save_file(initial_dir=Path.cwd(), title="Foo bar",
                         file_types=(("Text files", "*.txt"), ("All files", "*.*")))

    def test_save_file_bad_params(self):
        root = MainWindow()
        root.minimize()
        root.after(ms=1000, func=lambda: root.close())
        with self.assertRaises(TypeError):
            Dialog.save_file(initial_dir=1)
        with self.assertRaises(TypeError):
            Dialog.save_file(title=lambda: None)
        with self.assertRaises(TypeError):
            Dialog.save_file(file_types=[0, 0, 0])

    def test_select_directory_no_params(self):
        root = MainWindow()
        root.minimize()
        root.after(ms=1000, func=lambda: root.close())
        Dialog.select_directory()

    def test_select_directory_good_params(self):
        root = MainWindow()
        root.minimize()
        root.after(ms=1000, func=lambda: root.close())
        Dialog.select_directory(initial_dir=Path.cwd(), title="Foo bar")

    def test_select_directory_bad_params(self):
        root = MainWindow()
        root.minimize()
        root.after(ms=1000, func=lambda: root.close())
        with self.assertRaises(TypeError):
            Dialog.select_directory(initial_dir=1)
        with self.assertRaises(TypeError):
            Dialog.select_directory(title=lambda: None)

    def test_color_chooser_no_params(self):
        root = MainWindow()
        root.minimize()
        root.after(ms=1000, func=lambda: root.close())
        Dialog.choose_color()

    def test_color_chooser_good_params(self):
        root = MainWindow()
        root.minimize()
        root.after(ms=1000, func=lambda: root.close())
        Dialog.choose_color(initial_color="101010", as_rgb=True)

    def test_color_chooser_bad_params(self):
        root = MainWindow()
        root.minimize()
        root.after(ms=1000, func=lambda: root.close())
        with self.assertRaises(TypeError):
            Dialog.choose_color(initial_color=1234)
        with self.assertRaises(TypeError):
            Dialog.choose_color(as_rgb=42)

    def test_info_box_no_params(self):
        root = MainWindow()
        root.minimize()
        root.after(ms=1000, func=lambda: root.close())
        with self.assertRaises(TypeError):
            Dialog.show_info()

    def test_info_box_good_params(self):
        root = MainWindow()
        root.minimize()
        root.after(ms=1000, func=lambda: root.close())
        Dialog.show_info(parent=root, title="Title", message="Message", detail="Details")

    def test_info_box_bad_params(self):
        root = MainWindow()
        root.minimize()
        root.after(ms=1000, func=lambda: root.close())
        with self.assertRaises(TypeError):
            Dialog.show_info(parent=321123, title="", message="")
        with self.assertRaises(TypeError):
            Dialog.show_info(root, title=False, message="")
        with self.assertRaises(TypeError):
            Dialog.show_info(root, title="", message=())
        with self.assertRaises(TypeError):
            Dialog.show_info(root, title="", message="", detail=[])

    def test_warning_box_no_params(self):
        root = MainWindow()
        root.minimize()
        root.after(ms=1000, func=lambda: root.close())
        with self.assertRaises(TypeError):
            Dialog.show_warning()

    def test_warning_box_good_params(self):
        root = MainWindow()
        root.minimize()
        root.after(ms=1000, func=lambda: root.close())
        Dialog.show_warning(parent=root, title="Title", message="Message", detail="Details")

    def test_warning_box_bad_params(self):
        root = MainWindow()
        root.minimize()
        root.after(ms=1000, func=lambda: root.close())
        with self.assertRaises(TypeError):
            Dialog.show_warning(parent="asdf", title="", message="")
        with self.assertRaises(TypeError):
            Dialog.show_warning(root, title=1, message="")
        with self.assertRaises(TypeError):
            Dialog.show_warning(root, title="", message=lambda: None)
        with self.assertRaises(TypeError):
            Dialog.show_warning(root, title="", message="", detail=[])

    def test_error_box_no_params(self):
        root = MainWindow()
        root.minimize()
        root.after(ms=1000, func=lambda: root.close())
        with self.assertRaises(TypeError):
            Dialog.show_error()

    def test_error_box_good_params(self):
        root = MainWindow()
        root.minimize()
        root.after(ms=1000, func=lambda: root.close())
        Dialog.show_error(parent=root, title="Title", message="Message", detail="Details")

    def test_error_box_bad_params(self):
        root = MainWindow()
        root.minimize()
        root.after(ms=1000, func=lambda: root.close())
        with self.assertRaises(TypeError):
            Dialog.show_error(parent="asdf", title="", message="")
        with self.assertRaises(TypeError):
            Dialog.show_error(root, title=1, message="")
        with self.assertRaises(TypeError):
            Dialog.show_error(root, title="", message=lambda: None)
        with self.assertRaises(TypeError):
            Dialog.show_error(root, title="", message="", detail=[])

    def test_ok_cancel_box_no_params(self):
        root = MainWindow()
        root.minimize()
        root.after(ms=1000, func=lambda: root.close())
        with self.assertRaises(TypeError):
            Dialog.ask_ok_or_cancel()

    def test_ok_cancel_box_good_params(self):
        root = MainWindow()
        root.minimize()
        root.after(ms=1000, func=lambda: root.close())
        Dialog.ask_ok_or_cancel(parent=root, title="Title", message="Message", detail="Details")

    def test_ok_cancel_box_bad_params(self):
        root = MainWindow()
        root.minimize()
        root.after(ms=1000, func=lambda: root.close())
        with self.assertRaises(TypeError):
            Dialog.ask_ok_or_cancel(parent="asdf", title="", message="")
        with self.assertRaises(TypeError):
            Dialog.ask_ok_or_cancel(root, title=1, message="")
        with self.assertRaises(TypeError):
            Dialog.ask_ok_or_cancel(root, title="", message=lambda: None)
        with self.assertRaises(TypeError):
            Dialog.ask_ok_or_cancel(root, title="", message="", detail=[])

    def test_yes_no_box_no_params(self):
        root = MainWindow()
        root.minimize()
        root.after(ms=1000, func=lambda: root.close())
        with self.assertRaises(TypeError):
            Dialog.ask_yes_or_no()

    def test_yes_no_box_good_params(self):
        root = MainWindow()
        root.minimize()
        root.after(ms=1000, func=lambda: root.close())
        Dialog.ask_yes_or_no(parent=root, title="Title", message="Message", detail="Details")

    def test_yes_no_box_bad_params(self):
        root = MainWindow()
        root.minimize()
        root.after(ms=1000, func=lambda: root.close())
        with self.assertRaises(TypeError):
            Dialog.ask_yes_or_no(parent="asdf", title="", message="")
        with self.assertRaises(TypeError):
            Dialog.ask_yes_or_no(root, title=1, message="")
        with self.assertRaises(TypeError):
            Dialog.ask_yes_or_no(root, title="", message=lambda: None)
        with self.assertRaises(TypeError):
            Dialog.ask_yes_or_no(root, title="", message="", detail=[])

    def test_yes_no_cancel_box_no_params(self):
        root = MainWindow()
        root.minimize()
        root.after(ms=1000, func=lambda: root.close())
        with self.assertRaises(TypeError):
            Dialog.ask_yes_or_no_or_cancel()

    def test_yes_no_cancel_box_good_params(self):
        root = MainWindow()
        root.minimize()
        root.after(ms=1000, func=lambda: root.close())
        Dialog.ask_yes_or_no_or_cancel(parent=root, title="Title", message="Message", detail="Details")

    def test_yes_no_cancel_box_bad_params(self):
        root = MainWindow()
        root.minimize()
        root.after(ms=1000, func=lambda: root.close())
        with self.assertRaises(TypeError):
            Dialog.ask_yes_or_no_or_cancel(parent="asdf", title="", message="")
        with self.assertRaises(TypeError):
            Dialog.ask_yes_or_no_or_cancel(root, title=1, message="")
        with self.assertRaises(TypeError):
            Dialog.ask_yes_or_no_or_cancel(root, title="", message=lambda: None)
        with self.assertRaises(TypeError):
            Dialog.ask_yes_or_no_or_cancel(root, title="", message="",
                                           detail=[])

    def test_retry_cancel_box_no_params(self):
        root = MainWindow()
        root.minimize()
        root.after(ms=1000, func=lambda: root.close())
        with self.assertRaises(TypeError):
            Dialog.ask_retry_cancel()

    def test_retry_cancel_box_good_params(self):
        root = MainWindow()
        root.minimize()
        root.after(ms=1000, func=lambda: root.close())
        Dialog.ask_retry_cancel(parent=root, title="Title", message="Message", detail="Details")

    def test_retry_cancel_box_bad_params(self):
        root = MainWindow()
        root.minimize()
        root.after(ms=1000, func=lambda: root.close())
        with self.assertRaises(TypeError):
            Dialog.ask_retry_cancel(parent="asdf", message="", title="")
        with self.assertRaises(TypeError):
            Dialog.ask_retry_cancel(root, title=1, message="")
        with self.assertRaises(TypeError):
            Dialog.ask_retry_cancel(root, title="", message=lambda: None)
        with self.assertRaises(TypeError):
            Dialog.ask_retry_cancel(root, title="", message="", detail=[])

    def test_custom_dialog(self):
        root = MainWindow()
        root.lift()
        root.after(ms=1000, func=lambda: root.close())
        with self.assertRaises(TypeError):
            Dialog.CustomDialog(parent="lol")
        dialog = Dialog.CustomDialog(parent=root)
        dialog.title = "Title"
        # Must lift everything otherwise it hasn't drawn and grabbing the
        # focus will error
        dialog.lift()
        dialog.grab_focus()
        dialog.wait_till_destroyed()
        root.mainloop()

    def test_custom_dialog_binds(self):
        root = MainWindow()
        root.minimize()
        dialog = Dialog.CustomDialog(parent=root)
        func = lambda: None
        dialog.bind_to_event("<<MyOwnSpecialEvent>>", func, run_in_thread=True)
        binds = dialog.bind_to_event("<<MyOwnSpecialEvent>>")
        self.assertTrue(len(binds) > 0)
        root.close()

    def test_custom_dialog_enabled(self):
        root = MainWindow()
        root.lift()
        root.update()
        dialog = Dialog.CustomDialog(parent=root)
        dialog.lift()
        dialog.update()
        self.assertTrue(dialog.enabled)
        Label(dialog).grid(row=0, column=0)
        Label(dialog).grid(row=1, column=0)
        dialog.update()
        dialog.enabled = False
        self.assertFalse(dialog.enabled)
        root.close()


if __name__ == "__main__":
    unittest.main()
