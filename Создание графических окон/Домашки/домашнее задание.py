from tkinter import *

root = Tk()
root.geometry("600x400")
root.title("Рисовалка")
root["bg"] = "gray75"

canvas = Canvas(root, width=600, height=400, bg="white")
canvas.pack()

canvas.create_line(300,100,300,200)
canvas.create_line(200,200,400,200)
canvas.create_line(300,100,350,150)
canvas.create_line(300,200,350,150)
canvas.create_line(200,200,250,250)
canvas.create_line(400,200,350,250)
canvas.create_line(250,250,350,250)

root.mainloop()