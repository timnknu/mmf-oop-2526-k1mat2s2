# Приклад: вбудовані вікна повідомлень

import tkinter as tk
from tkinter import messagebox, ttk

# Docs:
# https://docs.python.org/3/library/tkinter.messagebox.html

root = tk.Tk()
root.title("Message boxes")

status = ttk.Label(root, text="Last result")
status.pack(fill="x", padx=10, pady=10)

def show(name, callback):
    s = f"{name} -> {callback()}"
    status.config(text=s)
    print(s)

actions = [
    ("showinfo", lambda: messagebox.showinfo("Info", "hello", parent=root)),
    ("showwarning", lambda: messagebox.showwarning("Warning", "careful", parent=root)),
    ("showerror", lambda: messagebox.showerror("Error", "something failed", parent=root)),
    ("askquestion", lambda: messagebox.askquestion("Question", "continue?", parent=root)),
    ("askokcancel", lambda: messagebox.askokcancel("Question", "continue?", parent=root)),
    ("askyesno", lambda: messagebox.askyesno("Question", "continue?", parent=root)),
    ("askretrycancel", lambda: messagebox.askretrycancel("Question", "try again?", parent=root)),
]

for name, action in actions:
    ttk.Button(root, text=name, command=lambda name=name, action=action: show(name, action)).pack(anchor="w", padx=10, pady=2)

root.mainloop()