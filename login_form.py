from tkinter import *
from tkinter import messagebox


def login():
    Username = Entry1.get()
    Password = Entry2.get()

    if (Username == "" and Password == ""):
        messagebox.showinfo("", "Username cannot empty")
    elif (Username == "safaith" and Password == "12345"):
        messagebox.showinfo("", "login success")
    else:
        messagebox.showinfo("Incorrect password")


root = Tk()
root.title("Login-form")
root.geometry("300x200")
global Entry1
global Entry2

Label(root, text="Username").place(x=20, y=20)
Label(root, text="Password").place(x=20, y=70)

Entry1 = Entry(root, bg="white", bd=5)
Entry1.place(x=140, y=20)

Entry2 = Entry(root, bg="white", bd=5)
Entry2.place(x=140, y=70)

Button(root, text="Login", command=login, height=3,
       width=15, bd=6).place(x=100, y=120)

root.mainloop()
