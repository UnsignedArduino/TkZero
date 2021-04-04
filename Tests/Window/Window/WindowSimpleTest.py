from TkZero.Window.MainWindow import MainWindow
from TkZero.Window.Window import Window
from TkZero import Vector

root = MainWindow()
root.title = "Test"
root.minimize()
window = Window(parent=root)
window.size = Vector.Size(width=1000, height=500)
window.position = Vector.Position(x=10, y=10)
print(f"The title of this window is {repr(window.title)}")
print(f"The size of this window is {repr(window.size)}")
print(f"The position of this window is {repr(window.position)}")
window.after(ms=1000, func=lambda: window.minimize())
window.after(ms=2000, func=lambda: window.restore())
window.after(ms=3000, func=lambda: window.maximize())
window.after(ms=4000, func=lambda: window.minimize())
window.after(ms=5000, func=lambda: window.restore())
window.after(ms=6000, func=lambda: window.full_screen(True))
window.after(ms=7000, func=lambda: window.full_screen(False))
root.mainloop()
