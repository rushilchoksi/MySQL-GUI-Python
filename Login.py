from tkinter import *
import webbrowser
import os

def RegisterUser():
    UsernameInfo = Username.get()
    PasswordInfo = Password.get()
    file = open(UsernameInfo, "w")
    file.write(UsernameInfo+"\n")
    file.write(PasswordInfo)
    file.close()
    UsernameEntry.delete(0, END)
    PasswordEntry.delete(0, END)
    Label(screen1, text="", bg="#282828").pack()
    Label(screen1, text="Registration successful!", bg="#282828", fg="Green", font=("-family {SF Pro Display} -size 10 -weight bold")).pack()

def Register():
    global screen1
    screen1 = Toplevel(screen)
    screen1.title("Register")
    screen1.configure(background="#282828")
    screen1.geometry("395x290+466+277")
    global Username
    global Password
    global UsernameEntry
    global PasswordEntry
    Username = StringVar()
    Password = StringVar()
    Label(screen1, text="Enter your credentials below", bg="#282828", font=("-family {SF Pro Display} -size 14 -weight bold"), foreground="#ffffff").pack()
    Label(screen1, text="", bg="#282828").pack()
    Label(screen1, text="Username * ", bg="#282828", font=("-family {SF Pro Display} -size 14 -weight bold"), foreground="#ffffff").pack()
    UsernameEntry = Entry(screen1, textvariable = Username)
    UsernameEntry.pack()
    Label(screen1, text="", bg="#282828").pack()
    Label(screen1, text="Password * ", bg="#282828", font=("-family {SF Pro Display} -size 14 -weight bold"), foreground="#ffffff").pack()
    PasswordEntry = Entry(screen1, textvariable = Password)
    PasswordEntry.pack()
    Label(screen1, text="", bg="#282828").pack()
    Button(screen1, text="Register", width = 10, height = 1,  bg="#282828", font=("-family {SF Pro Display} -size 14 -weight bold"), foreground="#ffffff", command=RegisterUser).pack()

def LoginSuccess():
    global screen3
    screen3 = Toplevel(screen)
    screen3.title("Login successful!")
    screen3.configure(background="#282828")
    screen3.geometry("395x290+466+277")
    for i in range(1,5):
        Label(screen3, text="", bg="#282828").pack()
    Label(screen3, text="Login successful!", bg="#282828", fg="Green", font=("-family {SF Pro Display} -size 10 -weight bold")).pack()
    Label(screen3, text="", bg="#282828").pack()
    Label(screen3, text="Click ""OK"" to continue", bg="#282828", fg="#ffffff", font=("-family {SF Pro Display} -size 14 -weight bold")).pack()
    Label(screen3, text="", bg="#282828").pack()
    Button(screen3, text="OK", width = 10, height = 1,  bg="#282828", font=("-family {SF Pro Display} -size 14 -weight bold"), foreground="#ffffff", command=DeleteCorrectLogin).pack()

def IncorrectPassword():
    global screen4
    screen4 = Toplevel(screen)
    screen4.title("Incorrect password!")
    screen4.configure(background="#282828")
    screen4.geometry("395x290+466+277")
    for j in range(1,5):
        Label(screen4, text="", bg="#282828").pack()
    Label(screen4, text="Incorrect password!", bg="#282828", fg="Red", font=("-family {SF Pro Display} -size 10 -weight bold")).pack()
    Label(screen4, text="", bg="#282828").pack()
    Label(screen4, text="Click ""OK"" to continue", bg="#282828", fg="#ffffff", font=("-family {SF Pro Display} -size 14 -weight bold")).pack()
    Label(screen4, text="", bg="#282828").pack()
    Button(screen4, text="OK", width = 10, height = 1,  bg="#282828", font=("-family {SF Pro Display} -size 14 -weight bold"), foreground="#ffffff", command=DeleteIncorrectPassword).pack()

