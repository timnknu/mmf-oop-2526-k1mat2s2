# Приклад: віджет Text: багаторядковий Text і використання StringVar для "дзеркалювання"
import tkinter as tk
from tkinter import ttk


# Docs:
# https://docs.python.org/3/library/tkinter.html
# https://docs.python.org/3/library/tkinter.html#the-text-widget
# https://docs.python.org/3/library/tkinter.html#coupling-widget-variables

root = tk.Tk()
root.title("Text + StringVar mirror")

mirror_var = tk.StringVar(value="first line\nsecond line")

text = tk.Text(root, width=40, height=6)
text.pack(padx=10, pady=10)
text.insert("1.0", mirror_var.get())

status = ttk.Label(root)
status.pack(fill="x", padx=10, pady=(0, 10))

def sync_from_text(event=None):
    mirror_var.set(text.get("1.0", "end-1c"))
    status.config(text=f"StringVar.get() = {mirror_var.get()}")

def load_from_variable():
    text.delete("1.0", tk.END)
    text.insert("1.0", mirror_var.get())
    sync_from_text()

def set_with_variable():
    mirror_var.set("set via StringVar\nthen copied into Text")
    load_from_variable()

text.bind("<KeyRelease>", sync_from_text)

ttk.Button(root, text="Read Text", command=sync_from_text).pack(anchor="w", padx=10)
ttk.Button(root, text="Set via StringVar", command=set_with_variable).pack(anchor="w", padx=10, pady=4)

root.mainloop()