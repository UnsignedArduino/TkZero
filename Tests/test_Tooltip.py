"""
Test the TkZero.Keybind module
"""

import unittest

from TkZero.Button import Button
from TkZero.Tooltip import add_tooltip
from TkZeroUnitTest import TkTestCase


class TooltipTest(TkTestCase):
    def test_no_params(self):
        with self.assertRaises(TypeError):
            add_tooltip()

    def test_good_params(self):
        b = Button(self.root, text="Click me this will definitely not install "
                                   "a virus")
        b.grid(row=0, column=0)
        add_tooltip(b, text="This definitely does not install a virus.\n"
                            "Click me!\n"
                            "Come on I know you want to click me. ",
                    hold_time=500)

    def test_bad_params(self):
        b = Button(self.root, text="Click me this will definitely not install "
                                   "a virus")
        b.grid(row=0, column=0)
        with self.assertRaises(TypeError):
            add_tooltip("this is definitely a widget")
        with self.assertRaises(TypeError):
            add_tooltip(b, text=1234567890)
        with self.assertRaises(TypeError):
            add_tooltip(b, text="fail", hold_time=55.5)


if __name__ == '__main__':
    unittest.main()
