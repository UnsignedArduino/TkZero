"""
Test the TkZero.Platform module
"""

import unittest
from TkZero import Platform
import tkinter as tk


class PlatformTest(unittest.TestCase):
    def test_on_x11(self):
        root = tk.Tk()
        root.update()
        self.assertEqual(Platform.on_platform(root, Platform.WindowingSystem.X11), Platform.on_x11(root))
        root.destroy()

    def test_on_win32(self):
        root = tk.Tk()
        root.update()
        self.assertEqual(Platform.on_platform(root, Platform.WindowingSystem.WIN32), Platform.on_win32(root))
        root.destroy()

    def test_on_aqua(self):
        root = tk.Tk()
        root.update()
        self.assertEqual(Platform.on_platform(root, Platform.WindowingSystem.AQUA), Platform.on_aqua(root))
        root.destroy()


if __name__ == "__main__":
    unittest.main()
