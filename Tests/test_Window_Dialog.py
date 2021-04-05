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


if __name__ == "__main__":
    unittest.main()
