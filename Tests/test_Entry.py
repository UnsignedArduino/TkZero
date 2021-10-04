"""
Test the TkZero.Entry module
"""
import tkinter as tk
import unittest

from TkZero import Style
from TkZero.Entry import Entry
from TkZeroUnitTest import TkTestCase


class EntryTest(TkTestCase):
    def test_good_params(self):
        Entry(self.root, width=20, show="*", validate=lambda: True,
              command=lambda: print("Changed")).grid(row=0, column=0)

    def test_value(self):
        e = Entry(self.root)
        e.grid(row=0, column=0)
        self.root.update()
        self.assertEqual(e.value, "")
        e.value = "Foo"
        self.assertEqual(e.value, "Foo")

    def test_enabled(self):
        e = Entry(self.root)
        e.grid(row=0, column=0)
        self.root.update()
        self.assertTrue(e.enabled)
        e.enabled = False
        self.assertFalse(e.enabled)

    def test_read_only(self):
        e = Entry(self.root)
        e.grid(row=0, column=0)
        self.root.update()
        self.assertFalse(e.read_only)
        e.read_only = True
        self.assertTrue(e.read_only)

    def test_hover(self):
        e = Entry(self.root)
        e.grid(row=0, column=0)
        self.root.update()
        self.assertEqual(type(e.hovering_over), bool)

    def test_right_click(self):
        # Also fails randomly in GitHub actions
        try:
            e = Entry(self.root)
            e.grid(row=0, column=0)
            self.root.update()
            e.enabled = False
            self.root.update()
            e._update_context_menu_states()
            self.root.update()
            e.enabled = True
            e.read_only = True
            self.root.update()
            e._update_context_menu_states()
            self.root.update()
            e.read_only = False
            e.select_all_contents()
            self.root.update()
            e._update_context_menu_states()
            self.root.update()
            e.copy_contents()
            self.root.update()
            e.cut_contents()
            self.root.update()
            e.delete_contents()
            self.root.update()
            e.paste_contents()
        except tk.TclError:
            pass

    def test_style(self):
        e = Entry(self.root)
        e.grid(row=0, column=0)
        Style.define_style(Style.WidgetStyleRoots.Button, "Test",
                           background="red")
        e.apply_style("Test")
        self.assertEqual(e.cget("style"), "Test.TEntry")
        self.root.update()


if __name__ == '__main__':
    unittest.main()
