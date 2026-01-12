from tkinter import *
root = Tk()
root.geometry("600x400")
root.title("Окошко")
root["bg"] = "green"

text = Label(root, text="Привет, Мир!")
text.pack()

text = Label(root, text="Привет, Мир!",
             font=("Consolas", 32, "bold"), fg="white",
             bg="darkblue")
text.pack(side='bottom')

text2 = Label(root, text="𓁈𓂀𓋹𓆣𓁀𓀾",
             font=("Consolas", 60, "bold"), fg="darkgreen",
             bg="green")
text2.pack()

def test():
    text2.destroy()

btn = Button(root)
btn.pack()

atv = Button(root, text="Press me!", fg="red", font=("Algerian", 23), command=test)
atv.pack()

btn = Button(root, text="Press me!", fg="tomato2", bg="navajowhite2",
             activeforeground="tomato4", activebackground="navajowhite4", font=(" t", 35))
btn.pack()

root.mainloop()