# Приклад: віджет Radiobutton: 'radiobutton'-"перемикачі", і використання StringVar

import tkinter as tk
from tkinter import ttk


# Docs:
# https://docs.python.org/3/library/tkinter.ttk.html#radiobutton
# https://docs.python.org/3/library/tkinter.html#coupling-widget-variables

root = tk.Tk()
root.title("Radiobutton + StringVar")

choice_var = tk.StringVar(value="green")

for color in ("red", "green", "blue"):
    ttk.Radiobutton(root, text=color, value=color, variable=choice_var).pack(anchor="w", padx=10, pady=2)

status = ttk.Label(root)
status.pack(fill="x", padx=10, pady=10)

def read_value():
    status.config(text=f"StringVar.get() = {choice_var.get()}")

def set_blue():
    choice_var.set("blue")
    read_value()

ttk.Button(root, text="Read", command=read_value).pack(anchor="w", padx=10)
ttk.Button(root, text="Set blue", command=set_blue).pack(anchor="w", padx=10, pady=4)

root.mainloop()