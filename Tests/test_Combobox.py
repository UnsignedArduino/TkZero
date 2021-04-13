import unittest
from TkZero.MainWindow import MainWindow
from TkZero.Combobox import Combobox
from TkZero import Style


class ComboboxTest(unittest.TestCase):
    def test_no_params(self):
        root = MainWindow()
        root.update()
        with self.assertRaises(TypeError):
            Combobox()
        root.update()
        root.close()

    def test_good_params(self):
        root = MainWindow()
        root.update()
        Combobox(root, width=20, show="*", values=("foo", "bar")).grid(row=0, column=0)
        root.update()
        root.close()

    def test_value(self):
        root = MainWindow()
        root.update()
        c = Combobox(root)
        c.grid(row=0, column=0)
        root.update()
        self.assertEqual(c.value, "")
        c.value = "Foo"
        self.assertEqual(c.value, "Foo")
        root.close()

    def test_values(self):
        root = MainWindow()
        root.update()
        c = Combobox(root)
        c.grid(row=0, column=0)
        root.update()
        self.assertEqual(c.values, ())
        c.values = ("Foo", )
        self.assertEqual(c.values, ("Foo", ))
        root.close()

    def test_enabled(self):
        root = MainWindow()
        root.update()
        c = Combobox(root)
        c.grid(row=0, column=0)
        root.update()
        self.assertTrue(c.enabled)
        c.enabled = False
        self.assertFalse(c.enabled)
        root.close()

    def test_read_only(self):
        root = MainWindow()
        root.update()
        c = Combobox(root)
        c.grid(row=0, column=0)
        root.update()
        self.assertFalse(c.read_only)
        c.read_only = True
        self.assertTrue(c.read_only)
        root.close()

    def test_style(self):
        root = MainWindow()
        root.update()
        c = Combobox(root)
        c.grid(row=0, column=0)
        Style.define_style(Style.WidgetStyleRoots.Button, "Test", background="red")
        c.apply_style("Test")
        self.assertEqual(c.cget("style"), "Test.TCombobox")
        root.update()
        root.close()


if __name__ == '__main__':
    unittest.main()
