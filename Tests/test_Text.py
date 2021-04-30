"""
Test the TkZero.Text module
"""

import unittest

from TkZero.MainWindow import MainWindow
from TkZero.Text import Text, TextWrap


class TextTest(unittest.TestCase):
    def test_no_params(self):
        root = MainWindow()
        root.update()
        with self.assertRaises(TypeError):
            Text()
        root.update()
        root.close()

    def test_bad_params(self):
        root = MainWindow()
        root.update()
        with self.assertRaises(TypeError):
            Text(parent=1)
        with self.assertRaises(TypeError):
            Text(root, width=5.5)
        with self.assertRaises(TypeError):
            Text(root, height=-3.2)
        with self.assertRaises(TypeError):
            Text(root, wrapping=False)
        root.update()
        root.close()

    def test_good_params(self):
        root = MainWindow()
        root.update()
        Text(root, width=20, height=10, wrapping=TextWrap.NoWrapping).grid(row=0, column=0)
        root.update()
        root.close()

    def test_text(self):
        root = MainWindow()
        root.update()
        t = Text(root)
        t.grid(row=0, column=0)
        root.update()
        self.assertEqual(t.text, "\n")
        t.text = "Foo"
        self.assertEqual(t.text, "Foo\n")
        with self.assertRaises(TypeError):
            t.text = False
        root.close()

    def test_enabled(self):
        root = MainWindow()
        root.update()
        t = Text(root)
        t.grid(row=0, column=0)
        self.assertTrue(t.enabled)
        t.enabled = False
        root.update()
        self.assertFalse(t.enabled)
        with self.assertRaises(TypeError):
            t.enabled = "False"
        root.close()

    def test_right_click(self):
        root = MainWindow()
        root.update()
        t = Text(root)
        t.grid(row=0, column=0)
        root.update()
        t.enabled = False
        root.update()
        t._update_context_menu_states()
        root.update()
        t.enabled = True
        root.update()
        t.select_all_contents()
        root.update()
        t._update_context_menu_states()
        root.update()
        t.copy_contents()
        root.update()
        t.cut_contents()
        root.update()
        t.delete_contents()
        root.update()
        t.paste_contents()
        root.update()
        root.close()


if __name__ == '__main__':
    unittest.main()
