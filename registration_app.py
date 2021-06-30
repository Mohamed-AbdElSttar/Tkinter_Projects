from tkinter import *
from PIL import ImageTk, Image
from sqlalchemy.sql.expression import text
import models


root = Tk()
root.title("Learn Tkinter")
root.resizable(False, False)


def delete():
    address = models.session.query(models.Addresses).filter(
        models.Addresses.id == delete_box.get()).one()
    models.session.delete(address)
    models.session.commit()


def save():
    address_record = models.session.query(models.Addresses).filter(
        models.Addresses.id == delete_box.get()).one()

    address_record.first_name = f_name_editor.get()
    address_record.last_name = l_name_editor.get()
    address_record.address = address_editor.get()
    address_record.city = city_editor.get()
    address_record.state = state_editor.get()
    address_record.zipcode = zipcode_editor.get()

    models.session.commit()
    editor.destroy()


def edit():
    global editor
    editor = Tk()
    editor.title("Learn Tkinter")
    editor.resizable(False, False)

    address_record = models.session.query(models.Addresses).filter(
        models.Addresses.id == delete_box.get()).one()

    global f_name_editor
    f_name_editor = Entry(editor, width=30)
    f_name_editor.grid(row=0, column=1, padx=20, pady=(10, 0))

    global l_name_editor
    l_name_editor = Entry(editor, width=30)
    l_name_editor.grid(row=1, column=1)

    global address_editor
    address_editor = Entry(editor, width=30)
    address_editor.grid(row=2, column=1)

    global city_editor
    city_editor = Entry(editor, width=30)
    city_editor.grid(row=3, column=1)

    global state_editor
    state_editor = Entry(editor, width=30)
    state_editor.grid(row=4, column=1)

    global zipcode_editor
    zipcode_editor = Entry(editor, width=30)
    zipcode_editor.grid(row=5, column=1)

    f_name_editor.insert(0, address_record.first_name)
    l_name_editor.insert(0, address_record.last_name)
    address_editor.insert(0, address_record.address)
    city_editor.insert(0, address_record.city)
    state_editor.insert(0, address_record.state)
    zipcode_editor.insert(0, address_record.zipcode)

    f_name_label = Label(editor, text="First Name : ")
    f_name_label.grid(row=0, column=0)

    l_name_label = Label(editor, text="Last Name : ")
    l_name_label.grid(row=1, column=0)

    address_label = Label(editor, text="Address : ")
    address_label.grid(row=2, column=0)

    city_label = Label(editor, text="City : ")
    city_label.grid(row=3, column=0)

    state_label = Label(editor, text="State : ")
    state_label.grid(row=4, column=0)

    zipcode_label = Label(editor, text="Zipcode : ")
    zipcode_label.grid(row=5, column=0)

    btn_save = Button(editor, text="save", command=save)
    btn_save.grid(row=6, column=0, columnspan=2, padx=10, pady=10, ipadx=100)


def submit():

    address_instance = models.Addresses(first_name=f_name.get(), last_name=l_name.get(
    ), address=address.get(), city=city.get(), state=state.get(), zipcode=zipcode.get())
    models.session.add(address_instance)
    models.session.commit()

    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)


f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20, pady=(10, 0))

l_name = Entry(root, width=30)
l_name.grid(row=1, column=1)

address = Entry(root, width=30)
address.grid(row=2, column=1)

city = Entry(root, width=30)
city.grid(row=3, column=1)

state = Entry(root, width=30)
state.grid(row=4, column=1)

zipcode = Entry(root, width=30)
zipcode.grid(row=5, column=1)

delete_box = Entry(root, width=30)
delete_box.grid(row=9, column=1)


f_name_label = Label(root, text="First Name : ")
f_name_label.grid(row=0, column=0)

l_name_label = Label(root, text="Last Name : ")
l_name_label.grid(row=1, column=0)

address_label = Label(root, text="Address : ")
address_label.grid(row=2, column=0)

city_label = Label(root, text="City : ")
city_label.grid(row=3, column=0)

state_label = Label(root, text="State : ")
state_label.grid(row=4, column=0)

zipcode_label = Label(root, text="Zipcode : ")
zipcode_label.grid(row=5, column=0)

delete_box_label = Label(root, text="Enter record ID : ")
delete_box_label.grid(row=9, column=0)

btn = Button(root, text="submit", command=submit)
btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)


def query():
    addresses = models.session.query(models.Addresses).all()
    # print(addresses)
    records = ""
    for i, address in enumerate(addresses):
        if i == len(list(addresses))-1:
            records += str(address.id) + " " + address.first_name + " " + \
                address.last_name + " " + address.address + " " + address.city + \
                " " + address.state + " " + str(address.zipcode)
        else:
            records += str(address.id) + " " + address.first_name + " " + \
                address.last_name + " " + address.address + " " + address.city + \
                " " + address.state + " " + str(address.zipcode) + "\n"

    global result_label
    result_label.grid_forget()
    result_label = Label(root, text=str(records))
    result_label.grid(row=8, column=0, columnspan=2)


query_btn = Button(root, text="Show Records", command=query)
query_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=77)

delete_btn = Button(root, text="Delete Record", command=delete)
delete_btn.grid(row=10, column=0, columnspan=2, pady=10, padx=10, ipadx=75)

edit_btn = Button(root, text="Edit Record", command=edit)
edit_btn.grid(row=11, column=0, columnspan=2, pady=10, padx=10, ipadx=85)

result_label = Label(root, text="")
result_label.grid(row=8, column=0, columnspan=2)

root.mainloop()
