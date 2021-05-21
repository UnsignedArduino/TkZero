import unittest

from TkZero.Notebook import Notebook, Tab
from TkZeroUnitTest import TkTestCase


class NotebookTest(TkTestCase):
    def test_no_params(self):
        with self.assertRaises(TypeError):
            Notebook()

    def test_bad_params(self):
        with self.assertRaises(TypeError):
            Notebook(parent=1)

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
        with self.assertRaises(TypeError):
            nb.tabs = {}
        with self.assertRaises(TypeError):
            nb.tabs = [1, 2]
            nb.update_tabs()

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
        with self.assertRaises(TypeError):
            Tab(parent=1)
        with self.assertRaises(TypeError):
            Tab(nb, title=12345678)

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
        with self.assertRaises(TypeError):
            t.title = 0

    def test_enabled(self):
        nb = Notebook(self.root)
        nb.grid(row=0, column=0)
        t = Tab(nb)
        self.assertTrue(t.enabled)
        t.enabled = False
        self.root.update()
        self.assertFalse(t.enabled)
        with self.assertRaises(TypeError):
            t.enabled = 1


if __name__ == '__main__':
    unittest.main()
