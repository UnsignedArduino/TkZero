"""
Test the TkZero.Platform module
"""

import unittest

from TkZero import Platform
from TkZeroUnitTest import TkTestCase


class PlatformTest(TkTestCase):
    def test_on_platform(self):
        Platform.on_platform(self.root, Platform.WindowingSystem.WIN32)
        Platform.on_platform(self.root, Platform.WindowingSystem.X11)
        Platform.on_platform(self.root, Platform.WindowingSystem.AQUA)

    def test_on_x11(self):
        self.assertEqual(
            Platform.on_platform(self.root, Platform.WindowingSystem.X11),
            Platform.on_x11(self.root)
        )

    def test_on_win32(self):
        self.assertEqual(
            Platform.on_platform(self.root, Platform.WindowingSystem.WIN32),
            Platform.on_win32(self.root)
        )

    def test_on_aqua(self):
        self.assertEqual(
            Platform.on_platform(self.root, Platform.WindowingSystem.AQUA),
            Platform.on_aqua(self.root)
        )


if __name__ == "__main__":
    unittest.main()
