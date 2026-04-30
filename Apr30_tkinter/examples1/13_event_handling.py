# Приклад: обробка подій, відмінних від натискання кнопки (віджет Button)
# Показано обробку руху миші, кліків, прокрутки колеса та натискань клавіш.
# Для обробки клавіатурних подій, потрібно спершу клацнути в білій області (event_box) перед натисканням клавіш.

import tkinter as tk
from tkinter import ttk


# Docs:
# https://docs.python.org/3/library/tkinter.html#bindings-and-events
# https://docs.python.org/3/library/tkinter.html#tkinter.Widget.bind

root = tk.Tk()
root.title("Event handling")

status_var = tk.StringVar(value="Move mouse, click, or press keys")
ttk.Label(root, textvariable=status_var).pack(fill="x", padx=10, pady=10)

event_box = tk.Frame(root, bg="white", width=320, height=160, highlightthickness=1, highlightbackground="gray")
event_box.pack(padx=10, pady=(0, 10))
event_box.pack_propagate(False)

ttk.Label(event_box, text="Click here first").place(relx=0.5, rely=0.5, anchor="center")

def on_motion(event):
    status_var.set(f"motion: x={event.x}, y={event.y}")

def on_click(event):
    event_box.focus_set()
    status_var.set(f"button {event.num}: x={event.x}, y={event.y}")

def on_key(event):
    status_var.set(f"key: keysym={event.keysym}, char={event.char}")

def on_wheel_up(event):
    status_var.set("wheel up")

def on_wheel_down(event):
    status_var.set("wheel down")

# примітка: залежно від операційної системи, прокрутка колеса може генерувати різні події.
event_box.bind("<Motion>", on_motion)
event_box.bind("<Button-1>", on_click)
event_box.bind("<Button-4>", on_wheel_up)
event_box.bind("<Button-5>", on_wheel_down)
event_box.bind("<MouseWheel>", lambda event: status_var.set(f"wheel delta={event.delta}"))
root.bind("<KeyPress>", on_key)

root.mainloop()