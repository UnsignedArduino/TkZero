import unittest

from TkZero.Listbox import Listbox
from TkZero.MainWindow import MainWindow


class ListboxTest(unittest.TestCase):
    def test_no_params(self):
        root = MainWindow()
        root.update()
        with self.assertRaises(TypeError):
            Listbox()
        root.update()
        root.close()

    def test_good_params(self):
        root = MainWindow()
        root.update()
        Listbox(root, width=20, height=10, values=["foo", "bar"]).grid(row=0, column=0)
        root.update()
        root.close()

    def test_selected(self):
        root = MainWindow()
        root.update()
        l = Listbox(root, values=["1", "2", "3"])
        l.grid(row=0, column=0)
        root.update()
        self.assertEqual(l.selected, ())
        l.selected = (0, )
        self.assertEqual(l.selected, (0, ))
        root.close()

    def test_values(self):
        root = MainWindow()
        root.update()
        l = Listbox(root)
        l.grid(row=0, column=0)
        root.update()
        self.assertEqual(l.values, [])
        l.values = ["Foo"]
        self.assertEqual(l.values, ["Foo"])
        root.close()

    def test_enabled(self):
        root = MainWindow()
        root.update()
        l = Listbox(root)
        l.grid(row=0, column=0)
        root.update()
        self.assertTrue(l.enabled)
        l.enabled = False
        self.assertFalse(l.enabled)
        root.close()


if __name__ == '__main__':
    unittest.main()
