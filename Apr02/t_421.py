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
        

turtle.speed(1)

# f = Figure(100, 50)
# f.show()

s = Square(100, 50, 50)
s.set_color('blue')
s.show()
s.hide()

c = Circle(-150, 80, 70)
c.show()
c.hide()
c.show()

turtle.mainloop()