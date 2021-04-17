"""
Test the TkZero.Menu module
"""

import unittest

from TkZero.MainWindow import MainWindow
from TkZero.Menu import Menu


class MenuTest(unittest.TestCase):
    def test_no_params(self):
        root = MainWindow()
        root.update()
        with self.assertRaises(TypeError):
            Menu()
        root.update()
        root.close()

    def test_good_params(self):
        root = MainWindow()
        root.update()
        Menu(root, is_menubar=True)
        root.update()
        root.close()


if __name__ == '__main__':
    unittest.main()
