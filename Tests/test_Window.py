"""
Test the TkZero.Window module
"""

import unittest

from TkZero import Vector
from TkZero.Label import Label
from TkZero.Window import Window
from TkZeroUnitTest import TkTestCase


class MainWindowTest(TkTestCase):
    def test_no_params(self):
        with self.assertRaises(TypeError):
            Window()

    def test_bad_params(self):
        with self.assertRaises(TypeError):
            Window(parent=1)

    def test_title(self):
        window = Window(self.root)
        window.title = "My title"
        window.update()
        self.assertEqual(window.title, "My title")
        with self.assertRaises(TypeError):
            window.title = 1234567890

    def test_size(self):
        window = Window(self.root)
        window.update()
        self.assertEqual(window.size, Vector.Size(width=200, height=200))
        window.size = Vector.Size(width=400, height=400)
        self.assertEqual(window.size, Vector.Size(width=400, height=400))
        window.size = (120, 120)
        self.assertEqual(window.size, Vector.Size(width=120, height=120))
        with self.assertRaises(TypeError):
            window.size = [200, 100]

    def test_position(self):
        window = Window(self.root)
        window.position = Vector.Position(x=0, y=0)
        self.assertEqual(window.position, Vector.Position(x=0, y=0))
        window.position = (100, 100)
        self.assertEqual(window.position, Vector.Position(x=100, y=100))
        with self.assertRaises(TypeError):
            window.position = [0, 0]

    def test_minimized(self):
        window = Window(self.root)
        window.minimized = True
        window.update()
        self.assertTrue(window.minimized)
        window.minimized = False
        window.update()
        self.assertFalse(window.minimized)
        with self.assertRaises(TypeError):
            window.minimized = "True"

    def test_restored(self):
        window = Window(self.root)
        window.update()
        window.minimized = True
        window.update()
        window.restored = True
        window.update()
        self.assertTrue(window.restored)
        window.restored = False
        window.update()
        self.assertFalse(window.restored)
        with self.assertRaises(TypeError):
            window.restored = "False"

    def test_maximized(self):
        window = Window(self.root)
        window.update()
        window.maximized = True
        window.update()
        self.assertTrue(window.maximized)
        window.maximized = False
        window.update()
        self.assertFalse(window.maximized)
        with self.assertRaises(TypeError):
            window.maximized = "True"

    def test_fullscreen(self):
        window = Window(self.root)
        window.full_screen = True
        window.update()
        self.assertTrue(window.full_screen)
        window.full_screen = False
        window.update()
        self.assertFalse(window.full_screen)
        with self.assertRaises(TypeError):
            window.full_screen = "la"

    def test_binds(self):
        window = Window(self.root)
        func = lambda: None
        window.bind_to_event("<<MyOwnSpecialEvent>>", func, run_in_thread=True)
        binds = window.bind_to_event("<<MyOwnSpecialEvent>>")
        self.assertTrue(len(binds) > 0)
        with self.assertRaises(TypeError):
            window.bind_to_event(1234)
        with self.assertRaises(TypeError):
            window.bind_to_event("<<event>>", add=1)
        self.root.generate_event("<<MyOwnSpecialEvent>>")

    def test_enabled(self):
        window = Window(self.root)
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

    def test_hover(self):
        window = Window(self.root)
        window.lift()
        window.update()
        self.assertEqual(type(window.hovering_over), bool)

    def test_on_close(self):
        window = Window(self.root)
        on_close_func = lambda: None
        window.on_close = on_close_func
        self.assertEqual(window.on_close, on_close_func)
        window.close()
        window.destroy()


if __name__ == "__main__":
    unittest.main()
