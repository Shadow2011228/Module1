import random
import time
from tkinter import *
from tkinter.colorchooser import *
root = Tk()
root.geometry("800x600")
root.title("Пулемет")
root["bg"] = "white"

canvas = Canvas(root, width=800, height=600, bg="white")
canvas.grid()

color="red"

canvas.create_rectangle(0,250,150,300,fill="black")
canvas.create_rectangle(0,350,150,400,fill="black")

bullets=[]

def shot():
    global bullets
    hero = canvas.create_oval(150,305,190,345,fill=color)
    b = (hero, 10, random.random())
    bullets.append(b)
    root.after(50, shot)

def draw():
    for bull in bullets:
        bullet = bull[0]
        h_x = bull[1]
        h_y = bull[2]
        x, y, x1, y1 = canvas.coords(bullet)
        if x1 >= 800:  # если мяч коснулся правой стенки
            canvas.delete(bullet)
            bullets.remove(bull)

        canvas.move(bullet, h_x, h_y)


def arc(event):
    global color
    color_code = askcolor(title="Выбери цвет")
    color = color_code[1]

a=[1,2,3,4,5]

def strelbaOchredami():
    global bullets
    for bull in a:
        hero = canvas.create_oval(150, 305, 190, 345, fill=color)
        b = (hero, 10, random.randint(-1,1)*3)
        bullets.append(b)

    for bull in bullets:
        bullet = bull[0]
        h_x = bull[1]
        h_y = bull[2]
        x, y, x1, y1 = canvas.coords(bullet)
        if x1 >= 800:  # если мяч коснулся правой стенки
            canvas.delete(bullet)
            bullets.remove(bull)




atv = Button(root, text="Огонь", fg="red", font=("Algerian", 23), command=strelbaOchredami)
atv.grid(row=0, column=0)


root.bind_all("<3>", arc)


while True:
    root.update()
    root.update_idletasks()
    draw()

    time.sleep(0.01)