from tkinter import *
root = Tk()
root.geometry("600x400")


label_a = Label(text="Label A", bg="yellow")
label_b = Label(text="Label B", bg="orange")
label_c = Label(text="Label C", bg="red")
label_d = Label(text="Label D", bg="light green")
label_e = Label(text="-----Label E-----\n123", bg="blue")
label_f = Label(text="Label F", bg="purple")

#  и разместим их по такой вот сетке
label_a.grid(row=0, column=0)
label_b.grid(row=1, column=0)
label_c.grid(row=0, column=1)
label_d.grid(row=0, column=2)
label_e.grid(row=2, column=0, rowspan=2, columnspan=2)
label_f.grid(row=4, column=0)

root.mainloop()
