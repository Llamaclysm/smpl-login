from tkinter import *

def default_screen():
    screen = Tk()
    screen.geometry("350x200")
    screen.title("Auth App 0.1")
    Label(text = "Auth App 0.1", bg = "grey", font = ("Calibri", 13)).pack()
    Label(text = "").pack()
    Button(text = "Login").pack()
    Label(text="").pack()
    Button(text = "Register").pack()

    screen.mainloop()

default_screen()
