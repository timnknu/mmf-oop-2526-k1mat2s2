# Приклад використання Canvas для побудови графіка функції y = sin(x)
# як набору точок, з'єднаних лінією. На графіку також виводиться текст "y = sin(x)"

from tkinter import *
import math


WIDTH = 500
HEIGHT = 300

root = Tk()
root.title("Function Plot")
root.geometry("500x300+300+300")

canvas = Canvas(root, width=WIDTH, height=HEIGHT, bg="white")
canvas.pack(fill=BOTH, expand=1)

mid_x = WIDTH // 2
mid_y = HEIGHT // 2

canvas.create_line(0, mid_y, WIDTH, mid_y, fill="black", width=2)
canvas.create_line(mid_x, 0, mid_x, HEIGHT, fill="black", width=2)

points = []
for x in range(WIDTH):
    y = mid_y - math.sin((x - mid_x) / 40) * 80
    points.extend((x, y))
print(points)

canvas.create_line(points, fill="blue", width=2, smooth=1)
canvas.create_text(70, 20, text="y = sin(x)", fill="blue", font=("Arial", 12, "bold"))

mainloop()
