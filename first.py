from cgitb import text
from tkinter import*
from tkinter.ttk import *
from time import strftime

wi = Tk()
wi.title("clock")
wi.minsize(200, 50)
wi.maxsize(400, 200)


def time():
    clock = strftime("%H :%M :%S %p")
    label.config(text=clock)
    label.after(1000, time)


label = Label(wi, font=("ds-digital,100"),
              background="white", foreground="black")
label.pack(anchor="center")
time()

mainloop()
