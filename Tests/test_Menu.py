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
    def test_no_params(self):
        with self.assertRaises(TypeError):
            Menu()

    def test_bad_params(self):
        with self.assertRaises(TypeError):
            Menu(parent=1)
        with self.assertRaises(TypeError):
            Menu(self.root, is_menubar=1234)

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
        with self.assertRaises(TypeError):
            m.items = ("tuples", "don't", "work")
        with self.assertRaises(TypeError):
            m.items = [1, MenuCommand(label="Break")]
        with self.assertRaises(TypeError):
            m.items = [
                MenuCascade(label="File", items=[], underline=0.0)
            ]
        with self.assertRaises(ValueError):
            m.items = [
                MenuCascade(label="File", items=[], underline=-1)
            ]
        with self.assertRaises(ValueError):
            m.items = [
                MenuCascade(label="File", items=[], underline=42)
            ]

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
        with self.assertRaises(TypeError):
            m.items = [
                MenuCascade(label="File", items=[
                    MenuCommand(label=False),
                ])
            ]
        with self.assertRaises(TypeError):
            m.items = [
                MenuCascade(label="File", items=[
                    MenuCommand(enabled=123.456),
                ])
            ]
        with self.assertRaises(ValueError):
            m.items = [
                MenuCommand(label="Fail")
            ]
        with self.assertRaises(TypeError):
            m.items = [
                MenuCascade(label="File", items=[
                    MenuCommand(underline=0.0),
                ])
            ]
        with self.assertRaises(ValueError):
            m.items = [
                MenuCascade(label="File", items=[
                    MenuCommand(underline=-1),
                ])
            ]
        with self.assertRaises(ValueError):
            m.items = [
                MenuCascade(label="File", items=[
                    MenuCommand(underline=42),
                ])
            ]
        with self.assertRaises(TypeError):
            m.items = [
                MenuCascade(label="File", items=[
                    MenuCommand(accelerator=("la", "la")),
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
        with self.assertRaises(TypeError):
            m.items = [
                MenuCascade(label="Settings", items=[
                    MenuCheckbutton(label=True),
                ])
            ]
        with self.assertRaises(TypeError):
            m.items = [
                MenuCascade(label="Settings", items=[
                    MenuCheckbutton(variable="lala"),
                ])
            ]
        with self.assertRaises(TypeError):
            m.items = [
                MenuCascade(label="Settings", items=[
                    MenuCheckbutton(on_value=lambda: False),
                ])
            ]
        with self.assertRaises(TypeError):
            m.items = [
                MenuCascade(label="Settings", items=[
                    MenuCheckbutton(off_value=lambda: True),
                ])
            ]
        with self.assertRaises(TypeError):
            m.items = [
                MenuCascade(label="Settings", items=[
                    MenuCheckbutton(enabled=123.456),
                ])
            ]
        with self.assertRaises(ValueError):
            m.items = [
                MenuCheckbutton(label="Fail")
            ]
        with self.assertRaises(TypeError):
            m.items = [
                MenuCascade(label="Settings", items=[
                    MenuCheckbutton(underline=0.0),
                ])
            ]
        with self.assertRaises(ValueError):
            m.items = [
                MenuCascade(label="Settings", items=[
                    MenuCheckbutton(underline=-1),
                ])
            ]
        with self.assertRaises(ValueError):
            m.items = [
                MenuCascade(label="Settings", items=[
                    MenuCheckbutton(underline=42),
                ])
            ]
        with self.assertRaises(TypeError):
            m.items = [
                MenuCascade(label="Settings", items=[
                    MenuCheckbutton(accelerator=("la", "la")),
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
        with self.assertRaises(TypeError):
            m.items = [
                MenuCascade(label="Settings", items=[
                    MenuRadiobutton(value="eng", label=True),
                ])
            ]
        with self.assertRaises(TypeError):
            m.items = [
                MenuCascade(label="Settings", items=[
                    MenuRadiobutton(value="eng", variable="lala"),
                ])
            ]
        with self.assertRaises(TypeError):
            m.items = [
                MenuCascade(label="Settings", items=[
                    MenuRadiobutton(value=lambda: False),
                ])
            ]
        with self.assertRaises(TypeError):
            m.items = [
                MenuCascade(label="Settings", items=[
                    MenuRadiobutton(value="eng", enabled=123.456),
                ])
            ]
        with self.assertRaises(ValueError):
            m.items = [
                MenuRadiobutton(value="eng", label="Fail")
            ]
        with self.assertRaises(TypeError):
            m.items = [
                MenuCascade(label="Settings", items=[
                    MenuRadiobutton(value="eng", label="English", underline=0.0),
                ])
            ]
        with self.assertRaises(ValueError):
            m.items = [
                MenuCascade(label="Settings", items=[
                    MenuRadiobutton(value="eng", label="English", underline=-1),
                ])
            ]
        with self.assertRaises(ValueError):
            m.items = [
                MenuCascade(label="Settings", items=[
                    MenuRadiobutton(value="eng", label="English", underline=42),
                ])
            ]
        with self.assertRaises(TypeError):
            m.items = [
                MenuCascade(label="Settings", items=[
                    MenuRadiobutton(accelerator=("la", "la")),
                ])
            ]

    def test_cascade(self):
        m = Menu(self.root, is_menubar=True)
        m.items = [
            MenuCascade(label="File", items=[
                MenuCascade(label="Recently opened", items=[], underline=0)
            ])
        ]
        with self.assertRaises(TypeError):
            m.items = [
                MenuCascade(label="File", items=[
                    MenuCommand(label=False),
                ])
            ]
        with self.assertRaises(TypeError):
            m.items = [
                MenuCascade(label="File", items=[
                    MenuCommand(items="lala"),
                ])
            ]
        with self.assertRaises(TypeError):
            m.items = [
                MenuCascade(label="File", items=[
                    MenuCommand(enabled=123.456),
                ])
            ]
        with self.assertRaises(TypeError):
            m.items = [
                MenuCascade(label="File", items=[
                    MenuCommand(underline=0.0),
                ])
            ]
        with self.assertRaises(ValueError):
            m.items = [
                MenuCascade(label="File", items=[
                    MenuCommand(underline=-1),
                ])
            ]
        with self.assertRaises(ValueError):
            m.items = [
                MenuCascade(label="File", items=[
                    MenuCommand(underline=42),
                ])
            ]


if __name__ == '__main__':
    unittest.main()
