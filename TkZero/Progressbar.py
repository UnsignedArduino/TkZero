"""
Creates a themed scale. (Slider)
"""

import tkinter as tk
from tkinter import ttk
from typing import Union


class OrientModes:
    """
    The orient modes for progress bars.
    Horizontal - makes the progress bar horizontal.
    Vertical - makes the progress bar vertical.
    """

    Horizontal = tk.HORIZONTAL
    Vertical = tk.VERTICAL


class ProgressModes:
    """
    The progress bar modes for, well, progress bars.
    Determinate - you know how much would be completed, etc.
    Indeterminate - you don't know, the progress bar will just be loading
     forever until stopped.
    """

    Determinate = "determinate"
    Indeterminate = "indeterminate"


# Used for differentiating between the different styles
_pbar_id = 0


class Progressbar(ttk.Progressbar):
    def __init__(
        self,
        parent: Union[tk.Widget, Union[tk.Tk, tk.Toplevel]],
        length: int,
        mode: str = ProgressModes.Determinate,
        orientation: str = OrientModes.Horizontal,
        allow_text: bool = True,
    ):
        """
        Initiate a ttk.Scrollbar.

        :param parent: The parent of the scrollbar.
        :param length: An int, which is the length of the scale.
        :param mode: The mode the progress bar should operate in. Defaults to
         ProgressModes.Determinate
        :param orientation: The orientation of the scrollbar and what
         direction it should scroll the widget in. Defaults to
         OrientModes.Horizontal and is a str value.
        :param allow_text: Whether you can add text on this progress bar or
         not. This can be turned off if it is messing with a theme.
        """
        self._allow_text = allow_text
        if self._allow_text:
            self._style = ttk.Style()
            global _pbar_id
            if mode == OrientModes.Horizontal:
                self.style_name = (
                    f"LabeledProgressbar{_pbar_id}.Horizontal.TProgressbar"
                )
                self._style.layout(
                    self.style_name,
                    [
                        (
                            "Horizontal.Progressbar.trough",
                            {
                                "sticky": "nswe",
                                "children": [
                                    (
                                        "Horizontal.Progressbar.pbar",
                                        {"side": "left", "sticky": "ns"},
                                    ),
                                    (f"{self.style_name}.label", {"sticky": ""}),
                                ],
                            },
                        )
                    ],
                )
            else:
                self.style_name = f"LabeledProgressbar{_pbar_id}.Vertical.TProgressbar"
                self._style.layout(
                    self.style_name,
                    [
                        (
                            "Vertical.Progressbar.trough",
                            {
                                "sticky": "nswe",
                                "children": [
                                    (
                                        "Vertical.Progressbar.pbar",
                                        {"side": "left", "sticky": "ns"},
                                    ),
                                    (f"{self.style_name}.label", {"sticky": ""}),
                                ],
                            },
                        )
                    ],
                )
            _pbar_id += 1
            # https://stackoverflow.com/a/40348163/10291933
            self._text = ""
            super().__init__(
                master=parent,
                orient=orientation,
                length=length,
                mode=mode,
                style=self.style_name,
            )
        else:
            super().__init__(
                master=parent, orient=orientation, length=length, mode=mode
            )
        self._style_root = "TProgressbar"
        self._enabled = True
        self._orientation = orientation
        self._hovering_over = False
        self.bind("<Enter>", lambda _: self._set_hover_state(True))
        self.bind("<Leave>", lambda _: self._set_hover_state(False))

    @property
    def value(self) -> float:
        """
        Get the value on this progress bar.

        :return: A float.
        """
        return float(self["value"])

    @value.setter
    def value(self, new_value: Union[int, float]) -> None:
        """
        Set the value on this progress bar.

        :param new_value: A float or an int.
        :return: None.
        """
        self["value"] = float(new_value)

    @property
    def maximum(self) -> float:
        """
        Get the maximum on this progress bar.

        :return: A float.
        """
        return self["maximum"]

    @maximum.setter
    def maximum(self, new_value: Union[int, float]) -> None:
        """
        Set the maximum on this progress bar.

        :param new_value: A float or an int.
        :return: None.
        """
        self["maximum"] = float(new_value)

    @property
    def text(self) -> str:
        """
        Get the text on this progressbar.

        :return: A str.
        """
        if not self._allow_text:
            raise ValueError(
                "Text has been disabled on this progressbar! "
                "(Enable it at creation with allow_text = True)"
            )
        return self._text

    @text.setter
    def text(self, new_text: str) -> None:
        """
        Set the text on this progressbar.

        :param new_text: A str.
        :return: None.
        """
        if not self._allow_text:
            raise ValueError(
                "Text has been disabled on this progressbar! "
                "(Enable it at creation with allow_text = True)"
            )
        self._text = new_text
        self._style.configure(self.style_name, text=self._text)

    @property
    def enabled(self) -> bool:
        """
        Get whether this widget is in normal mode or disabled mode. (grayed
        out and cannot interact with)

        :return: A bool, True if normal otherwise False.
        """
        return self._enabled

    @enabled.setter
    def enabled(self, new_state: bool) -> None:
        """
        Set whether this widget is in normal mode or disabled mode (grayed out
        and cannot interact with)

        :param new_state: The new state (a bool) True for enabled and False
         for disabled.
        :return: None.
        """
        self._enabled = new_state
        self.state(["!disabled" if self._enabled else "disabled"])

    @property
    def hovering_over(self) -> bool:
        """
        Get whether the cursor is hovering over this widget or not.

        :return: A bool.
        """
        return self._hovering_over

    def _set_hover_state(self, is_hovering: bool) -> None:
        """
        Set whether we are hovering over this widget or not.

        :param is_hovering: A bool.
        :return: None.
        """
        self._hovering_over = is_hovering
