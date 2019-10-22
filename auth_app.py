from tkinter import *

def register():
    print("registered!")


def login():
    print("login!")


def default_screen():
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
