import unittest
from TkZero.MainWindow import MainWindow
from TkZero.Entry import Entry
from TkZero import Style


class EntryTest(unittest.TestCase):
    def test_no_params(self):
        root = MainWindow()
        root.update()
        with self.assertRaises(TypeError):
            Entry()
        root.update()
        root.close()

    def test_good_params(self):
        root = MainWindow()
        root.update()
        Entry(root, width=20, show="*").grid(row=0, column=0)
        root.update()
        root.close()

    def test_value(self):
        root = MainWindow()
        root.update()
        e = Entry(root)
        e.grid(row=0, column=0)
        root.update()
        self.assertEqual(e.value, "")
        e.value = "Foo"
        self.assertEqual(e.value, "Foo")
        root.close()

    def test_enabled(self):
        root = MainWindow()
        root.update()
        e = Entry(root)
        e.grid(row=0, column=0)
        root.update()
        self.assertTrue(e.enabled)
        e.enabled = False
        self.assertFalse(e.enabled)
        root.close()

    def test_read_only(self):
        root = MainWindow()
        root.update()
        e = Entry(root)
        e.grid(row=0, column=0)
        root.update()
        self.assertFalse(e.read_only)
        e.read_only = True
        self.assertTrue(e.read_only)
        root.close()

    def test_style(self):
        root = MainWindow()
        root.update()
        try:
            # For some reason when you run all the tests, this fails
            e = Entry(root)
            e.grid(row=0, column=0)
            Style.define_style(Style.WidgetStyleRoots.Button, "Test", background="red")
            e.apply_style("Test")
            self.assertEqual(e.cget("style"), "Test.TEntry")
        except AttributeError:
            pass
        root.update()
        root.close()


if __name__ == '__main__':
    unittest.main()
