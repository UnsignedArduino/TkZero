"""
Test the TkZero.Listbox module
"""

import unittest

from TkZero.Listbox import Listbox
from TkZeroUnitTest import TkTestCase


class ListboxTest(TkTestCase):
    def test_no_params(self):
        with self.assertRaises(TypeError):
            Listbox()

    def test_bad_params(self):
        with self.assertRaises(TypeError):
            Listbox(parent=1)
        with self.assertRaises(TypeError):
            Listbox(self.root, values="")
        with self.assertRaises(TypeError):
            Listbox(self.root, select_mode=1)
        with self.assertRaises(TypeError):
            Listbox(self.root, height=2.5)
        with self.assertRaises(TypeError):
            Listbox(self.root, width="foo")

    def test_good_params(self):
        Listbox(self.root, width=20, height=10, values=["foo", "bar"],
                on_select=lambda: print("Selected"),
                on_double_click=lambda: print("Double click")
                ).grid(row=0, column=0)

    def test_selected(self):
        l = Listbox(self.root, values=["1", "2", "3"])
        l.grid(row=0, column=0)
        self.root.update()
        self.assertEqual(l.selected, ())
        l.selected = (0, )
        self.assertEqual(l.selected, (0, ))
        l.scroll_to(0)
        with self.assertRaises(TypeError):
            l.selected = []
        with self.assertRaises(TypeError):
            l.scroll_to("")
        self.root.close()

    def test_values(self):
        l = Listbox(self.root)
        l.grid(row=0, column=0)
        self.root.update()
        self.assertEqual(l.values, [])
        l.values = ["Foo"]
        self.assertEqual(l.values, ["Foo"])
        with self.assertRaises(TypeError):
            l.values = ()

    def test_enabled(self):
        l = Listbox(self.root)
        l.grid(row=0, column=0)
        self.root.update()
        self.assertTrue(l.enabled)
        l.enabled = False
        self.assertFalse(l.enabled)
        with self.assertRaises(TypeError):
            l.enabled = "boo"


if __name__ == '__main__':
    unittest.main()
