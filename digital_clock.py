from tkinter import *
from PIL import ImageTk, Image
import time


def times():
    current_time = time.strftime("%H:%M:%S")
    clock.config(text=current_time)
    clock.after(200, times)


root = Tk()
root.title("Digital Clock")
root.geometry("300x200")
root.resizable(False, False)

clock = Label(root, font=("times", 50, "bold"))
clock.grid(row=2, column=2, pady=(15, 0), padx=20)
times()

digi = Label(root, text="Digital Clock", font=(
    "times", 25, "bold"))
digi.grid(row=0, column=2, pady=(20, 0))

labels = Label(root, text="   houres   minutes   seconds   ",
               font=("times 15 bold"))
labels.grid(row=3, column=2)

root.mainloop()
