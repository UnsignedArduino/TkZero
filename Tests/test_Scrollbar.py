"""
Test the TkZero.Scrollbar module
"""

import unittest

from TkZero.Entry import Entry
from TkZero.Listbox import Listbox
from TkZero.MainWindow import MainWindow
from TkZero.Scrollbar import Scrollbar, OrientModes


class ScrollbarTest(unittest.TestCase):
    def test_no_params(self):
        root = MainWindow()
        root.update()
        with self.assertRaises(TypeError):
            Scrollbar()
        root.update()
        root.close()

    def test_bad_params(self):
        root = MainWindow()
        root.update()
        with self.assertRaises(TypeError):
            Scrollbar(parent=1)
        with self.assertRaises(TypeError):
            Scrollbar(root, orientation=1)
        with self.assertRaises(TypeError):
            Scrollbar(root, widget=[])
        root.update()
        root.close()

    def test_good_params(self):
        root = MainWindow()
        root.update()
        l = Listbox(root)
        l.grid(row=0, column=0)
        Scrollbar(root, orientation=OrientModes.Vertical, widget=l).grid(row=0, column=1)
        root.update()
        root.close()

    def test_attaching(self):
        root = MainWindow()
        root.update()
        l = Listbox(root)
        l.grid(row=0, column=0)
        s = Scrollbar(root)
        s.grid(row=0, column=1)
        s.attach_to(l)
        root.update()
        with self.assertRaises(TypeError):
            s.attach_to("lol")
        e = Entry(root)
        e.grid(row=1, column=0)
        with self.assertRaises(ValueError):
            s.attach_to(e)
        s2 = Scrollbar(root, orientation=OrientModes.Horizontal)
        s2.grid(row=2, column=0)
        with self.assertRaises(ValueError):
            s.attach_to(e)
        root.close()

    def test_enabled(self):
        root = MainWindow()
        root.update()
        s = Scrollbar(root)
        s.grid(row=0, column=0)
        root.update()
        self.assertTrue(s.enabled)
        s.enabled = False
        self.assertFalse(s.enabled)
        with self.assertRaises(TypeError):
            s.enabled = "True"
        root.close()


if __name__ == '__main__':
    unittest.main()
