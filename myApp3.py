from tkinter import *

class MyApp2(Frame):

    def __init__(self, top = None):
        Frame.__init__(self,top)
        self._l = Label(top, text = "Choice", font=("Impact", 72), fg="white", bg="black")
        self._l.pack()
        self._b = Button(top, text="BOOP", activebackground="red", activeforeground="white", command = self.hello)
        self._b.pack()

        self._decision = StringVar()
        self._decision.set("No")
        
        self._r1 = Radiobutton(top, text = "izzit?", variable = self._decision, value = "Yes")
        self._r1.pack(side = LEFT)
        self._r2 = Radiobutton(top, text = "'haps", variable = self._decision, value = "Maybe")
        self._r2.pack(side = LEFT)
        self._r3 = Radiobutton(top, text = "nah!", variable = self._decision, value = "No")
        self._r3.pack(side = LEFT)

        self._input = StringVar()
        self._e = Entry(top, width = 10, textvariable = self._input)
        self._e.pack()


        
        
    def hello(self):
        self._l.config(text = self._input.get())


if __name__== "__main__":
    MyApp2().mainloop()
        
