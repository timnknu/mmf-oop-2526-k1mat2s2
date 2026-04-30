# Приклад: метод .after() для створення "відкладених" та "періодичних" викликів функцій

import time
import tkinter as tk
from tkinter import ttk


# Docs:
# https://docs.python.org/3/library/tkinter.html#tkinter.Widget.after

root = tk.Tk()
root.title("after() timers")

clock_var = tk.StringVar()
counter_var = tk.IntVar(value=0)
running_var = tk.BooleanVar(value=True)

ttk.Label(root, textvariable=clock_var).pack(padx=10, pady=(10, 4))
ttk.Label(root, textvariable=counter_var).pack(padx=10, pady=(0, 10))

def update_clock():
    clock_var.set(time.strftime("%H:%M:%S"))
    root.after(1000, update_clock)

def periodic_task():
    if running_var.get():
        counter_var.set(counter_var.get() + 1)
    root.after(500, periodic_task)

ttk.Checkbutton(root, text="Run periodic task", variable=running_var).pack(anchor="w", padx=10)
ttk.Button(root, text="Reset", command=lambda: counter_var.set(0)).pack(anchor="w", padx=10, pady=4)

update_clock()
periodic_task()
root.mainloop()