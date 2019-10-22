from tkinter import *

def register():
    screen_register = Toplevel(screen)
    screen_register.title("Register")
    screen_register.geometry("350x200")
    print("registered!")

    username = StringVar()
    password = StringVar()


def login():
    print("login!")


def default_screen():
    global screen
    screen = Tk()
    screen.geometry("350x200")
    screen.title("Auth App 0.1")
    Label(text = "Auth App 0.1", font = ("Calibri", 14)).pack()
    Label(text = "").pack()
    Button(text = "Login", command = login()).pack()
    Label(text="").pack()
    Button(text = "Register", command = register()).pack()

    screen.mainloop()

default_screen()
