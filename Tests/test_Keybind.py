"""
Test the TkZero.Keybind module
"""

import unittest

from TkZero import Platform
from TkZero.Keybind import generate_accelerator_sequence
from TkZero.Keybind import generate_event_sequence
from TkZero.Platform import on_aqua
from TkZeroUnitTest import TkTestCase


class KeybindTest(TkTestCase):
    def test_event_gen_no_params(self):
        with self.assertRaises(TypeError):
            generate_event_sequence(self.root)

    def test_event_gen_good_params(self):
        self.assertEqual(generate_event_sequence(self.root, ctrl_cmd=True,
                                                 ctrl_ctrl=False,
                                                 shift_shift=False,
                                                 alt_option=False, letter="n"),
                         "<Command-n>" if Platform.on_aqua(
                             self.root) else "<Control-n>")
        self.assertEqual(generate_event_sequence(self.root, ctrl_cmd=True,
                                                 ctrl_ctrl=False,
                                                 shift_shift=True,
                                                 alt_option=True, letter="w"),
                         "<Command-Option-Shift-W>" if Platform.on_aqua(
                             self.root) else "<Control-Alt-Shift-W>")
        self.assertEqual(generate_event_sequence(self.root, ctrl_cmd=False,
                                                 ctrl_ctrl=True,
                                                 shift_shift=False,
                                                 alt_option=False,
                                                 letter="c"), "<Control-c>")

    def test_event_gen_bad_params(self):
        with self.assertRaises(TypeError):
            generate_event_sequence(widget=1, ctrl_cmd=False,
                                    ctrl_ctrl=False, shift_shift=False,
                                    alt_option=False, letter="a")
        with self.assertRaises(TypeError):
            generate_event_sequence(widget=self.root, ctrl_cmd=lambda: None,
                                    ctrl_ctrl=False, shift_shift=False,
                                    alt_option=False, letter="a")
        with self.assertRaises(TypeError):
            generate_event_sequence(widget=self.root, ctrl_cmd=False,
                                    ctrl_ctrl="boo", shift_shift=False,
                                    alt_option=False, letter="a")
        with self.assertRaises(TypeError):
            generate_event_sequence(widget=self.root, ctrl_cmd=False,
                                    ctrl_ctrl=False, shift_shift=42.0000000001,
                                    alt_option=False, letter="a")
        with self.assertRaises(TypeError):
            generate_event_sequence(widget=self.root, ctrl_cmd=False,
                                    ctrl_ctrl=False, shift_shift=False,
                                    alt_option=[], letter="a")
        with self.assertRaises(TypeError):
            generate_event_sequence(widget=self.root, ctrl_cmd=False,
                                    ctrl_ctrl=False, shift_shift=False,
                                    alt_option=False, letter=print)
        if not on_aqua(self.root):
            with self.assertRaises(ValueError):
                generate_event_sequence(widget=self.root, ctrl_cmd=True,
                                        ctrl_ctrl=True, shift_shift=False,
                                        alt_option=False, letter="a")

    def test_accelerator_gen_no_params(self):
        with self.assertRaises(TypeError):
            generate_accelerator_sequence(self.root)

    def test_accelerator_gen_good_params(self):
        self.assertEqual(generate_accelerator_sequence(self.root,
                                                       ctrl_cmd=True,
                                                       ctrl_ctrl=False,
                                                       shift_shift=False,
                                                       alt_option=False,
                                                       letter="n"),
                         "Command-N" if Platform.on_aqua(
                             self.root) else "Control+N")
        self.assertEqual(generate_accelerator_sequence(self.root,
                                                       ctrl_cmd=True,
                                                       ctrl_ctrl=False,
                                                       shift_shift=True,
                                                       alt_option=True,
                                                       letter="w"),
                         "Command-Shift-Option-W" if Platform.on_aqua(
                             self.root) else "Control+Shift+Alt+W")
        self.assertEqual(generate_accelerator_sequence(self.root,
                                                       ctrl_cmd=False,
                                                       ctrl_ctrl=True,
                                                       shift_shift=False,
                                                       alt_option=False,
                                                       letter="c"),
                         "Control-C" if Platform.on_aqua(
                             self.root) else "Control+C")

    def test_accelerator_gen_bad_params(self):
        with self.assertRaises(TypeError):
            generate_accelerator_sequence(widget=1, ctrl_cmd=False,
                                          ctrl_ctrl=False, shift_shift=False,
                                          alt_option=False, letter="a")
        with self.assertRaises(TypeError):
            generate_accelerator_sequence(widget=self.root,
                                          ctrl_cmd=lambda: False,
                                          ctrl_ctrl=False, shift_shift=False,
                                          alt_option=False, letter="a")
        with self.assertRaises(TypeError):
            generate_accelerator_sequence(widget=self.root,
                                          ctrl_cmd=False,
                                          ctrl_ctrl="foo", shift_shift=False,
                                          alt_option=False, letter="a")
        with self.assertRaises(TypeError):
            generate_accelerator_sequence(widget=self.root,
                                          ctrl_cmd=False,
                                          ctrl_ctrl=False, shift_shift=42.0001,
                                          alt_option=False, letter="a")
        with self.assertRaises(TypeError):
            generate_accelerator_sequence(widget=self.root,
                                          ctrl_cmd=False,
                                          ctrl_ctrl=False, shift_shift=False,
                                          alt_option=[], letter="a")
        with self.assertRaises(TypeError):
            generate_accelerator_sequence(widget=self.root,
                                          ctrl_cmd=False,
                                          ctrl_ctrl=False, shift_shift=False,
                                          alt_option=False, letter=print)
        if not on_aqua(self.root):
            with self.assertRaises(ValueError):
                generate_accelerator_sequence(widget=self.root, ctrl_cmd=True,
                                              ctrl_ctrl=True,
                                              shift_shift=False,
                                              alt_option=False, letter="a")


if __name__ == '__main__':
    unittest.main()
