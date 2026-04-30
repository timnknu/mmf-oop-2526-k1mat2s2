from tkinter import *

root = Tk()

# Використовуємо StringVar для "зв'язування" тексту в Entry та Label
var = StringVar()
Entry(root, textvariable=var).pack()
Label(root, textvariable=var).pack()

root.mainloop()
