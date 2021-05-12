"""
Test the TkZero.Combobox module
"""

import unittest

from TkZero import Style
from TkZero.Combobox import Combobox
from TkZeroUnitTest import TkTestCase


class ComboboxTest(TkTestCase):
    def test_no_params(self):
        with self.assertRaises(TypeError):
            Combobox()

    def test_bad_params(self):
        with self.assertRaises(TypeError):
            Combobox(1)
        with self.assertRaises(TypeError):
            Combobox(self.root, values=[])
        with self.assertRaises(TypeError):
            Combobox(self.root, width=5.5)
        with self.assertRaises(TypeError):
            Combobox(self.root, show=False)

    def test_good_params(self):
        Combobox(self.root, width=20, show="*", values=("foo", "bar"),
                 command=lambda: print("Changed"),
                 validate=lambda: True).grid(row=0, column=0)

    def test_value(self):
        c = Combobox(self.root)
        c.grid(row=0, column=0)
        self.root.update()
        self.assertEqual(c.value, "")
        c.value = "Foo"
        self.assertEqual(c.value, "Foo")
        with self.assertRaises(TypeError):
            c.value = 1

    def test_values(self):
        c = Combobox(self.root)
        c.grid(row=0, column=0)
        self.root.update()
        self.assertEqual(c.values, ())
        c.values = ("Foo", )
        self.assertEqual(c.values, ("Foo", ))
        with self.assertRaises(TypeError):
            c.values = ["lol", "this", "doesn't", "work", "it", "must", "be",
                        "a", "tuple"]

    def test_enabled(self):
        c = Combobox(self.root)
        c.grid(row=0, column=0)
        self.root.update()
        self.assertTrue(c.enabled)
        c.enabled = False
        self.assertFalse(c.enabled)
        with self.assertRaises(TypeError):
            c.enabled = "lala"

    def test_read_only(self):
        c = Combobox(self.root)
        c.grid(row=0, column=0)
        self.root.update()
        self.assertFalse(c.read_only)
        c.read_only = True
        self.assertTrue(c.read_only)
        with self.assertRaises(TypeError):
            c.read_only = 1

    def test_right_click(self):
        c = Combobox(self.root)
        c.grid(row=0, column=0)
        self.root.update()
        c.enabled = False
        self.root.update()
        c._update_context_menu_states()
        self.root.update()
        c.enabled = True
        c.read_only = True
        self.root.update()
        c._update_context_menu_states()
        self.root.update()
        c.read_only = False
        c.select_all_contents()
        self.root.update()
        c._update_context_menu_states()
        self.root.update()
        c.copy_contents()
        self.root.update()
        c.cut_contents()
        self.root.update()
        c.delete_contents()
        self.root.update()
        c.paste_contents()

    def test_style(self):
        c = Combobox(self.root)
        c.grid(row=0, column=0)
        Style.define_style(Style.WidgetStyleRoots.Button, "Test",
                           background="red")
        c.apply_style("Test")
        self.assertEqual(c.cget("style"), "Test.TCombobox")
        self.root.update()
        with self.assertRaises(TypeError):
            c.apply_style([bool])


if __name__ == '__main__':
    unittest.main()
