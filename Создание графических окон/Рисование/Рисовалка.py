from tkinter import *
from tkinter.colorchooser import *
root = Tk()
root.geometry("600x400")
root.title("Рисовалка")
root["bg"] = "gray75"

canvas = Canvas(root, width=540, height=400, bg="white")
canvas.grid(row=0, column=0, rowspan=7)

state="circle"
brush = 10
color = "red"
size = Label(root, text=brush, fg=color, font=(None, 32))
size.grid(row=6,column=1)

def choose(input):
    global brush
    if input=='plus':
        brush += 1
    if input=='minus':
        brush -= 1
    size.configure(text=brush)
    print(input)
    global state
    state = input

square_btn = Button(root, text="🟥", font=(None, 20), command=lambda: choose("square"))
square_btn.grid(row=0, column=1)

circle_btn = Button(root, text="🔴", font=(None, 20), command=lambda: choose("circle"))
circle_btn.grid(row=1, column=1)
line1_btn = Button(root, text=" ↘ ", font=(None, 20), command=lambda: choose("line1"))
line1_btn.grid(row=2, column=1)
line2_btn = Button(root, text=" ↙ ", font=(None, 20), command=lambda: choose("line2"))
line2_btn.grid(row=3, column=1)

plus_btn = Button(root, text="➕", font=(None, 20), command=lambda: choose("plus"))
plus_btn.grid(row=4, column=1)
minus_btn = Button(root, text="➖", font=(None, 20), command=lambda: choose("minus"))
minus_btn.grid(row=5, column=1)

def paint(event):
    if event.widget.__class__ is not Canvas:
        return
    if state=="circle":
        canvas.create_oval(event.x - brush,  # Координата x1
                           event.y - brush,  # Координата y1
                           event.x + brush,  # Координата x2
                           event.y + brush,  # Координата y2
                           fill=color,  # Цвет заливки
                           outline=color)  # Цвет обводки
    elif state == "square":
        canvas.create_rectangle(event.x - brush, event.y - brush,
                                event.x + brush, event.y + brush,
                                fill=color, outline=color)
    elif state == "line1":
        canvas.create_line(event.x - brush, event.y - brush,
                           event.x + brush, event.y + brush, fill=color)
    elif state == "line2":
        canvas.create_line(event.x + brush, event.y - brush,
                           event.x - brush, event.y + brush, fill=color)

def erase(event):
    canvas.create_oval(event.x - brush*2,  # Координата x1
                       event.y - brush*2,  # Координата y1
                       event.x + brush*2, # Координата x2
                       event.y + brush*2, # Координата y2
                       fill="white",  # Цвет заливки
                       outline="white")  # Цвет обводки
def erc(event):
    canvas.delete('all')

def arc(event):
    global color
    color_code = askcolor(title="Выбери цвет")
    color = color_code[1]
    size.configure(fg=color)

root.bind_all("<3>", arc)

root.bind_all("<BackSpace>", erc)

root.bind_all("<2>", erase)
root.bind_all("<B2-Motion>", erase)

root.bind_all("<1>", paint)
root.bind_all("<B1-Motion>", paint)


root.mainloop()