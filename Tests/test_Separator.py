"""
Test the TkZero.Scrollbar module
"""

import unittest

from TkZero.Separator import Separator, OrientModes
from TkZeroUnitTest import TkTestCase


class SeparatorTest(TkTestCase):
    def test_no_params(self):
        with self.assertRaises(TypeError):
            Separator()

    def test_bad_params(self):
        with self.assertRaises(TypeError):
            Separator(parent=1)
        with self.assertRaises(TypeError):
            Separator(self.root, orientation=1)

    def test_good_params(self):
        Separator(self.root,
                  orientation=OrientModes.Vertical).grid(row=0, column=1)

    def test_enabled(self):
        s = Separator(self.root)
        s.grid(row=0, column=0)
        self.root.update()
        self.assertTrue(s.enabled)
        s.enabled = False
        self.assertFalse(s.enabled)
        with self.assertRaises(TypeError):
            s.enabled = "True"

    def test_hover(self):
        s = Separator(self.root)
        s.grid(row=0, column=0)
        self.root.update()
        self.assertEqual(type(s.hovering_over), bool)


if __name__ == '__main__':
    unittest.main()
