from tkinter import *
root = Tk()
root.geometry("600x400")


text = Label(root, text="🟥")
text.place(x=300, y=200)

text = Label(root, text="🟥",
             font=("Consolas", 32, "bold"), fg="white",
             bg="darkblue")
text.place(x=300,y=100)

root.mainloop()
