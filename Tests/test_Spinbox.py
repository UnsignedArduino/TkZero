"""
Test the TkZero.Spinbox module
"""

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

    def test_bad_params(self):
        root = MainWindow()
        root.update()
        with self.assertRaises(TypeError):
            Spinbox(parent=1)
        with self.assertRaises(TypeError):
            Spinbox(root, values=["this", "doesn't", "work"])
        with self.assertRaises(TypeError):
            Spinbox(root, width=5.5)
        with self.assertRaises(TypeError):
            Spinbox(root, show=1)
        root.update()
        root.close()

    def test_good_params(self):
        root = MainWindow()
        root.update()
        Spinbox(root, width=20, show="*", values=("foo", "bar"),
                validate=lambda: True,
                command=lambda: print("Changed")).grid(row=0, column=0)
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
        with self.assertRaises(TypeError):
            s.value = ("la", )
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
        with self.assertRaises(TypeError):
            s.values = []
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
        with self.assertRaises(TypeError):
            s.enabled = "True"
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
        with self.assertRaises(TypeError):
            s.read_only = "False"
        root.close()

    def test_right_click(self):
        root = MainWindow()
        root.update()
        s = Spinbox(root)
        s.grid(row=0, column=0)
        root.update()
        s.enabled = False
        root.update()
        s._update_context_menu_states()
        root.update()
        s.enabled = True
        s.read_only = True
        root.update()
        s._update_context_menu_states()
        root.update()
        s.read_only = False
        s.select_all_contents()
        root.update()
        s._update_context_menu_states()
        root.update()
        s.copy_contents()
        root.update()
        s.cut_contents()
        root.update()
        s.delete_contents()
        root.update()
        s.paste_contents()
        root.update()
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
