# Приклад використання методу pack() для розміщення віджетів у головному вікні програми.
# Його параметри fill і expand дозволяють керувати тим, як віджети заповнюють доступний простір.
# Параметр fill може приймати значення tk.X (віджет заповнює горизонтально), tk.Y (віджет заповнює вертикально) або tk.BOTH (віджет заповнює і горизонтально, і вертикально).
# Параметр expand=True дозволяє віджету розширюватися, щоб заповнити доступний простір (якщо він є)

import tkinter as tk

root = tk.Tk()

obj = tk.Label(root, text="TOP fill=X", bg="#8ecae6")
obj.pack(fill=tk.X) # віджет заповнює простір горизонтально, але не вертикально

tk.Label(root, text="LEFT\nfill=Y", bg="#ffb703").pack(side=tk.LEFT, fill=tk.Y) # віджет розміщується зліва, і заповнює простір вертикально, але не горизонтально
# важливо, що цей віджет розміщується зліва від віджета, який був розміщений раніше (з текстом "TOP fill=X")
tk.Label(root, text="RIGHT\nfill=Y", bg="#fb8500").pack(side=tk.RIGHT, fill=tk.Y) # цей віджет розміщується справа від віджета, який був розміщений раніше
tk.Text(root).pack(fill=tk.BOTH, expand=True) # віджет заповнює весь доступний простір, як горизонтально, так і вертикально

# зверніть увагу на порядок створення віджетів та "порядок" їх фактичного відображення на головному вікні
# Причина "парадоксу", який спостерігається, полягає в тому, що для методу pack()
# вікно — це "робоча область". Кожен новий виклик .pack() "відрізає" шматок від цієї області (з вказаного у параметрах боку).
# "Хто перший прийшов — той відрізав собі шматок від повного краю вікна"


def myfunc():
    root.destroy() # закриває головне вікно, а отже - і всю програму

btn = tk.Button(root)
btn['text'] = 'Close'
btn['command'] = myfunc
btn.pack(side=tk.BOTTOM) # віджет розміщується внизу, але не заповнює простір ні горизонтально, ні вертикально (за замовчуванням fill=None)

root.mainloop()



# Аналогічний код, але з імпортом всіх імен з tkinter (не рекомендовано)

# from tkinter import *
#
# root = Tk()
#
# Label(root, text="TOP fill=X", bg="#8ecae6").pack(fill=X)
# Label(root, text="LEFT\nfill=Y", bg="#ffb703").pack(side=LEFT, fill=Y)
# Label(root, text="RIGHT\nfill=Y", bg="#fb8500").pack(side=RIGHT, fill=Y)
# Text(root).pack(fill=BOTH, expand=True)
# Button(root, text="Close", command=root.destroy).pack(side=BOTTOM)
#
# root.mainloop()


