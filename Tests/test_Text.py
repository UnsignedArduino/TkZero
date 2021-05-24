"""
Test the TkZero.Text module
"""

import unittest

from TkZero.Text import Text, TextWrap
from TkZeroUnitTest import TkTestCase


class TextTest(TkTestCase):
    def test_no_params(self):
        with self.assertRaises(TypeError):
            Text()

    def test_bad_params(self):
        with self.assertRaises(TypeError):
            Text(parent=1)
        with self.assertRaises(TypeError):
            Text(self.root, width=5.5)
        with self.assertRaises(TypeError):
            Text(self.root, height=-3.2)
        with self.assertRaises(TypeError):
            Text(self.root, wrapping=False)

    def test_good_params(self):
        Text(self.root, width=20, height=10,
             wrapping=TextWrap.NoWrapping).grid(row=0, column=0)

    def test_text(self):
        t = Text(self.root)
        t.grid(row=0, column=0)
        self.root.update()
        self.assertEqual(t.text, "\n")
        t.text = "Foo"
        self.assertEqual(t.text, "Foo\n")
        with self.assertRaises(TypeError):
            t.text = False

    def test_enabled(self):
        t = Text(self.root)
        t.grid(row=0, column=0)
        self.assertTrue(t.enabled)
        t.enabled = False
        self.root.update()
        self.assertFalse(t.enabled)
        with self.assertRaises(TypeError):
            t.enabled = "False"

    def test_right_click(self):
        t = Text(self.root)
        t.grid(row=0, column=0)
        self.root.update()
        t.enabled = False
        self.root.update()
        t._update_context_menu_states()
        self.root.update()
        t.enabled = True
        self.root.update()
        t.select_all_contents()
        self.root.update()
        t._update_context_menu_states()
        self.assertFalse(t.can_undo())
        self.assertFalse(t.can_redo())
        self.root.update()
        t.copy_contents()
        self.root.update()
        t.cut_contents()
        self.root.update()
        t.delete_contents()
        self.root.update()
        t.paste_contents()
        self.root.update()
        t._update_context_menu_states()
        t.undo_contents()
        t.redo_contents()


if __name__ == '__main__':
    unittest.main()
