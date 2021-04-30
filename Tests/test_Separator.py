"""
Test the TkZero.Scrollbar module
"""

import unittest

from TkZero.MainWindow import MainWindow
from TkZero.Separator import Separator, OrientModes


class SeparatorTest(unittest.TestCase):
    def test_no_params(self):
        root = MainWindow()
        root.update()
        with self.assertRaises(TypeError):
            Separator()
        root.update()
        root.close()

    def test_bad_params(self):
        root = MainWindow()
        root.update()
        with self.assertRaises(TypeError):
            Separator(parent=1)
        with self.assertRaises(TypeError):
            Separator(root, orientation=1)
        root.update()
        root.close()

    def test_good_params(self):
        root = MainWindow()
        root.update()
        Separator(root, orientation=OrientModes.Vertical).grid(row=0, column=1)
        root.update()
        root.close()

    def test_enabled(self):
        root = MainWindow()
        root.update()
        s = Separator(root)
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
