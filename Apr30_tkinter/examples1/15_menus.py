# Приклад*: меню, елементи-прапорці та елементи-перемикачі

import tkinter as tk
from tkinter import messagebox, ttk


# Docs:
# https://docs.python.org/3/library/tkinter.html#menus-and-toolbars
# https://docs.python.org/3/library/tkinter.html#tkinter.Menu

root = tk.Tk()
root.title("Menus")

# Створюємо змінні-"обгортки" для елементів меню
show_status_var = tk.BooleanVar(value=True)
theme_var = tk.StringVar(value="Light")
status_var = tk.StringVar()

# Створюємо віджет для статусу (та одразу "прив'язуємо" текст його до змінної status_var)
content = ttk.Frame(root, padding=10)
content.pack(fill="both", expand=True)
status_label = ttk.Label(content, textvariable=status_var)
status_label.pack(anchor="w")

def refresh_status():
    if show_status_var.get():
        status_label.pack(anchor="w")
    else:
        status_label.pack_forget()
    status_var.set(f"theme={theme_var.get()}, show_status={show_status_var.get()}")

menubar = tk.Menu(root) # створюємо головне меню

file_menu = tk.Menu(menubar, tearoff=False) # створюємо підменю для пункту "File"; tearoff=False - забороняє відривати це меню в окреме вікно
file_menu.add_command(label="Refresh", command=refresh_status) # додаємо пункт "Refresh" до підменю "File", який викликає функцію refresh_status при виборі цього пункту
file_menu.add_command(label="Exit", command=root.destroy)  # додаємо пункт "Exit" до підменю "File", який викликає метод destroy головного вікна при виборі цього пункту

menubar.add_cascade(label="File", menu=file_menu) # додаємо до головного меню пункт "File", який відкриває підменю file_menu при виборі цього пункту

view_menu = tk.Menu(menubar, tearoff=False) # створюємо підменю для пункту "View"; tearoff=False - забороняє відривати це меню в окреме вікно
view_menu.add_checkbutton(label="Show status", variable=show_status_var, command=refresh_status)
view_menu.add_radiobutton(label="Light", variable=theme_var, value="Light", command=refresh_status)
view_menu.add_radiobutton(label="Dark", variable=theme_var, value="Dark", command=refresh_status)

menubar.add_cascade(label="View", menu=view_menu) # додаємо до головного меню пункт "View", який відкриває підменю view_menu при виборі цього пункту; у підменю "View" є елемент-прапорець "Show status" та два елементи-перемикачі "Light" та "Dark", які керують відповідними змінними та викликають функцію refresh_status при зміні їхнього стану

help_menu = tk.Menu(menubar, tearoff=False) # створюємо підменю для пункту "Help"; tearoff=False - забороняє відривати це меню в окреме вікно
help_menu.add_command(label="About", command=lambda: messagebox.showinfo("About", "Menu example", parent=root))

menubar.add_cascade(label="Help", menu=help_menu) # додаємо до головного меню пункт "Help", який відкриває підменю help_menu при виборі цього пункту; у підменю "Help" є пункт "About", який при виборі цього пункту викликає функцію help_menu (а вона - показує інформаційне вікно з заголовком "About" та текстом "Menu example")

root.config(menu=menubar) # налаштовуємо головне вікно - встановлюємо його меню рівне створеному нами головному меню menubar
refresh_status()
root.mainloop()