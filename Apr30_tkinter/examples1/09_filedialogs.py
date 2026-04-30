# Приклад: вбудовані діалоги, пов'язані з файлами та папками

import tkinter as tk
from tkinter import filedialog, ttk


# Docs:
# https://docs.python.org/3/library/dialog.html#tkinter.filedialog

root = tk.Tk()
root.title("filedialog")

status = ttk.Label(root, text="Last path")
status.pack(fill="x", padx=10, pady=10)

def open_file():
    status.config(text=f"askopenfilename -> {filedialog.askopenfilename(parent=root)}")

def save_file():
    status.config(text=f"asksaveasfilename -> {filedialog.asksaveasfilename(parent=root)}")

def choose_directory():
    status.config(text=f"askdirectory -> {filedialog.askdirectory(parent=root)}")

ttk.Button(root, text="Open file", command=open_file).pack(anchor="w", padx=10)
ttk.Button(root, text="Save as", command=save_file).pack(anchor="w", padx=10, pady=4)
ttk.Button(root, text="Choose directory", command=choose_directory).pack(anchor="w", padx=10)

root.mainloop()