import tkinter as tk
from tkinter import ttk


root = tk.Tk()

utxt = tk.StringVar(value="Введіть суму і код валюти")
usrinp = ttk.Entry(root, textvariable=utxt)
usrinp.pack()

cb_val = tk.StringVar(value='UAH')
cb = ttk.Combobox(root, values=["USD", "UAH", "EUR"],
                  textvariable=cb_val)
cb.pack()

rates = {
    ('USD', 'UAH'): 36.9,
    ('USD', 'USD'): 1.0,
    ('USD', 'EUR'): 36.9/39.5,

    ('EUR', 'UAH'): 39.5,
    ('EUR', 'USD'): 39.5/36.9,
    ('EUR', 'EUR'): 1.0,

    ('UAH', 'USD'): 1.0,
    ('UAH', 'USD'): 1/36.9,
    ('UAH', 'EUR'): 1/39.5,
}

def btn_on_click():
    print('Button clicked', utxt.get(), cb_val.get())
    s = utxt.get()  # "50.5 EUR"
    d = s.split()  # ["50.5", "EUR"]
    v = float(d[0])
    k = (d[1],  cb_val.get())
    v_new = v * rates[k]
    lbl_txt.set( str(v_new) )


btn = ttk.Button(root, text="Convert!", command=btn_on_click)
btn.pack()

lbl_txt = tk.StringVar(value="Hello")
lbl = ttk.Label(root, textvariable=lbl_txt)
lbl.pack()


root.mainloop()
