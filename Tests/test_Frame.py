"""
Test the TkZero.Frame module
"""

import unittest

from TkZero import Style
from TkZero.Frame import Frame
from TkZero.Label import Label
from TkZero.MainWindow import MainWindow


class FrameTest(unittest.TestCase):
    def test_no_params(self):
        root = MainWindow()
        root.update()
        with self.assertRaises(TypeError):
            Frame()
        root.update()
        root.close()

    def test_bad_params(self):
        root = MainWindow()
        root.update()
        with self.assertRaises(TypeError):
            Frame(parent=1)
        root.update()
        root.close()

    def test_good_params(self):
        root = MainWindow()
        root.update()
        Frame(root).grid(row=0, column=0)
        root.update()
        root.close()

    def test_width_height(self):
        root = MainWindow()
        root.update()
        f = Frame(root)
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
        f = Frame(root)
        f.grid(row=0, column=0)
        self.assertTrue(f.enabled)
        Label(f).grid(row=0, column=0)
        Label(f).grid(row=1, column=0)
        Frame(f).grid(row=2, column=0)
        root.update()
        f.enabled = False
        self.assertFalse(f.enabled)
        with self.assertRaises(TypeError):
            f.enabled = []
        root.close()

    def test_style(self):
        root = MainWindow()
        root.update()
        f = Frame(root)
        f.grid(row=0, column=0)
        Style.define_style(Style.WidgetStyleRoots.Frame, "Test", background="red")
        f.apply_style("Test")
        self.assertEqual(f.cget("style"), "Test.TFrame")
        root.update()
        with self.assertRaises(TypeError):
            f.apply_style(123456789)
        root.close()


if __name__ == '__main__':
    unittest.main()
