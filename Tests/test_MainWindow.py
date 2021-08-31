"""
Test the TkZero.MainWindow module
"""
import base64
import tkinter as tk
import unittest

from PIL import ImageTk

from TkZero import Vector
from TkZero.Label import Label
from TkZeroUnitTest import TkTestCase


class MainWindowTest(TkTestCase):
    def test_title(self):
        self.root.title = "My title"
        self.assertEqual(self.root.title, "My title")
        with self.assertRaises(TypeError):
            self.root.title = 1

    def test_icon(self):
        image_data = base64.b64decode("""R0lGODlhZABkAPcAAAAAAAAAMwAAZgAAmQAAzA
        AA/wArAAArMwArZgArmQArzAAr/wBVAABVMwBVZgBVmQBVzABV/wCAAACAMwCAZgCAmQCAz
        ACA/wCqAACqMwCqZgCqmQCqzACq/wDVAADVMwDVZgDVmQDVzADV/wD/AAD/MwD/ZgD/mQD/
        zAD//zMAADMAMzMAZjMAmTMAzDMA/zMrADMrMzMrZjMrmTMrzDMr/zNVADNVMzNVZjNVmTN
        VzDNV/zOAADOAMzOAZjOAmTOAzDOA/zOqADOqMzOqZjOqmTOqzDOq/zPVADPVMzPVZjPVmT
        PVzDPV/zP/ADP/MzP/ZjP/mTP/zDP//2YAAGYAM2YAZmYAmWYAzGYA/2YrAGYrM2YrZmYrm
        WYrzGYr/2ZVAGZVM2ZVZmZVmWZVzGZV/2aAAGaAM2aAZmaAmWaAzGaA/2aqAGaqM2aqZmaq
        mWaqzGaq/2bVAGbVM2bVZmbVmWbVzGbV/2b/AGb/M2b/Zmb/mWb/zGb//5kAAJkAM5kAZpk
        AmZkAzJkA/5krAJkrM5krZpkrmZkrzJkr/5lVAJlVM5lVZplVmZlVzJlV/5mAAJmAM5mAZp
        mAmZmAzJmA/5mqAJmqM5mqZpmqmZmqzJmq/5nVAJnVM5nVZpnVmZnVzJnV/5n/AJn/M5n/Z
        pn/mZn/zJn//8wAAMwAM8wAZswAmcwAzMwA/8wrAMwrM8wrZswrmcwrzMwr/8xVAMxVM8xV
        ZsxVmcxVzMxV/8yAAMyAM8yAZsyAmcyAzMyA/8yqAMyqM8yqZsyqmcyqzMyq/8zVAMzVM8z
        VZszVmczVzMzV/8z/AMz/M8z/Zsz/mcz/zMz///8AAP8AM/8AZv8Amf8AzP8A//8rAP8rM/
        8rZv8rmf8rzP8r//9VAP9VM/9VZv9Vmf9VzP9V//+AAP+AM/+AZv+Amf+AzP+A//+qAP+qM
        /+qZv+qmf+qzP+q///VAP/VM//VZv/Vmf/VzP/V////AP//M///Zv//mf//zP///wAAAAAA
        AAAAAAAAACH5BAEAAPwALAAAAABkAGQAAAj/APcJHEiwoMGDCBMqXMiwocOHECNKnEixosW
        LGDNq3Mixo8ePIEOKHEmypMmTKFOqXMmypcuXMGPKnEmzps2bOHPq3Mmzp8+fQIMKHUq0qN
        GjSJMqXcq0qdOnUKNKnUq1qkx9hABohdBw2KIbWrUGiPFG2UJ6mGKEBXAAB6iFWNcagUtFb
        KiHisI+UKhPmIq1gLXGQSgMRuC1AdRES5g3bIC7CfPVBfDYYVytFhLO+3sY8OCClzuvRbDY
        YGitCUof1De5csPQew8K6xzjhtqwnwk2Rmyb81oBkAme1gokIWu7lrNuPcgOcAA4qgXqGxY
        m977hOqL39Q1AQPTryhGf/0IoGbnD3bEJbl6b/WEwxMFBhwfAtWDjAIaXr24dn2/4zMLNN9
        dDx4k1nnGTURZfaG/4Zt1A5VF2IEP6oFdQc2HV99AuaxW3EIZaDShdeHGUE5Z3pvGXXIYF0
        eLYhK+FlxqFMqoWWhyhaQihig6Fl951Cer4WoIiLvSeeQLtNlg+DoLGI41hASjQeoJFBCIA
        DyZ0ZW76aIGbQBxqheKOSMJl4UAguvZQmv1p1uSIXwIZlofSPQmXl/oJdGR33zG055gMRYj
        lQBWGdQeajgUXoZoMnQnmiTA2FGZ3kboZp0AkEuQiaqUVGMChMUZJ0DqJRkRqmQpRCQCo4F
        0qZ4h1ov9qnI8EsWnlWlkiZKt0Sl5Y6qJtIpSjer4V2ZCqxib0p42ZthhWap4Gi5CjrwIwI
        4EJXuvfs9E1K1yCONq5LWbOzhnRplV+KJdweK7K3InPiDurXgUxWepD9orZ57cnatfrQeg+
        oByj49JnELqUwaGQMJto+pu087QLgLE3ksedrIzR6yRgMrxV0DBeWlegWIoJ59da2g7krUF
        7OsbqnaIapOpaB8QQA3cPzpOgYzZfDABppq0sn3OVCkstu6J5ZprESadM6L8IzUzwvHmadn
        LSOCyzGi8+I6awsOG9fFDLUydE60LJLHKbVgfIoMm+BaWdn1Y3jGHWQkIHfa9VfPcr7fffg
        Acu+OCEF2744YgnrvjijDfu+OOQRy755JRXbvnlmGeu+eacd754QAA7""")
        self.assertEqual(self.root.icon, None)
        icon = tk.PhotoImage(data=image_data)
        self.root.icon = icon
        self.assertEqual(self.root.icon, icon)
        icon = ImageTk.PhotoImage(data=image_data)
        self.root.icon = icon
        self.assertEqual(self.root.icon, icon)
        with self.assertRaises(TypeError):
            self.root.icon = 69

    def test_size(self):
        self.assertEqual(self.root.size, Vector.Size(width=200, height=200))
        self.root.size = Vector.Size(width=400, height=400)
        self.assertEqual(self.root.size, Vector.Size(width=400, height=400))
        self.root.size = (300, 300)
        self.assertEqual(self.root.size, Vector.Size(width=300, height=300))
        with self.assertRaises(TypeError):
            self.root.size = [400, 400]

    def test_position(self):
        self.root.position = Vector.Position(x=0, y=0)
        self.assertEqual(self.root.position, Vector.Position(x=0, y=0))
        self.root.position = (100, 100)
        self.assertEqual(self.root.position, Vector.Position(x=100, y=100))
        with self.assertRaises(TypeError):
            self.root.position = [0, 0]

    def test_minimized(self):
        self.root.minimized = True
        self.root.update()
        self.assertTrue(self.root.minimized)
        self.root.minimized = False
        self.root.update()
        self.assertFalse(self.root.minimized)
        with self.assertRaises(TypeError):
            self.root.minimized = "bar"

    def test_restored(self):
        self.root.minimized = True
        self.root.update()
        self.root.restored = True
        self.root.update()
        self.assertTrue(self.root.restored)
        self.root.restored = False
        self.root.update()
        self.assertFalse(self.root.restored)
        with self.assertRaises(TypeError):
            self.root.restored = "foo"

    def test_maximized(self):
        self.root.maximized = True
        self.root.update()
        self.assertTrue(self.root.maximized)
        self.root.maximized = False
        self.root.update()
        self.assertFalse(self.root.maximized)
        with self.assertRaises(TypeError):
            self.root.maximized = "boo"

    def test_fullscreen(self):
        self.root.full_screen = True
        self.root.update()
        self.assertTrue(self.root.full_screen)
        self.root.full_screen = False
        self.root.update()
        self.assertFalse(self.root.full_screen)
        with self.assertRaises(TypeError):
            self.root.full_screen = "la"

    def test_binds(self):
        func = lambda: None
        self.root.bind_to_event("<<MyOwnSpecialEvent>>", func,
                                run_in_thread=True)
        binds = self.root.bind_to_event("<<MyOwnSpecialEvent>>")
        self.assertTrue(len(binds) > 0)
        with self.assertRaises(TypeError):
            self.root.bind_to_event(1234)
        with self.assertRaises(TypeError):
            self.root.bind_to_event("<<event>>", add=1)
        self.root.generate_event("<<MyOwnSpecialEvent>>")

    def test_enabled(self):
        self.assertTrue(self.root.enabled)
        Label(self.root).grid(row=0, column=0)
        Label(self.root).grid(row=1, column=0)
        self.root.update()
        self.root.enabled = False
        self.assertFalse(self.root.enabled)
        with self.assertRaises(TypeError):
            self.root.enabled = "False"

    def test_on_close(self):
        on_close_func = lambda: None
        self.root.on_close = on_close_func
        self.assertEqual(self.root.on_close, on_close_func)
        self.root.close()
        self.root.destroy()


if __name__ == "__main__":
    unittest.main()
