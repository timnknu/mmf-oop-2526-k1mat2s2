import tkinter as tk
from tkinter import ttk


root = tk.Tk()

utxt = tk.StringVar(value="Введіть суму і код валюти")
usrinp = ttk.Entry(root, textvariable=utxt)
usrinp.pack()

cb_val = tk.StringVar()
cb = ttk.Combobox(root, values=["USD", "UAH", "EUR"],
                  textvariable=cb_val)
cb.pack()

def btn_on_click():
    print('Button clicked', utxt.get(), cb_val.get())

btn = ttk.Button(root, text="Convert!", command=btn_on_click)
btn.pack()

lbl = ttk.Label(root)
lbl['text']="Hello"
lbl.pack()


root.mainloop()
