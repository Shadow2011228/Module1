import turtle
t = turtle.Pen()
screen = turtle.Screen()
screen.setup(1000, 800)
screen.bgcolor("black")
screen.title("Спираль")
colors  = ["red"]
t.speed(0)
for x in range(200):
  t.pencolor(colors[x % 1])
  t.circle(50)
  t.up()
  t.forward(x*1)
  t.down()
  t.left(11)

turtle.mainloop()