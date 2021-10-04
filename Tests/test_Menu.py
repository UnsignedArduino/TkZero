"""
Test the TkZero.Menu module
"""

import unittest

from TkZero.Keybind import generate_accelerator_sequence
from TkZero.Menu import Menu
from TkZero.Menu import MenuCheckbutton, MenuRadiobutton
from TkZero.Menu import MenuCommand, MenuCascade, MenuSeparator
from TkZeroUnitTest import TkTestCase


class MenuTest(TkTestCase):
    def test_good_params(self):
        Menu(self.root, is_menubar=True)

    def test_items(self):
        m = Menu(self.root, is_menubar=True)
        items = [
            MenuCascade(label="File", items=[
                MenuCommand(label="New"),
                MenuCommand(label="Open..."),
                MenuCommand(label="Save"),
                MenuSeparator(),
                MenuCommand(label="Exit")
            ], underline=0)
        ]
        m.items = items
        self.root.update()
        self.assertEqual(m.items, items)

    def test_commands(self):
        m = Menu(self.root, is_menubar=True)
        m.items = [
            MenuCascade(label="File", items=[
                MenuCommand(label="New", underline=0,
                            accelerator=generate_accelerator_sequence(
                                m, ctrl_cmd=True, ctrl_ctrl=False,
                                shift_shift=False, alt_option=False, letter="N"
                            ))
            ])
        ]

    def test_separator(self):
        m = Menu(self.root, is_menubar=True)
        m.items = [
            MenuCascade(label="File", items=[
                MenuSeparator()
            ])
        ]
        with self.assertRaises(ValueError):
            m.items = [
                MenuSeparator()
            ]

    def test_checkbutton(self):
        m = Menu(self.root, is_menubar=True)
        m.items = [
            MenuCascade(label="Settings", items=[
                MenuCheckbutton(label="Verbose logging", underline=0,
                                accelerator=generate_accelerator_sequence(
                                    m, ctrl_cmd=True, ctrl_ctrl=False,
                                    shift_shift=False, alt_option=False,
                                    letter="v"
                                ))
            ])
        ]

    def test_radiobutton(self):
        m = Menu(self.root, is_menubar=True)
        m.items = [
            MenuCascade(label="Language", items=[
                MenuRadiobutton(value="eng", label="English", underline=0,
                                accelerator=generate_accelerator_sequence(
                                    m, ctrl_cmd=True, ctrl_ctrl=False,
                                    shift_shift=False, alt_option=False,
                                    letter="E"
                                ))
            ])
        ]

    def test_cascade(self):
        m = Menu(self.root, is_menubar=True)
        m.items = [
            MenuCascade(label="File", items=[
                MenuCascade(label="Recently opened", items=[], underline=0)
            ])
        ]


if __name__ == '__main__':
    unittest.main()
