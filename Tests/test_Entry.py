"""
Test the TkZero.Entry module
"""

import unittest

from TkZero import Style
from TkZero.Entry import Entry
from TkZero.MainWindow import MainWindow


class EntryTest(unittest.TestCase):
    def test_no_params(self):
        root = MainWindow()
        root.update()
        with self.assertRaises(TypeError):
            Entry()
        root.update()
        root.close()

    def test_bad_params(self):
        root = MainWindow()
        root.update()
        with self.assertRaises(TypeError):
            Entry(parent=1)
        with self.assertRaises(TypeError):
            Entry(root, width=2.2)
        with self.assertRaises(TypeError):
            Entry(root, show=5)
        root.update()
        root.close()

    def test_good_params(self):
        root = MainWindow()
        root.update()
        Entry(root, width=20, show="*", validate=lambda: True,
              command=lambda: print("Changed")).grid(row=0, column=0)
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
        with self.assertRaises(TypeError):
            e.value = 1234
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
        with self.assertRaises(TypeError):
            e.enabled = "True"
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
        with self.assertRaises(TypeError):
            e.read_only = "False"
        root.close()

    def test_right_click(self):
        root = MainWindow()
        root.update()
        e = Entry(root)
        e.grid(row=0, column=0)
        root.update()
        e.enabled = False
        root.update()
        e._update_context_menu_states()
        root.update()
        e.enabled = True
        e.read_only = True
        root.update()
        e._update_context_menu_states()
        root.update()
        e.read_only = False
        e.select_all_contents()
        root.update()
        e._update_context_menu_states()
        root.update()
        e.copy_contents()
        root.update()
        e.cut_contents()
        root.update()
        e.delete_contents()
        root.update()
        e.paste_contents()
        root.update()
        root.close()


    def test_style(self):
        root = MainWindow()
        root.update()
        e = Entry(root)
        e.grid(row=0, column=0)
        Style.define_style(Style.WidgetStyleRoots.Button, "Test", background="red")
        e.apply_style("Test")
        self.assertEqual(e.cget("style"), "Test.TEntry")
        root.update()
        with self.assertRaises(TypeError):
            e.apply_style(123456789)
        root.close()


if __name__ == '__main__':
    unittest.main()
