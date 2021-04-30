"""
Test the TkZero.Window module
"""

import unittest

from TkZero import Vector
from TkZero.Label import Label
from TkZero.MainWindow import MainWindow
from TkZero.Window import Window


class MainWindowTest(unittest.TestCase):
    def test_no_params(self):
        root = MainWindow()
        root.minimize()
        with self.assertRaises(TypeError):
            Window()
        root.close()

    def test_bad_params(self):
        root = MainWindow()
        root.minimize()
        with self.assertRaises(TypeError):
            Window(parent=1)
        root.close()

    def test_title(self):
        root = MainWindow()
        root.minimize()
        window = Window(root)
        window.title = "My title"
        window.update()
        self.assertEqual(window.title, "My title")
        with self.assertRaises(TypeError):
            window.title = 1234567890
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
        with self.assertRaises(TypeError):
            window.size = (100, 100)
        root.close()

    def test_position(self):
        root = MainWindow()
        root.minimize()
        window = Window(root)
        window.position = Vector.Position(x=0, y=0)
        window.update()
        self.assertEqual(window.position, Vector.Position(x=0, y=0))
        with self.assertRaises(TypeError):
            window.position = (0, 0)
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

    def test_fullscreen(self):
        root = MainWindow()
        root.update()
        window = Window(root)
        window.full_screen(True)
        window.update()
        self.assertTrue(window.is_full_screen())
        with self.assertRaises(TypeError):
            window.full_screen("la")
        root.close()

    def test_binds(self):
        root = MainWindow()
        root.minimize()
        window = Window(root)
        func = lambda: None
        window.bind_to_event("<<MyOwnSpecialEvent>>", func, run_in_thread=True)
        binds = window.bind_to_event("<<MyOwnSpecialEvent>>")
        self.assertTrue(len(binds) > 0)
        with self.assertRaises(TypeError):
            window.bind_to_event(1234)
        with self.assertRaises(TypeError):
            window.bind_to_event("<<event>>", add=1)
        root.generate_event("<<MyOwnSpecialEvent>>")
        root.close()

    def test_enabled(self):
        root = MainWindow()
        root.lift()
        root.update()
        window = Window(root)
        window.lift()
        window.update()
        self.assertTrue(window.enabled)
        Label(window).grid(row=0, column=0)
        Label(window).grid(row=1, column=0)
        window.update()
        window.enabled = False
        self.assertFalse(window.enabled)
        with self.assertRaises(TypeError):
            window.enabled = "True"
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
