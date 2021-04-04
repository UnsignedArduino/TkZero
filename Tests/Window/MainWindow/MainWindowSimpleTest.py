from TkZero.Window.MainWindow import MainWindow
from TkZero import Vector

root = MainWindow()
root.title = "Test"
root.size = Vector.Size(width=1000, height=500)
root.position = Vector.Position(x=10, y=10)
print(f"The title of this window is {repr(root.title)}")
print(f"The size of this window is {repr(root.size)}")
print(f"The position of this window is {repr(root.position)}")
root.after(ms=1000, func=lambda: root.minimize())
root.after(ms=2000, func=lambda: root.restore())
root.after(ms=3000, func=lambda: root.maximize())
root.after(ms=4000, func=lambda: root.minimize())
root.after(ms=5000, func=lambda: root.restore())
root.after(ms=6000, func=lambda: root.full_screen(True))
root.after(ms=7000, func=lambda: root.full_screen(False))
root.mainloop()
