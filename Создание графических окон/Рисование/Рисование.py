from tkinter import *
root = Tk()
root.geometry("600x400")
root.title("Рисовалка")
root["bg"] = "gray75"

canas = Canvas(root, width=600, height=400, bg="white")
canas.pack()

canas.create_line(200,400,200,200)

root.mainloop()