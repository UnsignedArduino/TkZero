"""
Test the TkZero.Window.MainWindow module
"""

import unittest
from TkZero.Window.MainWindow import MainWindow
from TkZero import Vector


class MainWindowTest(unittest.TestCase):
    def test_title(self):
        root = MainWindow()
        root.update()
        root.title = "My title"
        self.assertEqual(root.title, "My title")
        root.close()

    def test_size(self):
        root = MainWindow()
        root.update()
        self.assertEqual(root.size, Vector.Size(width=200, height=200))
        root.size = Vector.Size(width=400, height=400)
        self.assertEqual(root.size, Vector.Size(width=400, height=400))
        root.close()

    def test_position(self):
        root = MainWindow()
        root.update()
        root.position = Vector.Position(x=0, y=0)
        root.update()
        self.assertEqual(root.position, Vector.Position(x=0, y=0))
        root.close()

    def test_minimized(self):
        root = MainWindow()
        root.update()
        root.minimize()
        root.update()
        self.assertTrue(root.is_minimized())
        root.close()

    def test_restored(self):
        root = MainWindow()
        root.update()
        root.minimize()
        root.update()
        root.restore()
        root.update()
        self.assertTrue(root.is_restored())
        root.close()

    def test_maximized(self):
        root = MainWindow()
        root.update()
        root.maximize()
        root.update()
        self.assertTrue(root.is_maximized())
        root.close()

    def test_on_close(self):
        root = MainWindow()
        root.update()
        on_close_func = lambda: None
        root.on_close = on_close_func
        self.assertEqual(root.on_close, on_close_func)
        root.close()
        root.destroy()


if __name__ == "__main__":
    unittest.main()
