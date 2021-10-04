"""
Test the TkZero.Text module
"""

import unittest

from TkZero.Text import Text, TextWrap
from TkZeroUnitTest import TkTestCase


class TextTest(TkTestCase):
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

    def test_cursor(self):
        t = Text(self.root)
        t.grid(row=0, column=0)
        self.root.update()
        self.assertEqual(t.cursor, "1.0")
        t.text = "This text\nhas some\nnewlines."
        t.cursor = "2.0"
        self.assertEqual(t.cursor, "2.0")

    def test_enabled(self):
        t = Text(self.root)
        t.grid(row=0, column=0)
        self.assertTrue(t.enabled)
        t.enabled = False
        self.root.update()
        self.assertFalse(t.enabled)

    def test_read_only(self):
        t = Text(self.root)
        t.grid(row=0, column=0)
        self.assertFalse(t.read_only)
        t.read_only = True
        self.root.update()
        self.assertTrue(t.read_only)

    def test_hover(self):
        t = Text(self.root)
        t.grid(row=0, column=0)
        self.root.update()
        self.assertEqual(type(t.hovering_over), bool)

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
