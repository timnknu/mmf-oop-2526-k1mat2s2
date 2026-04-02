import turtle

class Figure:
    def __init__(self, x0, y0):
        self._x0 = x0
        self._y0 = y0
        self._color = 'red'
    def set_color(self, clr):
        self._color = clr
    def _draw(self):
        raise NotImplementedError("Потрібно спершу створити клас-нащадок")
    def show(self):
        turtle.color(self._color)
        self._draw()
    def hide(self):
        turtle.color('white')
        self._draw()

class Circle(Figure):
    def __init__(self, x0, y0, r):
        super().__init__(x0, y0)
        self._r = r
    def _draw(self):
        turtle.penup()
        turtle.goto(self._x0, self._y0 - self._r)
        turtle.pendown()
        turtle.circle(self._r)


class Rectangle(Figure):
    def __init__(self, x0, y0, sideX, sideY):
        super().__init__(x0, y0)
        self._a = sideX
        self._b = sideY
    def _draw(self):
        turtle.penup()
        turtle.goto(self._x0, self._y0)
        turtle.pendown()
        turtle.goto(self._x0, self._y0 + self._b)
        turtle.goto(self._x0 + self._a, self._y0 + self._b)
        turtle.goto(self._x0 + self._a, self._y0)
        turtle.goto(self._x0, self._y0)

class Square(Rectangle):
    def __init__(self, x0, y0, a):
        super().__init__(x0, y0, a, a)

class Car(Figure):
    def __init__(self, x0, y0):
        super().__init__(x0, y0)
        self._s = Rectangle(x0, y0, 150, 50)
        self._s.set_color('blue')
        self._w1 = Circle(x0 + 40, y0, 30)
        self._w2 = Circle(x0 + 150 - 40, y0, 30)
    def _draw(self):
        self._s._draw()
        self._w1._draw()
        self._w2._draw()


turtle.speed(1)

# f = Figure(100, 50)
# f.show()

c = Car(-200, 50)
c.show()

turtle.mainloop()