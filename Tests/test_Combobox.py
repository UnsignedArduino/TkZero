"""
Test the TkZero.Combobox module
"""

import unittest

from TkZero import Style
from TkZero.Combobox import Combobox
from TkZero.MainWindow import MainWindow


class ComboboxTest(unittest.TestCase):
    def test_no_params(self):
        root = MainWindow()
        root.update()
        with self.assertRaises(TypeError):
            Combobox()
        root.update()
        root.close()

    def test_bad_params(self):
        root = MainWindow()
        root.update()
        with self.assertRaises(TypeError):
            Combobox(1)
        with self.assertRaises(TypeError):
            Combobox(root, values=[])
        with self.assertRaises(TypeError):
            Combobox(root, width=5.5)
        with self.assertRaises(TypeError):
            Combobox(root, show=False)
        root.update()
        root.close()

    def test_good_params(self):
        root = MainWindow()
        root.update()
        Combobox(root, width=20, show="*", values=("foo", "bar"),
                 command=print("Changed")).grid(row=0, column=0)
        root.update()
        root.close()

    def test_value(self):
        root = MainWindow()
        root.update()
        c = Combobox(root)
        c.grid(row=0, column=0)
        root.update()
        self.assertEqual(c.value, "")
        c.value = "Foo"
        self.assertEqual(c.value, "Foo")
        with self.assertRaises(TypeError):
            c.value = 1
        root.close()

    def test_values(self):
        root = MainWindow()
        root.update()
        c = Combobox(root)
        c.grid(row=0, column=0)
        root.update()
        self.assertEqual(c.values, ())
        c.values = ("Foo", )
        self.assertEqual(c.values, ("Foo", ))
        with self.assertRaises(TypeError):
            c.values = ["lol", "this", "doesn't", "work", "it", "must", "be",
                        "a", "tuple"]
        root.close()

    def test_enabled(self):
        root = MainWindow()
        root.update()
        c = Combobox(root)
        c.grid(row=0, column=0)
        root.update()
        self.assertTrue(c.enabled)
        c.enabled = False
        self.assertFalse(c.enabled)
        with self.assertRaises(TypeError):
            c.enabled = "lala"
        root.close()

    def test_read_only(self):
        root = MainWindow()
        root.update()
        c = Combobox(root)
        c.grid(row=0, column=0)
        root.update()
        self.assertFalse(c.read_only)
        c.read_only = True
        self.assertTrue(c.read_only)
        with self.assertRaises(TypeError):
            c.read_only = 1
        root.close()

    def test_right_click(self):
        root = MainWindow()
        root.update()
        c = Combobox(root)
        c.grid(row=0, column=0)
        root.update()
        c.enabled = False
        root.update()
        c._update_context_menu_states()
        root.update()
        c.enabled = True
        c.read_only = True
        root.update()
        c._update_context_menu_states()
        root.update()
        c.read_only = False
        c.select_all_contents()
        root.update()
        c._update_context_menu_states()
        root.update()
        c.copy_contents()
        root.update()
        c.cut_contents()
        root.update()
        c.delete_contents()
        root.update()
        c.paste_contents()
        root.update()
        root.close()

    def test_style(self):
        root = MainWindow()
        root.update()
        c = Combobox(root)
        c.grid(row=0, column=0)
        Style.define_style(Style.WidgetStyleRoots.Button, "Test", background="red")
        c.apply_style("Test")
        self.assertEqual(c.cget("style"), "Test.TCombobox")
        root.update()
        with self.assertRaises(TypeError):
            c.apply_style([bool])
        root.close()


if __name__ == '__main__':
    unittest.main()
