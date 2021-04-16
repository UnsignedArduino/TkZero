import unittest

from TkZero.MainWindow import MainWindow
from TkZero.Scale import Scale, OrientModes


class ScaleTest(unittest.TestCase):
    def test_no_params(self):
        root = MainWindow()
        root.update()
        with self.assertRaises(TypeError):
            Scale()
        root.update()
        root.close()

    def test_good_params(self):
        root = MainWindow()
        root.update()
        Scale(root, orientation=OrientModes.Vertical, length=200, minimum=0.0, maximum=100.0).grid(row=0, column=1)
        root.update()
        root.close()

    def test_value(self):
        root = MainWindow()
        root.update()
        s = Scale(root, orientation=OrientModes.Vertical, length=200, minimum=0.0, maximum=100.0)
        s.grid(row=0, column=0)
        root.update()
        self.assertEqual(s.value, 0)
        s.value = 25
        root.update()
        self.assertEqual(s.value, 25)
        root.close()

    def test_enabled(self):
        root = MainWindow()
        root.update()
        s = Scale(root, orientation=OrientModes.Vertical, length=200, minimum=0.0, maximum=100.0)
        s.grid(row=0, column=0)
        root.update()
        self.assertTrue(s.enabled)
        s.enabled = False
        self.assertFalse(s.enabled)
        root.close()


if __name__ == '__main__':
    unittest.main()
