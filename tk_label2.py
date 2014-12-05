from tkinter import Tk, Label, Button

def hello():
    print("Hello!")

def popUp():
    if True:
        top = Tk()
        lbl = Label(top, text="Boom")
        lbl.pack()
        top.mainloop()
        #popUp()


    
top = Tk()
lbl = Label(top, text = "A Button", font=("Impact", 72), fg="white", bg="black")
lbl.pack()
b = Button(top, text="BOOP", activebackground="red", activeforeground="white", command = popUp)
b.pack()
top.mainloop()

