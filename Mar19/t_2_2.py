import turtle
import random

turtle.speed(3)

class Triangle:
    def __init__(self, x1, y1, x2, y2):
        self._position = (0, 0) # абсолютна позиція першої вершини
        self._vertex1 = (x1, y1) # позиція другої відносно першої вершини
        self._vertex2 = (x2, y2) # позиція третьої відносно першої вершини
        self._color = "black"
    def randomize_position(self):
        x0 = random.randint(-250, 250)
        y0 = random.randint(-250, 250)
        self._position = (x0, y0)

    def set_random_color(self):
        possible_colors = ['red', 'green', 'blue', 'yellow']
        i = random.randint(0, len(possible_colors))
        self._color = possible_colors[i]
    def set_position(self, x, y):
        self._position = (x, y)
    def set_color(self, color):
        self._color = color
    def draw(self):
        x0 = self._position[0]
        y0 = self._position[1]
        x1, y1 = self._vertex1
        x2, y2 = self._vertex2
        turtle.penup()
        turtle.goto(x0, y0)
        turtle.pendown()

        turtle.color(self._color)
        turtle.fillcolor(self._color)
        turtle.begin_fill()

        turtle.goto(x0 + x1, y0 + y1)
        turtle.goto(x0 + x2, y0 + y2)
        turtle.goto(x0, y0)

        turtle.end_fill()
#
my_objects = []
for i in range(5):
    tr = Triangle(random.randint(-50, 50),
                  random.randint(-50, 50),
                  random.randint(-50, 50),
                  random.randint(-50, 50))
    tr.randomize_position()
    tr.set_random_color()
    tr.draw()
#     my_objects.append(tr)
#
# for obj in my_objects:
#     obj.draw()

turtle.mainloop()
