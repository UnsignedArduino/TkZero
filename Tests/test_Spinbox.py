"""
Test the TkZero.Spinbox module
"""
import tkinter as tk
import unittest

from TkZero import Style
from TkZero.Spinbox import Spinbox
from TkZeroUnitTest import TkTestCase


class SpinboxTest(TkTestCase):
    def test_no_params(self):
        with self.assertRaises(TypeError):
            Spinbox()

    def test_bad_params(self):
        with self.assertRaises(TypeError):
            Spinbox(parent=1)
        with self.assertRaises(TypeError):
            Spinbox(self.root, values={"this", "doesn't", "work"})
        with self.assertRaises(TypeError):
            Spinbox(self.root, width=5.5)
        with self.assertRaises(TypeError):
            Spinbox(self.root, show=1)

    def test_good_params(self):
        Spinbox(self.root, width=20, show="*", values=("foo", "bar"),
                validate=lambda: True,
                command=lambda: print("Changed")).grid(row=0, column=0)

    def test_value(self):
        s = Spinbox(self.root)
        s.grid(row=0, column=0)
        self.root.update()
        self.assertEqual(s.value, "")
        s.value = "Foo"
        self.assertEqual(s.value, "Foo")
        with self.assertRaises(TypeError):
            s.value = ("la", )

    def test_values(self):
        s = Spinbox(self.root)
        s.grid(row=0, column=0)
        self.root.update()
        self.assertEqual(s.values, ())
        s.values = ("Foo", )
        self.assertEqual(s.values, ("Foo", ))
        s.values = ["Foo"]
        self.assertEqual(s.values, ("Foo",))
        with self.assertRaises(TypeError):
            s.values = {}

    def test_enabled(self):
        s = Spinbox(self.root)
        s.grid(row=0, column=0)
        self.root.update()
        self.assertTrue(s.enabled)
        s.enabled = False
        self.assertFalse(s.enabled)
        with self.assertRaises(TypeError):
            s.enabled = "True"

    def test_read_only(self):
        s = Spinbox(self.root)
        s.grid(row=0, column=0)
        self.root.update()
        self.assertFalse(s.read_only)
        s.read_only = True
        self.assertTrue(s.read_only)
        with self.assertRaises(TypeError):
            s.read_only = "False"

    def test_hover(self):
        s = Spinbox(self.root)
        s.grid(row=0, column=0)
        self.root.update()
        self.assertEqual(type(s.hovering_over), bool)

    def test_right_click(self):
        # Also fails in GitHub actions
        try:
            s = Spinbox(self.root)
            s.grid(row=0, column=0)
            self.root.update()
            s.enabled = False
            self.root.update()
            s._update_context_menu_states()
            self.root.update()
            s.enabled = True
            s.read_only = True
            self.root.update()
            s._update_context_menu_states()
            self.root.update()
            s.read_only = False
            s.select_all_contents()
            self.root.update()
            s._update_context_menu_states()
            self.root.update()
            s.copy_contents()
            self.root.update()
            s.cut_contents()
            self.root.update()
            s.delete_contents()
            self.root.update()
            s.paste_contents()
        except tk.TclError:
            pass

    def test_style(self):
        s = Spinbox(self.root)
        s.grid(row=0, column=0)
        Style.define_style(Style.WidgetStyleRoots.Button, "Test",
                           background="red")
        s.apply_style("Test")
        self.assertEqual(s.cget("style"), "Test.TSpinbox")


if __name__ == '__main__':
    unittest.main()
