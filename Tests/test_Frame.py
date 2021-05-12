"""
Test the TkZero.Frame module
"""

import unittest

from TkZero import Style
from TkZero.Frame import Frame
from TkZero.Label import Label
from TkZeroUnitTest import TkTestCase


class FrameTest(TkTestCase):
    def test_no_params(self):
        with self.assertRaises(TypeError):
            Frame()
    def test_bad_params(self):
        with self.assertRaises(TypeError):
            Frame(parent=1)

    def test_good_params(self):
        Frame(self.root).grid(row=0, column=0)

    def test_width_height(self):
        f = Frame(self.root)
        f.grid(row=0, column=0)
        f.width = 500
        f.height = 200
        self.root.update()
        self.assertEqual(f.width, 500)
        self.assertEqual(f.height, 200)
        with self.assertRaises(TypeError):
            f.width = "la"
        with self.assertRaises(ValueError):
            f.width = 0
        with self.assertRaises(TypeError):
            f.height = "lo"
        with self.assertRaises(ValueError):
            f.height = -1

    def test_enabled(self):
        f = Frame(self.root)
        f.grid(row=0, column=0)
        self.assertTrue(f.enabled)
        Label(f).grid(row=0, column=0)
        Label(f).grid(row=1, column=0)
        Frame(f).grid(row=2, column=0)
        self.root.update()
        f.enabled = False
        self.assertFalse(f.enabled)
        with self.assertRaises(TypeError):
            f.enabled = []

    def test_style(self):
        f = Frame(self.root)
        f.grid(row=0, column=0)
        Style.define_style(Style.WidgetStyleRoots.Frame, "Test",
                           background="red")
        f.apply_style("Test")
        self.assertEqual(f.cget("style"), "Test.TFrame")
        self.root.update()
        with self.assertRaises(TypeError):
            f.apply_style(123456789)


if __name__ == '__main__':
    unittest.main()
