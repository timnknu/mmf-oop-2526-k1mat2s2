# Приклад: віджет Scale - "повзунок", і використання DoubleVar

import tkinter as tk
from tkinter import ttk


# Docs:
# https://docs.python.org/3/library/tkinter.ttk.html#scale
# https://docs.python.org/3/library/tkinter.html#coupling-widget-variables

root = tk.Tk()
root.title("Scale + DoubleVar")

volume_var = tk.DoubleVar(value=25.0)

scale = ttk.Scale(root, from_=0, to=100, variable=volume_var, orient="horizontal")
scale.pack(fill="x", padx=10, pady=10)

status = ttk.Label(root)
status.pack(fill="x", padx=10, pady=(0, 10))

def read_value():
    status.config(text=f"DoubleVar.get() = {volume_var.get():.1f}; scale.get() = {scale.get():.1f}")

def set_value():
    volume_var.set(75)
    read_value()

ttk.Button(root, text="Read", command=read_value).pack(anchor="w", padx=10)
ttk.Button(root, text="Set to 75", command=set_value).pack(anchor="w", padx=10, pady=4)

root.mainloop()