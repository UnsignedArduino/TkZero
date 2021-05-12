"""
Extends the unittest.TestCase module to automatically create and destroy
windows in setUp and tearDown
"""

import tkinter as tk
import unittest
from time import sleep

from TkZero.MainWindow import MainWindow


class TkTestCase(unittest.TestCase):
    def setUp(self) -> None:
        """
        Set up the test case. In this case, we are creating a main window and
        scheduling it to delete itself within 10 seconds otherwise the test
        pipeline may halt because of a Tk bug.

        :return: None.
        """
        while True:
            try:
                self.root = MainWindow()
            except tk.TclError:
                sleep(0.1)
            else:
                break
        self.root.update()
        self.root.after(ms=10_000, func=self.closeWindow)

    def tearDown(self) -> None:
        """
        Close the test case. In this case, we are closing the main window.

        :return: None.
        """
        self.closeWindow()

    def closeWindow(self) -> None:
        """
        Try to close the window. If it's been already destroyed,
        _tkinter.TclError would be raised and we just ignore it.

        :return:
        """
        try:
            self.root.close()
        except tk.TclError:
            pass
