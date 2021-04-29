"""
Test the TkZero.Platform module
"""

import tkinter as tk
import unittest

from TkZero import Platform


class PlatformTest(unittest.TestCase):
    def test_on_platform(self):
        root = tk.Tk()
        root.update()
        Platform.on_platform(root, Platform.WindowingSystem.WIN32)
        Platform.on_platform(root, Platform.WindowingSystem.X11)
        Platform.on_platform(root, Platform.WindowingSystem.AQUA)
        with self.assertRaises(TypeError):
            Platform.on_platform(1)
        root.destroy()

    def test_on_x11(self):
        root = tk.Tk()
        root.update()
        self.assertEqual(Platform.on_platform(root, Platform.WindowingSystem.X11), Platform.on_x11(root))
        with self.assertRaises(TypeError):
            Platform.on_x11(1)
        root.destroy()

    def test_on_win32(self):
        root = tk.Tk()
        root.update()
        self.assertEqual(Platform.on_platform(root, Platform.WindowingSystem.WIN32), Platform.on_win32(root))
        with self.assertRaises(TypeError):
            Platform.on_win32(1)
        root.destroy()

    def test_on_aqua(self):
        root = tk.Tk()
        root.update()
        self.assertEqual(Platform.on_platform(root, Platform.WindowingSystem.AQUA), Platform.on_aqua(root))
        with self.assertRaises(TypeError):
            Platform.on_aqua(1)
        root.destroy()


if __name__ == "__main__":
    unittest.main()
