from tkinter import *
class lbs2kgs(Frame):
    
    def __init__(self, top = None):
        Frame.__init__(self,top)

        self._l = Label(top, text = "Enter lbs to be converted", font=("Verdana", 24), fg="white", bg="black")
        self._l.pack()
        self._b = Button(top, text="CONVERT", activebackground="red", activeforeground="white", command = self.convert)
        self._b.pack()

        self._input = StringVar()
        self._e = Entry(top, width = 20, textvariable = self._input)
        self._e.pack()


        


    def convert(self):
        self._l.config(text = float(self._input.get())* 0.45359237)
        

        






if __name__== "__main__":
    lbs2kgs().mainloop()        
