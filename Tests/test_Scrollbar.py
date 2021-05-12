"""
Test the TkZero.Scrollbar module
"""

import unittest

from TkZero.Entry import Entry
from TkZero.Listbox import Listbox
from TkZero.Scrollbar import Scrollbar, OrientModes
from TkZeroUnitTest import TkTestCase


class ScrollbarTest(TkTestCase):
    def test_no_params(self):
        with self.assertRaises(TypeError):
            Scrollbar()

    def test_bad_params(self):
        with self.assertRaises(TypeError):
            Scrollbar(parent=1)
        with self.assertRaises(TypeError):
            Scrollbar(self.root, orientation=1)
        with self.assertRaises(TypeError):
            Scrollbar(self.root, widget=[])

    def test_good_params(self):
        l = Listbox(self.root)
        l.grid(row=0, column=0)
        Scrollbar(self.root, orientation=OrientModes.Vertical,
                  widget=l).grid(row=0, column=1)

    def test_attaching(self):
        l = Listbox(self.root)
        l.grid(row=0, column=0)
        s = Scrollbar(self.root)
        s.grid(row=0, column=1)
        s.attach_to(l)
        self.root.update()
        with self.assertRaises(TypeError):
            s.attach_to("lol")
        e = Entry(self.root)
        e.grid(row=1, column=0)
        with self.assertRaises(ValueError):
            s.attach_to(e)
        s2 = Scrollbar(self.root, orientation=OrientModes.Horizontal)
        s2.grid(row=2, column=0)
        with self.assertRaises(ValueError):
            s.attach_to(e)

    def test_enabled(self):
        s = Scrollbar(self.root)
        s.grid(row=0, column=0)
        self.root.update()
        self.assertTrue(s.enabled)
        s.enabled = False
        self.assertFalse(s.enabled)
        with self.assertRaises(TypeError):
            s.enabled = "True"


if __name__ == '__main__':
    unittest.main()
