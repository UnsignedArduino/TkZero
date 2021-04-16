import unittest

from TkZero import Style
from TkZero.MainWindow import MainWindow
from TkZero.Spinbox import Spinbox


class SpinboxTest(unittest.TestCase):
    def test_no_params(self):
        root = MainWindow()
        root.update()
        with self.assertRaises(TypeError):
            Spinbox()
        root.update()
        root.close()

    def test_good_params(self):
        root = MainWindow()
        root.update()
        Spinbox(root, width=20, show="*", values=("foo", "bar")).grid(row=0, column=0)
        root.update()
        root.close()

    def test_value(self):
        root = MainWindow()
        root.update()
        s = Spinbox(root)
        s.grid(row=0, column=0)
        root.update()
        self.assertEqual(s.value, "")
        s.value = "Foo"
        self.assertEqual(s.value, "Foo")
        root.close()

    def test_values(self):
        root = MainWindow()
        root.update()
        s = Spinbox(root)
        s.grid(row=0, column=0)
        root.update()
        self.assertEqual(s.values, ())
        s.values = ("Foo", )
        self.assertEqual(s.values, ("Foo", ))
        root.close()

    def test_enabled(self):
        root = MainWindow()
        root.update()
        s = Spinbox(root)
        s.grid(row=0, column=0)
        root.update()
        self.assertTrue(s.enabled)
        s.enabled = False
        self.assertFalse(s.enabled)
        root.close()

    def test_read_only(self):
        root = MainWindow()
        root.update()
        s = Spinbox(root)
        s.grid(row=0, column=0)
        root.update()
        self.assertFalse(s.read_only)
        s.read_only = True
        self.assertTrue(s.read_only)
        root.close()

    def test_style(self):
        root = MainWindow()
        root.update()
        s = Spinbox(root)
        s.grid(row=0, column=0)
        Style.define_style(Style.WidgetStyleRoots.Button, "Test", background="red")
        s.apply_style("Test")
        self.assertEqual(s.cget("style"), "Test.TSpinbox")
        root.update()
        root.close()


if __name__ == '__main__':
    unittest.main()
