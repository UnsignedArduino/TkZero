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
root.mainloop()
