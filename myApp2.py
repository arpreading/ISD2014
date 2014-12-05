from tkinter import Tk, Label, Button, Frame

class MyApp2(Frame):

    def __init__(self, top = None):
        Frame.__init__(self,top)
        self._l = Label(top, text = "A Button", font=("Impact", 72), fg="white", bg="black")
        self._l.pack()
        self._b = Button(top, text="BOOP", activebackground="red", activeforeground="white", command = self.hello)
        self._b.pack()
        
    def hello(self):
        print("Hello!")


if __name__== "__main__":
    MyApp2().mainloop()
        
