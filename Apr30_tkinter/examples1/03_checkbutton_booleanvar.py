# Приклад: віджет Checkbutton: 'checkbox'-"прапорець", і використання BooleanVar

import tkinter as tk
from tkinter import ttk


# Docs:
# https://docs.python.org/3/library/tkinter.ttk.html#checkbutton
# https://docs.python.org/3/library/tkinter.html#coupling-widget-variables

root = tk.Tk()
root.title("Checkbutton + BooleanVar")

enabled_var = tk.BooleanVar(value=True)

ttk.Checkbutton(root, text="Enabled", variable=enabled_var).pack(anchor="w", padx=10, pady=10)

status = ttk.Label(root)
status.pack(fill="x", padx=10, pady=(0, 10))

def read_value():
    status.config(text=f"BooleanVar.get() = {enabled_var.get()}")

def toggle_value():
    enabled_var.set(not enabled_var.get())
    read_value()

ttk.Button(root, text="Read", command=read_value).pack(anchor="w", padx=10)
ttk.Button(root, text="Toggle via BooleanVar", command=toggle_value).pack(anchor="w", padx=10, pady=4)

root.mainloop()