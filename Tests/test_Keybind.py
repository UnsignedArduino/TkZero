"""
Test the TkZero.Keybind module
"""

import unittest

from TkZero import Platform
from TkZero.Keybind import generate_accelerator_sequence
from TkZero.Keybind import generate_event_sequence
from TkZeroUnitTest import TkTestCase


class KeybindTest(TkTestCase):
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


if __name__ == '__main__':
    unittest.main()
