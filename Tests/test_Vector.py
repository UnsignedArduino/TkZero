"""
Test the TkZero.Vector module
"""

import unittest

from TkZero import Vector


class VectorTest(unittest.TestCase):
    def test_size_vector_initiate(self):
        size = Vector.Size(width=100, height=50)
        self.assertEqual(size.width, 100)
        self.assertEqual(size.height, 50)

    def test_size_vector_exceptions(self):
        size = Vector.Size(width=0, height=0)
        with self.assertRaises(AttributeError):
            size.width = "foo"
        with self.assertRaises(AttributeError):
            size.notAnAttribute += 1
        with self.assertRaises(AttributeError):
            size.width += 10
        with self.assertRaises(AttributeError):
            size.height *= 2

    def test_position_vector_initiate(self):
        pos = Vector.Position(x=0, y=0)
        self.assertEqual(pos.x, 0)
        self.assertEqual(pos.y, 0)

    def test_position_vector_exceptions(self):
        pos = Vector.Position(x=4, y=4)
        with self.assertRaises(AttributeError):
            pos.x = "bar"
        with self.assertRaises(AttributeError):
            pos.definitelyNotAnAttribute -= 1
        with self.assertRaises(AttributeError):
            pos.x += 10
        with self.assertRaises(AttributeError):
            pos.y -= 10


if __name__ == "__main__":
    unittest.main()
