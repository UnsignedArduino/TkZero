"""
Test the TkZero.Progressbar module
"""

import unittest

from TkZero.MainWindow import MainWindow
from TkZero.Progressbar import Progressbar, OrientModes, ProgressModes


class ProgressbarTest(unittest.TestCase):
    def test_no_params(self):
        root = MainWindow()
        root.update()
        with self.assertRaises(TypeError):
            Progressbar()
        root.update()
        root.close()

    def test_good_params(self):
        root = MainWindow()
        root.update()
        Progressbar(root, orientation=OrientModes.Vertical, mode=ProgressModes.Determinate,
                    length=200).grid(row=0, column=1)
        root.update()
        root.close()

    def test_value(self):
        root = MainWindow()
        root.update()
        p = Progressbar(root, orientation=OrientModes.Vertical, mode=ProgressModes.Determinate, length=200)
        p.grid(row=0, column=0)
        p.maximum = 100
        root.update()
        self.assertEqual(p.value, 0)
        self.assertEqual(p.maximum, 100)
        p.value = 25
        root.update()
        self.assertEqual(p.value, 25)
        root.close()

    def test_indeterminate(self):
        root = MainWindow()
        root.update()
        p = Progressbar(root, orientation=OrientModes.Horizontal, mode=ProgressModes.Indeterminate, length=200)
        p.grid(row=0, column=0)
        p.start()
        root.update()
        root.after(ms=2000, func=root.close)
        root.mainloop()

    def test_enabled(self):
        root = MainWindow()
        root.update()
        p = Progressbar(root, orientation=OrientModes.Vertical, mode=ProgressModes.Determinate, length=200)
        p.grid(row=0, column=0)
        root.update()
        self.assertTrue(p.enabled)
        p.enabled = False
        self.assertFalse(p.enabled)
        root.close()


if __name__ == '__main__':
    unittest.main()
