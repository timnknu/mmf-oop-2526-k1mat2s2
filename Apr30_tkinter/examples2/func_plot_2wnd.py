# "Удосконалений" приклад побудови графіка функції з використанням двох вікон:
# одного для введення функції, іншого для її відображення.

from tkinter import *
from tkinter import messagebox
import math


WIDTH = 500
HEIGHT = 300

root = Tk()
root.title("Function Input")
root.geometry("300x120+300+300")

plot_window = Toplevel(root)
plot_window.title("Function Plot")
plot_window.geometry("500x300+650+300")

canvas = Canvas(plot_window, width=WIDTH, height=HEIGHT, bg="white")
canvas.pack(fill=BOTH, expand=1)

mid_x = WIDTH // 2
mid_y = HEIGHT // 2

def draw_function():
    expr = function_entry.get().strip()
    if not expr:
        return

    canvas.delete("all")
    canvas.create_line(0, mid_y, WIDTH, mid_y, fill="black", width=2)
    canvas.create_line(mid_x, 0, mid_x, HEIGHT, fill="black", width=2)

    safe_names = {
        name: getattr(math, name)
        for name in dir(math)
        if not name.startswith("_")
    }
    safe_names["abs"] = abs

    points = []
    try:
        for px in range(WIDTH):
            x = (px - mid_x) / 40
            # тут ми використовуємо `eval` для обчислення значення функції, введеної користувачем
            # (це не найбезпечніший спосіб, але він найпростіший для демонстрації)
            y_value = eval(expr, {"__builtins__": {}}, {**safe_names, "x": x})
            y = mid_y - y_value * 80
            points.extend((px, y))
    except Exception:
        messagebox.showerror("Error", "Invalid function")
        return

    canvas.create_line(points, fill="blue", width=2, smooth=1)
    canvas.create_text(90, 20, text=f"y = {expr}", fill="blue", font=("Arial", 12, "bold"))

Label(root, text="Enter function y = ").pack(pady=(10, 0))
function_entry = Entry(root, width=30)
function_entry.pack(pady=5)
function_entry.insert(0, "sin(x)")

Button(root, text="Plot", command=draw_function).pack(pady=5)

draw_function()

mainloop()
