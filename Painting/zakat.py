import turtle

t = turtle.Pen()
t.color("yellow")

t.begin_fill()
t.fillcolor("yellow")
for i in range(72):
    t.forward(5)
    t.left(5)
t.end_fill()


t.begin_fill()
t.fillcolor("blue")
t.forward(200)
t.right(90)
t.forward(100)
t.right(90)
t.forward(400)
t.right(90)
t.forward(100)
t.right(90)
t.forward(200)
t.end_fill()



turtle.mainloop()