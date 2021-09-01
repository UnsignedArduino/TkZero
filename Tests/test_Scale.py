"""
Test the TkZero.Scale module
"""

import unittest

from TkZero.Scale import Scale, OrientModes
from TkZeroUnitTest import TkTestCase


class ScaleTest(TkTestCase):
    def test_no_params(self):
        with self.assertRaises(TypeError):
            Scale()

    def test_bad_params(self):
        with self.assertRaises(TypeError):
            Scale(parent=1)
        with self.assertRaises(TypeError):
            Scale(self.root, length="5", minimum=0.0, maximum=5.0)
        with self.assertRaises(TypeError):
            Scale(self.root, length=5, minimum="0.0", maximum=5.0)
        with self.assertRaises(TypeError):
            Scale(self.root, length=5, minimum=0.0, maximum="5.0")
        with self.assertRaises(TypeError):
            Scale(self.root, length=5, minimum=0.0, maximum=5.0,
                  orientation=[])

    def test_good_params(self):
        Scale(self.root, orientation=OrientModes.Vertical, length=200,
              minimum=0.0, maximum=100.0).grid(row=0, column=1)

    def test_value(self):
        s = Scale(self.root, orientation=OrientModes.Vertical, length=200,
                  minimum=0.0, maximum=100.0)
        s.grid(row=0, column=0)
        self.root.update()
        self.assertEqual(s.value, 0)
        s.value = 25
        self.root.update()
        self.assertEqual(s.value, 25)
        with self.assertRaises(TypeError):
            s.value = "foo"

    def test_enabled(self):
        s = Scale(self.root, orientation=OrientModes.Vertical, length=200,
                  minimum=0.0, maximum=100.0)
        s.grid(row=0, column=0)
        self.root.update()
        self.assertTrue(s.enabled)
        s.enabled = False
        self.assertFalse(s.enabled)
        with self.assertRaises(TypeError):
            s.enabled = "pink cat"

    def test_hover(self):
        s = Scale(self.root, orientation=OrientModes.Vertical, length=200,
                  minimum=0.0, maximum=100.0)
        s.grid(row=0, column=0)
        self.root.update()
        self.assertEqual(type(s.hovering_over), bool)


if __name__ == '__main__':
    unittest.main()
