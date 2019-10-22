from tkinter import *

def write():
    print("saved!")


def register():
    screen_register = Toplevel(screen)
    screen_register.title("Register")
    screen_register.geometry("350x200")
    print("registered!")

    username = StringVar()
    password = StringVar()

    Label(screen_register, text="").pack()
    Label(screen_register, text="Fill the registration form:").pack()
    Label(screen_register, text="").pack()
    Label(screen_register, text="Username").pack()
    Entry(screen_register, textvariable = username)
    Label(screen_register, text="Password").pack()
    Entry(screen_register, textvariable = password)
    Button(screen_register, text="SAVE", command=write).pack()

def login():
    print("login!")


def default_screen():
    global screen
    screen = Tk()
    screen.geometry("350x200")
    screen.title("Auth App 0.1")
    Label(text = "Auth App 0.1", font = ("Calibri", 14)).pack()
    Label(text = "").pack()
    Button(text = "Login", command = login).pack()
    Label(text="").pack()
    Button(text = "Register", command = register).pack()

    screen.mainloop()

default_screen()
