# Приклад: віджет Spinbox і використання IntVar

import tkinter as tk
from tkinter import ttk


# Docs:
# https://docs.python.org/3/library/tkinter.html#the-packer
# https://docs.python.org/3/library/tkinter.html#tkinter.Spinbox
# https://docs.python.org/3/library/tkinter.html#coupling-widget-variables

root = tk.Tk()
root.title("Spinbox + IntVar")

count_var = tk.IntVar(value=3)

spinbox = tk.Spinbox(root, from_=0, to=10, textvariable=count_var, width=8)
spinbox.pack(anchor="w", padx=10, pady=10)

status = ttk.Label(root)
status.pack(fill="x", padx=10, pady=(0, 10))

def read_value():
    status.config(text=f"spinbox.get() = {spinbox.get()}; IntVar.get() = {count_var.get()}")

def set_value():
    count_var.set(7)
    read_value()

ttk.Button(root, text="Read", command=read_value).pack(anchor="w", padx=10)
ttk.Button(root, text="Set to 7", command=set_value).pack(anchor="w", padx=10, pady=4)

root.mainloop()