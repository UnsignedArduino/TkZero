"""
Test the TkZero.Labelframe module
"""

import unittest

from TkZero import Style
from TkZero.Label import Label
from TkZero.Labelframe import Labelframe
from TkZero.MainWindow import MainWindow


class FrameTest(unittest.TestCase):
    def test_no_params(self):
        root = MainWindow()
        root.update()
        with self.assertRaises(TypeError):
            Labelframe()
        root.update()
        root.close()

    def test_bad_params(self):
        root = MainWindow()
        root.update()
        with self.assertRaises(TypeError):
            Labelframe(parent=1)
        with self.assertRaises(TypeError):
            Labelframe(root, text=5)
        root.update()
        root.close()

    def test_good_params(self):
        root = MainWindow()
        root.update()
        Labelframe(root, text="Options: ").grid(row=0, column=0)
        root.update()
        root.close()

    def test_width_height(self):
        root = MainWindow()
        root.update()
        f = Labelframe(root)
        f.grid(row=0, column=0)
        f.width = 500
        f.height = 200
        root.update()
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
        root.close()

    def test_enabled(self):
        root = MainWindow()
        root.update()
        f = Labelframe(root)
        f.grid(row=0, column=0)
        self.assertTrue(f.enabled)
        Label(f).grid(row=0, column=0)
        Label(f).grid(row=1, column=0)
        Labelframe(f).grid(row=2, column=0)
        root.update()
        f.enabled = False
        self.assertFalse(f.enabled)
        with self.assertRaises(TypeError):
            f.enabled = []
        root.close()

    def test_text(self):
        root = MainWindow()
        root.update()
        f = Labelframe(root)
        f.grid(row=0, column=0)
        self.assertEqual(f.text, "")
        f.text = "Foo"
        self.assertEqual(f.text, "Foo")
        with self.assertRaises(TypeError):
            f.text = 42
        root.close()

    def test_style(self):
        root = MainWindow()
        root.update()
        f = Labelframe(root)
        f.grid(row=0, column=0)
        Style.define_style(Style.WidgetStyleRoots.Frame, "Test", background="red")
        f.apply_style("Test")
        self.assertEqual(f.cget("style"), "Test.TLabelframe")
        root.update()
        with self.assertRaises(TypeError):
            f.apply_style(123456789)
        root.close()


if __name__ == '__main__':
    unittest.main()
