import turtle

class Figure:
    def __init__(self, x0, y0):
        self._x0 = x0
        self._y0 = y0
        self._color = 'red'
    def set_color(self, clr):
        self._color = clr

class Circle(Figure):
    def __init__(self, x0, y0, r):
        super().__init__(x0, y0)
        self._r = r
    def draw(self):
        turtle.penup()
        turtle.goto(self._x0, self._y0 - self._r)
        turtle.pendown()
        turtle.color(self._color)
        turtle.circle(self._r)

class Square(Figure):
    def __init__(self, x0, y0, side):
        super().__init__(x0, y0)
        self._a = side
    def draw(self):
        turtle.penup()
        turtle.goto(self._x0, self._y0)
        turtle.pendown()
        turtle.color(self._color)
        turtle.goto(self._x0, self._y0 + self._a)
        turtle.goto(self._x0 + self._a, self._y0 + self._a)
        turtle.goto(self._x0 + self._a, self._y0)
        turtle.goto(self._x0, self._y0)


turtle.speed(1)

s = Square(100, 50, 50)
s.set_color('blue')
s.draw()

# c = Circle(-150, 80, 70)
# c.draw()

turtle.mainloop()