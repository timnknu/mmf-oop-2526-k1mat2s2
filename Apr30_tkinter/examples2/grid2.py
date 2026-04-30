# Використання методу grid для розміщення віджетів у вікні.
# У цьому прикладі, віджет Label розтягується на всю ширину вікна, а
# віджет Entry розтягується на всю ширину стовпця.

from tkinter import *

root = Tk()
root.columnconfigure(1, weight=1)

obj =Label(root, text="Header", bg="#b0c4de")
obj.grid(row=0, column=0, columnspan=3, sticky="ew")
# тут row=0, column=0 задає позицію віджета в сітці,
# columnspan=3 дозволяє йому займати 3 стовпці,
# а sticky="ew" розтягує його по горизонталі (від лівого до правого краю)

Label(root, text="Name:").grid(row=1, column=0) # тут row=1, column=0 задає позицію віджета в сітці, але без sticky він займе лише фіксовану ширину (задля лаконічності коду ми одразу викликали метод grid() без збереження об'єкта в окрему змінну)
Entry(root).grid(row=1, column=1, sticky="ew")
Button(root, text="Go").grid(row=1, column=2)
Text(root, height=4).grid(row=2, column=0, columnspan=3, sticky="ew")
Button(root, text="OK").grid(row=3, column=2)

root.mainloop()
