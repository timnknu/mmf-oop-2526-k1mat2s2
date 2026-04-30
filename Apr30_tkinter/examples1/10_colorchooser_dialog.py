# Приклад: діалог вибору кольору

import tkinter as tk
from tkinter import colorchooser, ttk


# Docs:
# https://docs.python.org/3/library/tkinter.colorchooser.html

root = tk.Tk()
root.title("colorchooser")

preview = tk.Label(root, text="preview", bg="lightgray", width=20, height=5)
preview.pack(padx=10, pady=10)

status = ttk.Label(root, text="Last result")
status.pack(fill="x", padx=10, pady=(0, 10))

def pick_color():
    rgb, value = colorchooser.askcolor(parent=root)
    if value:
        preview.config(bg=value)
    status.config(text=f"askcolor -> rgb={rgb}, hex={value}")

ttk.Button(root, text="Choose color", command=pick_color).pack(anchor="w", padx=10)

root.mainloop()