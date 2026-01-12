import time
import turtle
import random

t = turtle.Pen()
t.shape("arrow")
screen=turtle.Screen()
screen.setup(1000,800)
screen.bgcolor("midnight blue")
screen.title("Фейерверки")
t.hideturtle()

def refresh():
    t.color('black')
    t.up()
    t.goto(random.randint(-400, 400), -380)
    t.down()
    time.sleep(0.3)
    screen.clear()
    screen.bgcolor("midnight blue")


def fairvork():


    t.showturtle()
    t.left(90)

    for x in range(42):
        t.forward(10)
        t.up()
        t.forward(5)
        t.down()

    colors=("red", "blue", "yellow", "white", "pink")

    t.hideturtle()
    turtle.tracer(0, 0)
    t.color(random.choice(colors))
    for x in range(20):
        t.forward(140)
        t.right(190)
        turtle.update()
    turtle.tracer(1, 1)
    t.left(110)

for i in range(200):
    refresh()
    fairvork()



turtle.mainloop()
