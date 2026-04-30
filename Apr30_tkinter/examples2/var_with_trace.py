# https://www.geeksforgeeks.org/python/tracing-tkinter-variables-in-python/

from tkinter import *

root = Tk()
var = StringVar()

def on_button():
    current = var.get()          # read
    print("User typed:", current)
    var.set(current.upper())     # write (updates UI immediately)

def on_change(*args): # ця функція буде викликана при кожній зміні значення var
    print("Changed to:", var.get())

var.trace_add("write", on_change) # trace_add() - це новий метод для додавання "слідкування" за змінами "змінної-контейнера";
# "write" означає, що ми хочемо викликати функцію on_change при кожній зміні значення var

Entry(root, textvariable=var).pack()
Label(root, textvariable=var).pack()
Button(root, text="Process", command=on_button).pack()

root.mainloop()
