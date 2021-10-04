import unittest

from TkZero.Notebook import Notebook, Tab
from TkZeroUnitTest import TkTestCase


class NotebookTest(TkTestCase):
    def test_good_params(self):
        Notebook(self.root).grid(row=0, column=0)

    def test_tabs(self):
        nb = Notebook(self.root)
        nb.grid(row=0, column=0)
        self.assertEqual(len(nb.tabs), 0)
        nb.tabs = [Tab(nb), Tab(nb)]
        nb.update_tabs()
        self.root.update()
        self.assertEqual(len(nb.tabs), 2)

    def test_selected(self):
        nb = Notebook(self.root)
        nb.grid(row=0, column=0)
        nb.tabs = [Tab(nb), Tab(nb)]
        nb.update_tabs()
        self.root.update()
        nb.selected = 0
        nb.selected += 1
        with self.assertRaises(TypeError):
            nb.selected = "1"
        with self.assertRaises(ValueError):
            nb.selected = -1
        with self.assertRaises(ValueError):
            nb.selected = 42


class TabTest(TkTestCase):
    def test_no_params(self):
        with self.assertRaises(TypeError):
            Tab()

    def test_bad_params(self):
        nb = Notebook(self.root)
        nb.grid(row=0, column=0)

    def test_good_params(self):
        nb = Notebook(self.root)
        nb.grid(row=0, column=0)
        nb.tabs = [
            Tab(nb, title="Tab 1"),
            Tab(nb, title="Tab 2"),
            Tab(nb, title="Tab 3")
        ]

    def test_title(self):
        nb = Notebook(self.root)
        nb.grid(row=0, column=0)
        t = Tab(nb, title="foobar")
        self.assertEqual(t.title, "foobar")
        t.title = "lalala"
        self.root.update()
        self.assertEqual(t.title, "lalala")

    def test_enabled(self):
        nb = Notebook(self.root)
        nb.grid(row=0, column=0)
        t = Tab(nb)
        self.assertTrue(t.enabled)
        t.enabled = False
        self.root.update()
        self.assertFalse(t.enabled)

    def test_hover(self):
        nb = Notebook(self.root)
        nb.grid(row=0, column=0)
        t = Tab(nb)
        self.root.update()
        self.assertEqual(type(t.hovering_over), bool)


if __name__ == '__main__':
    unittest.main()
