from tkinter import *

def write_user():
    username_usr = username.get()
    username_pwd = password.get()

    file=open(username_usr+".txt", "w")
    file.write(username_usr+"\n")
    file.write(username_pwd)
    file.close()

    username_usr_entry.delete(0, END)
    username_pwd_entry.delete(0, END)

    Label(screen_register, text = "Data saved!", fg = "green")

def register():
    screen_register = Toplevel(screen)
    screen_register.title("Register")
    screen_register.geometry("350x250")
    global screen_register

    username = StringVar()
    global username
    password = StringVar()
    global password

    Label(screen_register, text="Fill the registration form:").pack()
    Label(screen_register, text="").pack()
    Label(screen_register, text="Username").pack()
    username_usr_entry = Entry(screen_register, textvariable = username)
    username_usr_entry.pack()
    global username_usr_entry
    Label(screen_register, text="Password").pack()
    username_pwd_entry = Entry(screen_register, textvariable = password)
    username_pwd_entry.pack()
    global username_pwd_entry
    Label(screen_register, text="").pack()
    Button(screen_register, text="SAVE", command=write_user).pack()


def login():
    print("login!")


def default_screen():
    screen = Tk()
    screen.geometry("350x250")
    screen.title("Auth App 0.1")
    global screen
    Label(text = "Auth App 0.1", font = ("Calibri", 14)).pack()
    Label(text = "").pack()
    Button(text = "Login", command = login).pack()
    Label(text="").pack()
    Button(text = "Register", command = register).pack()

    screen.mainloop()

default_screen()