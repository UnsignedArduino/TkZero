"""
Test the TkZero.Scrollbar module
"""

import unittest


from TkZero.Listbox import Listbox
from TkZero.MainWindow import MainWindow
from TkZero.Scrollbar import Scrollbar, OrientModes


class LabelTest(unittest.TestCase):
    def test_no_params(self):
        root = MainWindow()
        root.update()
        with self.assertRaises(TypeError):
            Scrollbar()
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

    def test_enabled(self):
        root = MainWindow()
        root.update()
        s = Scrollbar(root)
        s.grid(row=0, column=0)
        root.update()
        self.assertTrue(s.enabled)
        s.enabled = False
        self.assertFalse(s.enabled)
        root.close()


if __name__ == '__main__':
    unittest.main()
