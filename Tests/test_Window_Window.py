"""
Test the TkZero.Window.Window module
"""

import unittest
from TkZero.Window.MainWindow import MainWindow
from TkZero.Window.Window import Window
from TkZero import Vector


class MainWindowTest(unittest.TestCase):
    def test_title(self):
        root = MainWindow()
        root.minimize()
        window = Window(root)
        window.title = "My title"
        window.update()
        self.assertEqual(window.title, "My title")
        root.close()

    def test_size(self):
        root = MainWindow()
        root.minimize()
        window = Window(root)
        window.update()
        self.assertEqual(window.size, Vector.Size(width=200, height=200))
        window.size = Vector.Size(width=400, height=400)
        window.update()
        self.assertEqual(window.size, Vector.Size(width=400, height=400))
        root.close()

    def test_position(self):
        root = MainWindow()
        root.minimize()
        window = Window(root)
        window.position = Vector.Position(x=0, y=0)
        window.update()
        self.assertEqual(window.position, Vector.Position(x=0, y=0))
        root.close()

    def test_minimized(self):
        root = MainWindow()
        root.minimize()
        window = Window(root)
        window.minimize()
        window.update()
        self.assertTrue(window.is_minimized())
        root.close()

    def test_restored(self):
        root = MainWindow()
        root.minimize()
        window = Window(root)
        window.update()
        window.minimize()
        window.update()
        window.restore()
        window.update()
        self.assertTrue(window.is_restored())
        root.close()

    def test_maximized(self):
        root = MainWindow()
        root.minimize()
        window = Window(root)
        window.update()
        window.maximize()
        window.update()
        self.assertTrue(window.is_maximized())
        root.close()

    def test_on_close(self):
        root = MainWindow()
        root.minimize()
        window = Window(root)
        on_close_func = lambda: None
        window.on_close = on_close_func
        self.assertEqual(window.on_close, on_close_func)
        window.close()
        window.destroy()
        root.close()


if __name__ == "__main__":
    unittest.main()