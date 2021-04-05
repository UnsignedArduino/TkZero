"""
Test the TkZero.Window.Dialog module
"""

import unittest
from TkZero.Window.MainWindow import MainWindow
from TkZero.Window import Dialog
from pathlib import Path


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
            Dialog.show_info(parent="asdf")
        with self.assertRaises(TypeError):
            Dialog.show_info(title=1)
        with self.assertRaises(TypeError):
            Dialog.show_info(message=lambda: None)
        with self.assertRaises(TypeError):
            Dialog.show_info(detail=[])

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
            Dialog.show_warning(parent="asdf")
        with self.assertRaises(TypeError):
            Dialog.show_warning(title=1)
        with self.assertRaises(TypeError):
            Dialog.show_warning(message=lambda: None)
        with self.assertRaises(TypeError):
            Dialog.show_warning(detail=[])

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
            Dialog.show_error(parent="asdf")
        with self.assertRaises(TypeError):
            Dialog.show_error(title=1)
        with self.assertRaises(TypeError):
            Dialog.show_error(message=lambda: None)
        with self.assertRaises(TypeError):
            Dialog.show_error(detail=[])

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
            Dialog.ask_ok_or_cancel(parent="asdf")
        with self.assertRaises(TypeError):
            Dialog.ask_ok_or_cancel(title=1)
        with self.assertRaises(TypeError):
            Dialog.ask_ok_or_cancel(message=lambda: None)
        with self.assertRaises(TypeError):
            Dialog.ask_ok_or_cancel(detail=[])


if __name__ == "__main__":
    unittest.main()
