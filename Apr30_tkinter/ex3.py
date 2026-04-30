# приклад tkinter.simpledialog: функція askstring() використовується
# для відображення діалогового вікна, яке запитує у користувача рядок тексту
# (у деякому сенсі - це аналог функції input()).
# Коли користувач вводить текст і натискає кнопку "OK", функція повертає введений рядок.
# Якщо користувач натискає "Cancel", функція повертає None.

from tkinter.simpledialog import askstring
from tkinter import *

top = Tk()

top.geometry("100x100")


def show():
    name = askstring("Input", "Enter you name")
    print(name)


B = Button(top, text="Click", command=show)
B.place(x=50, y=50)

top.mainloop()