import turtle

t=turtle.Pen()
screen=turtle.Screen()
screen.setup(1000,800)
screen.bgcolor("black")
screen.title("Спираль")
colors=["red", "yellow", "blue", "green"]
t.speed(0)
for x in range(200):
    t.pencolor(colors[x % 4])
    t.circle(x)
    t.left(91)


turtle.mainloop()