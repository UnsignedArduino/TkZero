import unittest
from TkZero.Window.MainWindow import MainWindow
from TkZero.Keybind import generate_event_sequence
from TkZero import Platform


class KeybindTest(unittest.TestCase):
    def testKeybindsNoParams(self):
        root = MainWindow()
        root.minimize()
        with self.assertRaises(TypeError):
            generate_event_sequence(root)
        root.close()

    def testKeybindsGoodParams(self):
        root = MainWindow()
        root.minimize()
        self.assertEqual(generate_event_sequence(root, ctrl_cmd=True, ctrl_ctrl=False,
                                                 shift_shift=False, alt_option=False, letter="n"),
                         "<Command-n>" if Platform.on_aqua(root) else "<Control-n>")
        self.assertEqual(generate_event_sequence(root, ctrl_cmd=True, ctrl_ctrl=False,
                                                 shift_shift=True, alt_option=True, letter="w"),
                         "<Command-Option-Shift-W>" if Platform.on_aqua(root) else "<Control-Alt-Shift-W>")
        self.assertEqual(generate_event_sequence(root, ctrl_cmd=False, ctrl_ctrl=True,
                                                 shift_shift=False, alt_option=False, letter="c"), "<Control-c>")
        root.close()

    def testKeybindsBadParams(self):
        root = MainWindow()
        root.minimize()
        with self.assertRaises(TypeError):
            generate_event_sequence(widget=1)
        with self.assertRaises(TypeError):
            generate_event_sequence(ctrl_ctrl=lambda: None)
        with self.assertRaises(TypeError):
            generate_event_sequence(ctrl_ctrl="foo")
        with self.assertRaises(TypeError):
            generate_event_sequence(shift_shift=41.9999999999999999)
        with self.assertRaises(TypeError):
            generate_event_sequence(alt_option=[])
        with self.assertRaises(TypeError):
            generate_event_sequence(letter=print)
        root.close()


if __name__ == '__main__':
    unittest.main()
