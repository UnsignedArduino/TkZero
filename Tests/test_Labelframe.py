"""
Test the TkZero.Labelframe module
"""

import unittest

from TkZero import Style
from TkZero.Label import Label
from TkZero.Labelframe import Labelframe
from TkZeroUnitTest import TkTestCase


class FrameTest(TkTestCase):
    def test_good_params(self):
        Labelframe(self.root, text="Options: ").grid(row=0, column=0)

    def test_width_height(self):
        f = Labelframe(self.root)
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
        f = Labelframe(self.root)
        f.grid(row=0, column=0)
        self.assertTrue(f.enabled)
        Label(f).grid(row=0, column=0)
        Label(f).grid(row=1, column=0)
        Labelframe(f).grid(row=2, column=0)
        self.root.update()
        f.enabled = False
        self.assertFalse(f.enabled)

    def test_hover(self):
        f = Labelframe(self.root)
        f.grid(row=0, column=0)
        self.root.update()
        self.assertEqual(type(f.hovering_over), bool)

    def test_text(self):
        f = Labelframe(self.root)
        f.grid(row=0, column=0)
        self.assertEqual(f.text, "")
        f.text = "Foo"
        self.assertEqual(f.text, "Foo")

    def test_style(self):
        f = Labelframe(self.root)
        f.grid(row=0, column=0)
        Style.define_style(Style.WidgetStyleRoots.Frame, "Test",
                           background="red")
        f.apply_style("Test")
        self.assertEqual(f.cget("style"), "Test.TLabelframe")
        self.root.update()


if __name__ == '__main__':
    unittest.main()
