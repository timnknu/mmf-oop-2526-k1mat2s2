import tkinter as tk
from tkinter import ttk
import curr_conv_logic

root = tk.Tk()

utxt = tk.StringVar(value="Введіть суму і код валюти")
usrinp = ttk.Entry(root, textvariable=utxt)
usrinp.pack()

cb_val = tk.StringVar(value='UAH')
cb = ttk.Combobox(root, values=["USD", "UAH", "EUR"],
                  textvariable=cb_val)
cb.pack()


def btn_on_click():
    print('Button clicked', utxt.get(), cb_val.get())

    v_new = curr_conv_logic.convert_value(utxt.get(), cb_val.get())

    lbl_txt.set( str(v_new) )


btn = ttk.Button(root, text="Convert!", command=btn_on_click)
btn.pack()

lbl_txt = tk.StringVar(value="Hello")
lbl = ttk.Label(root, textvariable=lbl_txt)
lbl.pack()


root.mainloop()
