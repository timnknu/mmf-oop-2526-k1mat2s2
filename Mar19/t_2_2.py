import turtle

turtle.speed(1)

x0, y0 = (-100, -50)
x1, y1 = 80, 50
x2, y2 = 180, -150

turtle.penup()
turtle.goto(x0, y0)
turtle.pendown()

turtle.color('red')

turtle.fillcolor('yellow')
turtle.begin_fill()

turtle.goto(x0+x1, y0+y1)
turtle.goto(x0+x2, y0+y2)
turtle.goto(x0, y0)

turtle.end_fill()


turtle.mainloop()
