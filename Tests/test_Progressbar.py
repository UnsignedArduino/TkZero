"""
Test the TkZero.Progressbar module
"""

import unittest

from TkZero.Progressbar import Progressbar, OrientModes, ProgressModes
from TkZeroUnitTest import TkTestCase


class ProgressbarTest(TkTestCase):
    def test_good_params(self):
        Progressbar(self.root, orientation=OrientModes.Vertical,
                    mode=ProgressModes.Determinate, length=200
                    ).grid(row=0, column=1)

    def test_value(self):
        p = Progressbar(self.root, orientation=OrientModes.Vertical,
                        mode=ProgressModes.Determinate, length=200)
        p.grid(row=0, column=0)
        p.maximum = 100
        self.root.update()
        self.assertEqual(p.value, 0)
        p.value = 25
        self.root.update()
        self.assertEqual(p.value, 25)

    def test_max(self):
        p = Progressbar(self.root, orientation=OrientModes.Vertical,
                        mode=ProgressModes.Determinate, length=200)
        p.grid(row=0, column=0)
        p.maximum = 100
        self.root.update()
        self.assertEqual(p.maximum, 100)
        p.maximum = 25
        self.root.update()
        self.assertEqual(p.maximum, 25)

    def test_text(self):
        p = Progressbar(self.root, orientation=OrientModes.Vertical,
                        mode=ProgressModes.Determinate, length=200)
        p.grid(row=0, column=0)
        p.value = 0
        p.maximum = 100
        self.root.update()
        self.assertEqual(p.text, "")
        p.text = "Foobar"
        self.root.update()
        self.assertEqual(p.text, "Foobar")

    def test_disabled_text(self):
        p = Progressbar(self.root, orientation=OrientModes.Vertical,
                        mode=ProgressModes.Determinate, length=200,
                        allow_text=False)
        p.grid(row=0, column=0)
        p.value = 0
        p.maximum = 100
        self.root.update()
        with self.assertRaises(ValueError):
            self.assertEqual(p.text, "")
        with self.assertRaises(ValueError):
            p.text = "Foobar"
        self.root.update()
        with self.assertRaises(ValueError):
            self.assertEqual(p.text, "Foobar")

    def test_indeterminate(self):
        p = Progressbar(self.root, orientation=OrientModes.Horizontal,
                        mode=ProgressModes.Indeterminate, length=200)
        p.grid(row=0, column=0)
        p.start()
        self.root.update()
        self.root.after(ms=2000, func=self.root.close)
        self.root.mainloop()

    def test_enabled(self):
        p = Progressbar(self.root, orientation=OrientModes.Vertical,
                        mode=ProgressModes.Determinate, length=200)
        p.grid(row=0, column=0)
        self.root.update()
        self.assertTrue(p.enabled)
        p.enabled = False
        self.assertFalse(p.enabled)

    def test_hover(self):
        p = Progressbar(self.root, orientation=OrientModes.Vertical,
                        mode=ProgressModes.Determinate, length=200)
        p.grid(row=0, column=1)
        self.root.update()
        self.assertEqual(type(p.hovering_over), bool)


if __name__ == '__main__':
    unittest.main()