def IncorrectUser():
    global screen5
    screen5 = Toplevel(screen)
    screen5.title("No user ID found!")
    screen5.configure(background="#282828")
    screen5.geometry("395x290+466+277")
    for i in range(1,5):
        Label(screen4, text="", bg="#282828").pack()
    Label(screen5, text="No user ID found!", bg="#282828", fg="Red", font=("-family {SF Pro Display} -size 10 -weight bold")).pack()
    Label(screen5, text="", bg="#282828").pack()
    Label(screen5, text="Click ""OK"" to continue", bg="#282828", fg="#ffffff", font=("-family {SF Pro Display} -size 14 -weight bold")).pack()
    Label(screen5, text="", bg="#282828").pack()
    Button(screen5, text="OK", width = 10, height = 1,  bg="#282828", font=("-family {SF Pro Display} -size 14 -weight bold"), foreground="#ffffff", command=DeleteIncorrectPassword).pack()

def DeleteCorrectLogin():
    screen3.destroy()
    screen2.destroy()
    webbrowser.open("GUI.py")

def DeleteIncorrectPassword():
    screen4.destroy()
    screen2.destroy()

def DeleteIncorrectUser():
    screen5.destroy()
    screen2.destroy()

def LoginVerify():
    Username1 = UsernameVerify.get()
    Password1 = PasswordVerify.get()
    UsernameEntry_1.delete(0, END)
    PasswordEntry_1.delete(0, END)
    ListofFiles = os.listdir('C:\Users\Rushil\Desktop\Python\MySQL - Python - HTML') #Enter the file directory where you registered
    if Username1 in ListofFiles:
        file1 = open(Username1, "r")
        Verify = file1.read().splitlines()
        if Password1 in Verify:
            LoginSuccess()
        else:
            IncorrectPassword()
    else:
        IncorrectUser()

def Login():
    global screen2
    screen2 = Toplevel(screen)
    screen2.title("Login")
    screen2.configure(background="#282828")
    screen2.geometry("395x290+466+277")
    Label(screen2, text="Enter your credentials below to login", bg="#282828", font=("-family {SF Pro Display} -size 14 -weight bold"), foreground="#ffffff").pack()
    Label(screen2, text="", bg="#282828").pack()
    global UsernameVerify
    global PasswordVerify
    UsernameVerify = StringVar()
    PasswordVerify = StringVar()
    global UsernameEntry_1
    global PasswordEntry_1
    Label(screen2, text="Username * ", bg="#282828",  font=("-family {SF Pro Display} -size 14 -weight bold"), foreground="#ffffff").pack()
    UsernameEntry_1 = Entry(screen2, textvariable = UsernameVerify)
    UsernameEntry_1.pack()
    Label(screen2, text="", bg="#282828").pack()
    Label(screen2, text="Password * ", bg="#282828", font=("-family {SF Pro Display} -size 14 -weight bold"), foreground="#ffffff").pack()
    PasswordEntry_1 = Entry(screen2, textvariable = PasswordVerify)
    PasswordEntry_1.pack()
    Label(screen2, text="", bg="#282828").pack()
    Button(screen2, text = "Login", width = 10, height = 1,  bg="#282828", font=("-family {SF Pro Display} -size 14 -weight bold"), foreground="#ffffff", command=LoginVerify).pack()

def main_screen():
    global screen
    screen = Tk()
    screen.geometry("395x290+466+277")
    screen.title("Hello")
    screen.configure(background="#282828")
    Label(text="Welcome to MySQL GUI", bg="#282828", font=("-family {SF Pro Display} -size 14 -weight bold"), foreground="#ffffff").pack()
    Label(text="", bg="#282828").pack()
    Label(text="", bg="#282828").pack()
    Button(text="Login", bg="#282828", font=("-family {SF Pro Display} -size 14 -weight bold"), foreground="#ffffff", height=2, width=30, command = Login).pack()
    Label(text="", bg="#282828").pack()
    Button(text="Register", bg="#282828", font=("-family {SF Pro Display} -size 14 -weight bold"), foreground="#ffffff", height=2, width=30, command = Register).pack()

    screen.mainloop()

main_screen()
