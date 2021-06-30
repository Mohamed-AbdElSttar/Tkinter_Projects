from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Countdown")
root.geometry("180x180")
root.resizable(False, False)

t=0

def set_timer():
    global t
    t=t+int(myInput.get())
    return t

def countdown():
    global t
    if t>0:
        myLabel.config(text=t)
        t=t-1
        myLabel.after(1000, countdown)
    elif t==0:
        myLabel.config(text="Good")

myLabel = Label(root, font="times 20")
myLabel.grid(row=0, column=2, pady=5)

times=StringVar()
myInput = Entry(root, textvariable=times)
myInput.grid(row=2, column=2, padx=5)

set_button = Button(root, text="Set", width=10, command=set_timer)
set_button.grid(row=3, column=2, padx=20, pady=(5, 0))

start_button = Button(root, text="Start", width=10, command=countdown)
start_button.grid(row=4, column=2, padx=20, pady=5)

root.mainloop()