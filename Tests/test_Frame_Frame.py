import unittest
from TkZero.Window.MainWindow import MainWindow
from TkZero.Frame.Frame import Frame
from TkZero import Style


class FrameTest(unittest.TestCase):
    def test_frame_no_params(self):
        root = MainWindow()
        root.update()
        with self.assertRaises(TypeError):
            Frame()
        root.update()
        root.close()

    def test_frame_good_params(self):
        root = MainWindow()
        root.update()
        Frame(root).grid(row=0, column=0)
        root.update()
        root.close()

    def test_frame_width_height(self):
        root = MainWindow()
        root.update()
        f = Frame(root)
        f.grid(row=0, column=0)
        f.width = 500
        f.height = 200
        root.update()
        self.assertEqual(f.width, 500)
        self.assertEqual(f.height, 200)
        root.close()

    def test_frame_style(self):
        root = MainWindow()
        root.update()
        f = Frame(root)
        f.grid(row=0, column=0)
        Style.define_style(Style.WidgetStyleRoots.Frame, "Test", background="red")
        f.apply_style("Test")
        self.assertEqual(f.cget("style"), "Test.TFrame")
        root.update()
        root.close()


if __name__ == '__main__':
    unittest.main()
