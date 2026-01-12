from tkinter import *
root = Tk()
root.geometry("600x400")
root.title("Окошко")
root["bg"] = "green"

def home():
    text = Label(root, text="И тебе привет!")

    text.pack()

atv = Button(root, text="Привет!", fg="red", font=("Algerian", 23), command=home)
atv.pack()


root.mainloop()