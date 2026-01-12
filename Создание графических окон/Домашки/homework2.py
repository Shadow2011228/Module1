from tkinter import *

# Инициализация основного окна
root = Tk()
root.title("Рисунок домика")

# Создание Canvas
canvas = Canvas(root, width=300, height=300, bg='white')
canvas.pack()

# Рисуем крышу дома
canvas.create_polygon(150, 50, 50, 150, 250, 150, fill='lightblue', outline='black')

# Рисуем корпус дома
canvas.create_rectangle(75, 150, 225, 250, fill='lightblue', outline='black')

# Рисуем окно
canvas.create_rectangle(100, 175, 140, 215, fill='white', outline='black')
canvas.create_line(120, 175, 120, 215, fill='black')
canvas.create_line(100, 195, 140, 195, fill='black')

# Рисуем солнце
canvas.create_oval(200, 20, 250, 70, fill='orange', outline='orange')

# Рисуем дерево рядом с домом
for i in range(5, 200, 10):
    canvas.create_arc(10 + i, 240, 35 + i, 300, start=160, extent=-90, style=ARC, outline='green', width=2)

# Запуск основного цикла Tkinter
root.mainloop()