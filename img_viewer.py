from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title("Image Viewer")

imgs_names = ["1.jpg", "2.jpg", "3.jpg", "4.jpg", "5.jpg"]
imgs = []
for i in range(0, len(imgs_names)):
    imgs.append(ImageTk.PhotoImage(Image.open(
        "images/"+imgs_names[i]).resize((450, 350))))

status = Label(root, text="Image 1 of " + str(len(imgs)),
               bd=1, relief=SUNKEN, anchor=E)


def back(image_number):
    global my_label
    global btn_forword
    global btn_back
    global status

    my_label.grid_forget()
    status.grid_forget()
    my_label = Label(image=imgs[image_number - 1])
    my_label.grid(row=0, column=0, columnspan=3)
    btn_back = Button(
        root, text="<<<", command=lambda: back(image_number-1))
    if(image_number-1 <= 0):
        btn_back = Button(root, text="<<<", state=DISABLED)
    else:
        btn_back = Button(
            root, text="<<<", command=lambda: back(image_number-1))
    btn_forword = Button(root, text=">>>",
                         command=lambda: forword(image_number+1))

    btn_back.grid(row=1, column=0)
    btn_forword.grid(row=1, column=2)
    status = Label(root, text="Image " + str(image_number) + " of " + str(len(imgs)),
                   bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)


def forword(image_number):
    global my_label
    global btn_forword
    global btn_back
    global status

    my_label.grid_forget()
    status.grid_forget()
    my_label = Label(image=imgs[image_number - 1])
    my_label.grid(row=0, column=0, columnspan=3)
    btn_forword = Button(
        root, text=">>>", command=lambda: forword(image_number+1))
    if(image_number >= len(imgs)):
        btn_forword = Button(root, text=">>>", state=DISABLED)
    else:
        btn_forword = Button(
            root, text=">>>", command=lambda: forword(image_number+1))
    btn_back = Button(root, text="<<<",
                      command=lambda: back(image_number-1))

    btn_back.grid(row=1, column=0)
    btn_forword.grid(row=1, column=2)
    status = Label(root, text="Image " + str(image_number) + " of " + str(len(imgs)),
                   bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)


btn_back = Button(root, text="<<<", state=DISABLED)
btn_exit = Button(root, text="Exit", command=root.quit)
btn_forword = Button(root, text=">>>", command=lambda: forword(2))

btn_back.grid(row=1, column=0)
btn_exit.grid(row=1, column=1)
btn_forword.grid(row=1, column=2, pady=10)


my_label = Label(image=imgs[0])
my_label.grid(row=0, column=0, columnspan=3)

status.grid(row=2, column=0, columnspan=3, sticky=W+E)

root.mainloop()
