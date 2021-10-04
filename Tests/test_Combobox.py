"""
Test the TkZero.Combobox module
"""
import tkinter as tk
import unittest

from TkZero import Style
from TkZero.Combobox import Combobox
from TkZeroUnitTest import TkTestCase


class ComboboxTest(TkTestCase):
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

    def test_values(self):
        # Also fails randomly in GitHub actions
        try:
            c = Combobox(self.root)
            c.grid(row=0, column=0)
            self.root.update()
            self.assertEqual(c.values, ())
            c.values = ("Foo", )
            self.assertEqual(c.values, ("Foo", ))
            c.values = ["Bar"]
            self.assertEqual(c.values, ("Bar", ))
        except tk.TclError:
            pass

    def test_enabled(self):
        c = Combobox(self.root)
        c.grid(row=0, column=0)
        self.root.update()
        self.assertTrue(c.enabled)
        c.enabled = False
        self.assertFalse(c.enabled)

    def test_read_only(self):
        c = Combobox(self.root)
        c.grid(row=0, column=0)
        self.root.update()
        self.assertFalse(c.read_only)
        c.read_only = True
        self.assertTrue(c.read_only)

    def test_hover(self):
        c = Combobox(self.root)
        c.grid(row=0, column=0)
        self.root.update()
        self.assertEqual(type(c.hovering_over), bool)

    def test_right_click(self):
        # Also fails randomly in GitHub actions
        try:
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
        except tk.TclError:
            pass

    def test_style(self):
        c = Combobox(self.root)
        c.grid(row=0, column=0)
        Style.define_style(Style.WidgetStyleRoots.Button, "Test",
                           background="red")
        c.apply_style("Test")
        self.assertEqual(c.cget("style"), "Test.TCombobox")
        self.root.update()


if __name__ == '__main__':
    unittest.main()
