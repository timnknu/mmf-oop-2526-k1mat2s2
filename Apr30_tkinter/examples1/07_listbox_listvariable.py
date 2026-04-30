# Приклад: віджет Listbox та його параметр listvariable

import tkinter as tk
from tkinter import ttk


# Docs:
# https://docs.python.org/3/library/tkinter.html#listbox
# https://docs.python.org/3/library/tkinter.html#coupling-widget-variables

root = tk.Tk()
root.title("Listbox + listvariable")

items_var = tk.StringVar(value=("Alpha", "Beta", "Gamma"))

listbox = tk.Listbox(root, listvariable=items_var, height=4, exportselection=False)
listbox.pack(fill="x", padx=10, pady=10)
listbox.selection_set(0)

status = ttk.Label(root)
status.pack(fill="x", padx=10, pady=(0, 10))

def read_selection():
    selection = listbox.curselection()
    if selection:
        index = selection[0]
        status.config(text=f"selected = {listbox.get(index)}")
    else:
        status.config(text="selected = none")

def replace_items():
    items_var.set(("One", "Two", "Three"))
    listbox.selection_clear(0, tk.END)
    listbox.selection_set(1)
    read_selection()

ttk.Button(root, text="Read", command=read_selection).pack(anchor="w", padx=10)
ttk.Button(root, text="Replace via listvariable", command=replace_items).pack(anchor="w", padx=10, pady=4)

root.mainloop()