import turtle
t = turtle.Pen()
screen = turtle.Screen()
screen.setup(1000, 800)
screen.bgcolor("black")
screen.title("Спираль")
t.pencolor('red')
t.speed(0)
for x in range(70):
  t.circle(x)
  t.left(10)

turtle.mainloop()