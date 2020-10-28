from Data.tkinter_gui_file import *
from tkinter import *
import os

# Designing first window showing login and register.

def login_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("400x350")
    main_screen.iconbitmap(r'Data' + os.path.sep + 'logo.ico')
    main_screen.title("AIA Account Login")
    main_screen.configure(bg="#8B8BFB")
    Label(text="Select Your Choice", bg="light blue", width="300", height="3", font=("Times New Roman", 15)).pack()
    Label(text="", bg="#8B8BFB").pack()
    Label(text="", bg="#8B8BFB").pack()
    Button(text="Login",bg="light blue", height="2", width="30", command=login,font=("Times New Roman", 12)).pack()
    Label(text="", bg="#8B8BFB").pack()
    Button(text="Register",bg="light blue", height="2", width="30", command=register,font=("Times New Roman", 12)).pack()
    Label(text="", bg="#8B8BFB").pack()
    main_screen.mainloop()

# Designing registration window with username and password

def register():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Register")
    register_screen.geometry("400x350")
    register_screen.iconbitmap(r'Data' + os.path.sep + 'logo.ico')
    register_screen.configure(bg="#8B8BFB")
    Label(register_screen, text="Please enter details below", bg="light blue", width="300", height="3", font=("Times New Roman", 15)).pack()
    Label(register_screen, text="", bg="#8B8BFB").pack()
    Label(register_screen, text="", bg="#8B8BFB").pack()

    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()

    username_lable = Label(register_screen, text="Username ", bg="light blue", font=("Times New Roman", 12))
    username_lable.pack()
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()
    Label(register_screen, text="", bg="#8B8BFB").pack()
    password_lable = Label(register_screen, text="Password ",bg="light blue", font=("Times New Roman", 12))
    password_lable.pack()
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()
    Label(register_screen, text="", bg="#8B8BFB").pack()
    Button(register_screen, text="Register", width=10, height=1, bg="white", command=register_user).pack()


# Implementing functionality to the register window

def register_user():
    username_info = username.get()
    password_info = password.get()

    if not os.path.exists('Data' + os.path.sep + "login_info" + os.path.sep):
        os.makedirs('Data' + os.path.sep + "login_info" + os.path.sep)
    file = open('Data' + os.path.sep + "login_info" + os.path.sep + username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()

    username_entry.delete(0, END)
    password_entry.delete(0, END)

    Label(register_screen, text="Registration Success", fg="green", bg="light blue", font=("calibri", 11)).pack()


# Designing login window

def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("400x350")
    login_screen.iconbitmap(r'Data' + os.path.sep + 'logo.ico')
    login_screen.configure(bg="#8B8BFB")
    Label(login_screen, text="Please enter details below", bg="light blue", width="300", height="3",font=("Times New Roman", 15)).pack()
    Label(login_screen, text="", bg="#8B8BFB").pack()
    Label(login_screen, text="", bg="#8B8BFB").pack()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_login_entry
    global password_login_entry

    Label(login_screen, text="Username ", bg="light blue", font=("Times New Roman", 12)).pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="", bg="#8B8BFB").pack()
    Label(login_screen, text="Password ", bg="light blue", font=("Times New Roman", 12)).pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show='*')
    password_login_entry.pack()
    Label(login_screen, text="", bg="#8B8BFB").pack()
    Button(login_screen, text="Login", width=10, height=1, command=login_verify).pack()


# Implementing event on login button

def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)

    if not os.path.exists('Data' + os.path.sep + "login_info" + os.path.sep):
        os.makedirs('Data' + os.path.sep + "login_info" + os.path.sep)

    list_of_files = os.listdir('Data' + os.path.sep + 'login_info' + os.path.sep)
    if username1 in list_of_files:
        file1 = open('Data' + os.path.sep + 'login_info' + os.path.sep + username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            Label(login_screen, text="Login Success").pack()
            login_screen.destroy()
            main_screen.destroy()
            main()
            # login_sucess

        else:
            Label(login_screen, text="Invalid Password ").pack()
            # password_not_recognised

    else:
        Label(login_screen, text="User Not Found").pack()
        # user_not_found



