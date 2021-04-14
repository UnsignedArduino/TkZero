import unittest
from TkZero.MainWindow import MainWindow
from TkZero.Text import Text, TextWrap
from TkZero import Style


class TextTest(unittest.TestCase):
    def test_no_params(self):
        root = MainWindow()
        root.update()
        with self.assertRaises(TypeError):
            Text()
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
        root.close()


if __name__ == '__main__':
    unittest.main()
