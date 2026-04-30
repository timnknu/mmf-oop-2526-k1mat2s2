# Приклад: власний модальний діалог з `grab_set()` і `wait_window()`
# (основне вікно блокується, поки діалог відкритий, а після закриття діалогу можна отримати результат взаємодії з ним користувача)

import tkinter as tk
from tkinter import ttk


# Docs:
# https://docs.python.org/3/library/tkinter.html#tkinter.Toplevel
# https://docs.python.org/3/library/tkinter.html#tkinter.Toplevel.wm_overrideredirect
# https://docs.python.org/3/library/tkinter.html#tkinter.Widget.grab_set
# https://docs.python.org/3/library/tkinter.html#tkinter.Widget.wait_visibility
# https://docs.python.org/3/library/tkinter.html#tkinter.Widget.wait_window

def ask_name(parent):
    dialog = tk.Toplevel(parent) # створюємо нове вікно, яке буде діалогом
    dialog.transient(parent) # робимо його "транзитним" для батьківського вікна (не буде окремим пунктом у панелі задач, буде завжди поверх батьківського)
    dialog.overrideredirect(True) # вимикаємо стандартні рамки і заголовок вікна (можна зробити власні, але для прикладу просто вимкнемо)

    value_var = tk.StringVar(value="Alice")
    result = {"value": None}

    frame = ttk.Frame(dialog, padding=10)
    frame.pack(fill="both", expand=True)

    ttk.Label(frame, text="Modal dialog").pack(anchor="w")
    ttk.Label(frame, text="Name:").pack(anchor="w", pady=(8, 4))
    entry = ttk.Entry(frame, textvariable=value_var)
    entry.pack(fill="x")

    def accept(event=None):
        result["value"] = value_var.get()
        dialog.destroy()

    def cancel(event=None):
        dialog.destroy()

    ttk.Button(frame, text="OK", command=accept).pack(anchor="w", pady=(10, 4))
    ttk.Button(frame, text="Cancel", command=cancel).pack(anchor="w")

    dialog.bind("<Return>", accept) # дозволяємо натискання Enter замість кнопки OK для підтвердження
    dialog.bind("<Escape>", cancel) # дозволяємо натискання Escape для скасування (замість кнопки Cancel)

    dialog.update_idletasks()  # щоб отримати правильні розміри діалогу перед позиціюванням
    x = parent.winfo_rootx() + 40
    y = parent.winfo_rooty() + 40
    dialog.geometry(f"+{x}+{y}") # позиціюємо діалог відносно батьківського вікна (з невеликим відступом)

    dialog.wait_visibility() # чекаємо, поки діалог стане видимим (щоб не було проблем з фокусом)
    dialog.grab_set() # робимо діалог модальним (захоплюємо всі події миші і клавіатури, блокуючи взаємодію з іншими вікнами)
    entry.focus_set() # встановлюємо фокус на поле вводу, щоб користувач міг одразу починати вводити текст
    parent.wait_window(dialog) # чекаємо, поки діалог буде знищений (закритий), після чого продовжуємо виконання коду і можемо отримати результат взаємодії користувача з діалогом
    return result["value"] # повертаємо результат (ім'я, введене користувачем, або None, якщо він скасував діалог)


root = tk.Tk()
root.title("Custom modal dialog")

status = ttk.Label(root, text="Last result")
status.pack(fill="x", padx=10, pady=10)

def open_dialog():
    status.config(text=f"result = {ask_name(root)}")

b1 = ttk.Button(root, text="Open modal dialog", command=open_dialog)
b1.pack(anchor="w", padx=10)

root.mainloop()