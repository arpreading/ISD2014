from tkinter import Tk, Label

top = Tk()
lbl = Label(top, text = "Hello World", font=("Impact", 72), fg="Blue", bg="black")
lbl.pack()
top.title("My First GUI")
top.minsize(480,140)
top.mainloop()
