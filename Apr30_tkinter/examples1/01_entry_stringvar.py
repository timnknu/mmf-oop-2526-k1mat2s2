# Приклад: віджет Entry: однорядкове текстове поле і використання StringVar

import tkinter as tk
from tkinter import ttk

# Docs:
# https://docs.python.org/3/library/tkinter.html
# https://docs.python.org/3/library/tkinter.ttk.html#entry
# https://docs.python.org/3/library/tkinter.html#coupling-widget-variables

root = tk.Tk()
root.title("Entry + StringVar")

value_var = tk.StringVar(value="Initial text")

entry = ttk.Entry(root, textvariable=value_var) # створюємо віджет Entry і зв'язуємо його вміст зі змінною value_var
entry.pack(fill="x", padx=10, pady=10)

status = ttk.Label(root) # створюємо віджет Label для відображення статусу
status.pack(fill="x", padx=10, pady=(0, 10))

def read_value():
    print('The value is', value_var.get())
    status.config(text=f"entry.get() = {entry.get()}; StringVar.get() = {value_var.get()}")

def set_with_variable():
    value_var.set("set via StringVar")
    read_value()

def set_with_widget():
    entry.delete(0, tk.END)
    entry.insert(0, "set via Entry")
    read_value()

b1 = ttk.Button(root, text="Read", command=read_value) # створюємо кнопку, яка при натисканні викликає функцію read_value
b1.pack(anchor="w", padx=10)
b2 = ttk.Button(root, text="Set via StringVar", command=set_with_variable) # створюємо кнопку, яка при натисканні викликає функцію set_with_variable (яка змінює значення StringVar)
b2.pack(anchor="w", padx=10, pady=4)
ttk.Button(root, text="Set via Entry", command=set_with_widget).pack(anchor="w", padx=10) # створюємо кнопку, яка при натисканні викликає функцію set_with_widget (яка змінює текст у віджеті Entry); тут ми одразу викликали метод pack() без збереження об'єкта в окрему змінну - задля лаконічності коду


root.mainloop()