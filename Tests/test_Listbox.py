"""
Test the TkZero.Listbox module
"""

import unittest

from TkZero.Listbox import Listbox
from TkZero.MainWindow import MainWindow


class ListboxTest(unittest.TestCase):
    def test_no_params(self):
        root = MainWindow()
        root.update()
        with self.assertRaises(TypeError):
            Listbox()
        root.update()
        root.close()

    def test_bad_params(self):
        root = MainWindow()
        root.update()
        with self.assertRaises(TypeError):
            Listbox(parent=1)
        with self.assertRaises(TypeError):
            Listbox(root, values="")
        with self.assertRaises(TypeError):
            Listbox(root, select_mode=1)
        with self.assertRaises(TypeError):
            Listbox(root, height=2.5)
        with self.assertRaises(TypeError):
            Listbox(root, width="foo")
        root.update()
        root.close()

    def test_good_params(self):
        root = MainWindow()
        root.update()
        Listbox(root, width=20, height=10, values=["foo", "bar"],
                on_select=lambda: print("Selected"),
                on_double_click=lambda: print("Double click")
                ).grid(row=0, column=0)
        root.update()
        root.close()

    def test_selected(self):
        root = MainWindow()
        root.update()
        l = Listbox(root, values=["1", "2", "3"])
        l.grid(row=0, column=0)
        root.update()
        self.assertEqual(l.selected, ())
        l.selected = (0, )
        self.assertEqual(l.selected, (0, ))
        l.scroll_to(0)
        with self.assertRaises(TypeError):
            l.selected = []
        with self.assertRaises(TypeError):
            l.scroll_to("")
        root.close()

    def test_values(self):
        root = MainWindow()
        root.update()
        l = Listbox(root)
        l.grid(row=0, column=0)
        root.update()
        self.assertEqual(l.values, [])
        l.values = ["Foo"]
        self.assertEqual(l.values, ["Foo"])
        with self.assertRaises(TypeError):
            l.values = ()
        root.close()

    def test_enabled(self):
        root = MainWindow()
        root.update()
        l = Listbox(root)
        l.grid(row=0, column=0)
        root.update()
        self.assertTrue(l.enabled)
        l.enabled = False
        self.assertFalse(l.enabled)
        with self.assertRaises(TypeError):
            l.enabled = "boo"
        root.close()


if __name__ == '__main__':
    unittest.main()
