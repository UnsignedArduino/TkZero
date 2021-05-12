"""
Test the TkZero.MainWindow module
"""

import unittest

from TkZero import Vector
from TkZero.Label import Label
from TkZeroUnitTest import TkTestCase


class MainWindowTest(TkTestCase):
    def test_title(self):
        self.root.title = "My title"
        self.assertEqual(self.root.title, "My title")
        with self.assertRaises(TypeError):
            self.root.title = 1

    def test_size(self):
        self.assertEqual(self.root.size, Vector.Size(width=200, height=200))
        self.root.size = Vector.Size(width=400, height=400)
        self.assertEqual(self.root.size, Vector.Size(width=400, height=400))
        self.root.size = (300, 300)
        self.assertEqual(self.root.size, Vector.Size(width=300, height=300))
        with self.assertRaises(TypeError):
            self.root.size = [400, 400]

    def test_position(self):
        self.root.position = Vector.Position(x=0, y=0)
        self.assertEqual(self.root.position, Vector.Position(x=0, y=0))
        self.root.position = (100, 100)
        self.assertEqual(self.root.position, Vector.Position(x=100, y=100))
        with self.assertRaises(TypeError):
            self.root.position = [0, 0]

    def test_minimized(self):
        self.root.minimize()
        self.root.update()
        self.assertTrue(self.root.is_minimized())

    def test_restored(self):
        self.root.minimize()
        self.root.update()
        self.root.restore()
        self.root.update()
        self.assertTrue(self.root.is_restored())

    def test_maximized(self):
        self.root.maximize()
        self.root.update()
        self.assertTrue(self.root.is_maximized())

    def test_fullscreen(self):
        self.root.full_screen(True)
        self.root.update()
        self.assertTrue(self.root.is_full_screen())
        with self.assertRaises(TypeError):
            self.root.full_screen("la")

    def test_binds(self):
        func = lambda: None
        self.root.bind_to_event("<<MyOwnSpecialEvent>>", func,
                                run_in_thread=True)
        binds = self.root.bind_to_event("<<MyOwnSpecialEvent>>")
        self.assertTrue(len(binds) > 0)
        with self.assertRaises(TypeError):
            self.root.bind_to_event(1234)
        with self.assertRaises(TypeError):
            self.root.bind_to_event("<<event>>", add=1)
        self.root.generate_event("<<MyOwnSpecialEvent>>")

    def test_enabled(self):
        self.assertTrue(self.root.enabled)
        Label(self.root).grid(row=0, column=0)
        Label(self.root).grid(row=1, column=0)
        self.root.update()
        self.root.enabled = False
        self.assertFalse(self.root.enabled)
        with self.assertRaises(TypeError):
            self.root.enabled = "False"

    def test_on_close(self):
        on_close_func = lambda: None
        self.root.on_close = on_close_func
        self.assertEqual(self.root.on_close, on_close_func)
        self.root.close()
        self.root.destroy()


if __name__ == "__main__":
    unittest.main()
