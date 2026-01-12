import turtle

t = turtle.Pen()
screen=turtle.Screen()
screen.setup(1000,500)
screen.bgcolor("cyan")
screen.title("Привет, ребята!")
t.hideturtle()
for x in range (300, 400, 8):
          t.forward(x / 5)
          t.left(x / 10)
          t.backward (29)
screen.clear()


turtle.mainloop()