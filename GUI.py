#
#File: GUI.py
#Author: Rushil Choksi
#Description: Internship Assessment Evaluation
#Program Hash(SHA256): F48D15338FD0728A8E6F198101397047AA64E6E25FCC5A25DAF7FF1834BB0915
#Program Hash(MD5): 104C1E1D512584EA0015CEAB5C3E9239
#

import os
import sys
import csv
import time
import webbrowser
from tkinter import messagebox 

try:
    import mysql.connector
except ImportError:
    print ("Module not found!")

try:
    from mysql.connector import Error
except ImportError:
    print ("Module not found!")

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import GUI_support
from tkinter import *

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Main (root)
    GUI_support.init(root, top)
    root.mainloop()

w = None
def create_Main(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    top = Main (w)
    GUI_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Main():
    global w
    w.destroy()
    w = None

class Main:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#d9d9d9' # X11 color: 'gray85'
        font9 = "-family {Segoe UI} -size 9"

        top.geometry("395x290+466+277")
        top.title("MySQL GUI - Rushil")
        top.configure(background="#282828")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.WelcomeMessage = tk.Message(top)
        self.WelcomeMessage.place(relx=0.051, rely=0.017, relheight=0.186
                , relwidth=0.894)
        self.WelcomeMessage.configure(background="#282828")
        self.WelcomeMessage.configure(font="-family {SF Pro Display} -size 14 -weight bold")
        self.WelcomeMessage.configure(foreground="#ffffff")
        self.WelcomeMessage.configure(highlightbackground="#d9d9d9")
        self.WelcomeMessage.configure(highlightcolor="black")
        self.WelcomeMessage.configure(text='''Welcome to MySQL GUI''')
        self.WelcomeMessage.configure(width=353)

        self.menubar = tk.Menu(top, font=('Segoe UI', 9, ), bg=_bgcolor
                ,fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.conFrame = tk.Frame(top)
        self.conFrame.place(relx=0.076, rely=0.207, relheight=0.707
                , relwidth=0.848)
        self.conFrame.configure(relief='groove')
        self.conFrame.configure(borderwidth="2")
        self.conFrame.configure(relief="groove")
        self.conFrame.configure(background="#282828")
        self.conFrame.configure(width=335)

        self.ActionMessage = tk.Message(self.conFrame)
        self.ActionMessage.place(relx=0.224, rely=0.024, relheight=0.263
                , relwidth=0.546)
        self.ActionMessage.configure(background="#282828")
        self.ActionMessage.configure(font="-family {SF Pro Display} -size 14 -weight bold")
        self.ActionMessage.configure(foreground="#ffffff")
        self.ActionMessage.configure(highlightbackground="#d9d9d9")
        self.ActionMessage.configure(highlightcolor="black")
        self.ActionMessage.configure(text='''Select your action.''')
        self.ActionMessage.configure(width=183)

        self.chooseDB = tk.Button(self.conFrame)
        self.chooseDB.place(relx=0.134, rely=0.463, height=38, width=250)
        self.chooseDB.configure(activebackground="#d9d9d9")
        self.chooseDB.configure(activeforeground="#000000")
        self.chooseDB.configure(background="#282828")
        self.chooseDB.configure(disabledforeground="#a3a3a3")
        self.chooseDB.configure(font="-family {SF Pro Display} -size 14 -weight bold")
        self.chooseDB.configure(foreground="#ffffff")
        self.chooseDB.configure(highlightbackground="#d9d9d9")
        self.chooseDB.configure(highlightcolor="black")
        self.chooseDB.configure(pady="0")
        self.chooseDB.configure(width=50)
        self.chooseDB.configure(text='''Use an existing database''')
        self.chooseDB.configure(command=self.ExistingDB)

        self.createDB = tk.Button(self.conFrame)
        self.createDB.place(relx=0.134, rely=0.707, height=38, width=250)
        self.createDB.configure(activebackground="#d9d9d9")
        self.createDB.configure(activeforeground="#000000")
        self.createDB.configure(background="#282828")
        self.createDB.configure(disabledforeground="#a3a3a3")
        self.createDB.configure(font="-family {SF Pro Display} -size 14 -weight bold")
        self.createDB.configure(foreground="#ffffff")
        self.createDB.configure(highlightbackground="#d9d9d9")
        self.createDB.configure(highlightcolor="black")
        self.createDB.configure(pady="0")
        self.createDB.configure(text='''Create a new database''')
        self.createDB.configure(command=self.CreateDB)

    def ExistingDB(self):
        global dbEntry
        self.screen = Toplevel(root)
        self.screen.title("MySQL GUI - Rushil")
        self.screen.geometry("395x310+466+277")
        self.screen.configure(background="#282828")
        self.screen.configure(highlightbackground="#d9d9d9")
        self.screen.configure(highlightcolor="black")
        Label(self.screen, text="", bg="#282828").pack()
        Label(self.screen, text="Choose your database from", bg="#282828", font=("-family {SF Pro Display} -size 14 -weight bold"), foreground="#ffffff").pack()
        Label(self.screen, text="the list below", bg="#282828", font=("-family {SF Pro Display} -size 14 -weight bold"), foreground="#ffffff").pack()
        Label(self.screen, text="", bg="#282828").pack()
        Label(self.screen, text="Available databases are:", bg="#282828", font=("-family {SF Pro Display} -size 12 -weight bold"), foreground="Green").pack()
        self.Database = StringVar()
        self.CheckDB()
        List = open("Database.txt").readlines()
        variable = StringVar(root)
        variable.set(List[0])
        variable.trace("w", self.CheckDB)
        dbMenu = OptionMenu(self.screen,variable, *List)
        dbMenu.configure(font="-family {SF Pro Display} -size 12 -weight bold")
        dbMenu.configure(width=14, height=1)
        dbMenu.configure(anchor=NW)
        dbMenu.pack()
        Label(self.screen, text="", bg="#282828").pack()
        Label(self.screen, text="Type below the desired database", bg="#282828", font=("-family {SF Pro Display} -size 12 -weight bold"), foreground="White").pack()
        dbEntry = Entry(self.screen, textvariable=self.Database)
        dbEntry.pack()
        Label(self.screen, text="", bg="#282828").pack()
        Button(self.screen, text="Enter", width = 10, height = 1,  bg="#282828", font=("-family {SF Pro Display} -size 14 -weight bold"), foreground="#ffffff", command=self.SetDB).pack()

    def CheckDB(self, *args):
        Connection = mysql.connector.connect(host = "localhost", user = "root", passwd = "root")
        mycursor = Connection.cursor()
        mycursor.execute("show databases")
        result=mycursor.fetchall()
        fp=open("Database.txt","w")
        myFile=csv.writer(fp)
        myFile.writerows(result)
        fp.close()
        Connection.close()

    def SetDB(self, *args):
        global DatabaseInfo
        try:
            DatabaseInfo = self.Database.get()
            Connection_1 = mysql.connector.connect(host = "localhost", user = "root", passwd = "root")
            mycursor = Connection_1.cursor()
            mycursor.execute("use "+str(DatabaseInfo))
            messagebox.showinfo("MySQL GUI - Rushil", "Database successfully set to "+DatabaseInfo+"! Click ""OK"" to continue.")
            Connection_1.close()
            self.Query()
        except Error:
            messagebox.showinfo("MySQL GUI - Rushil", "No Database "+DatabaseInfo+ "found! Click ""OK"" to continue.")

    def CreateDB(self):
        global dbNameEntry
        self.screen1 = Toplevel(root)
        self.screen1.title("MySQL GUI - Rushil")
        self.screen1.geometry("395x310+466+277")
        self.screen1.configure(background="#282828")
        self.screen1.configure(highlightbackground="#d9d9d9")
        self.screen1.configure(highlightcolor="black")
        self.NewDB = StringVar()
        self.screen1 = Toplevel(root)
        self.screen1.title("MySQL GUI - Rushil")
        self.screen1.geometry("395x310+466+277")
        self.screen1.configure(background="#282828")
        self.screen1.configure(highlightbackground="#d9d9d9")
        self.screen1.configure(highlightcolor="black")
        Label(self.screen1, text="Enter database name below", bg="#282828", font=("-family {SF Pro Display} -size 14 -weight bold"), foreground="#ffffff").pack()
        dbName = StringVar()
        Label(self.screen1, text="", bg="#282828").pack()
        Label(self.screen1, text="", bg="#282828").pack()
        dbNameEntry = Entry(self.screen1, textvariable=self.NewDB)
        dbNameEntry.pack()
        Label(self.screen1, text="", bg="#282828").pack()
        Button(self.screen1, text="Create",  width = 10, height = 1,  bg="#282828", font=("-family {SF Pro Display} -size 14 -weight bold"), foreground="#ffffff", command=self.CreateNewDB).pack()

    def CreateNewDB(self, *args):
        global NewDatabaseName
        NewDatabaseName = self.NewDB.get()
        Connection_2 = mysql.connector.connect(host = "localhost", user = "root", passwd = "root")
        mycursor = Connection_2.cursor()
        mycursor.execute("create database "+str(NewDatabaseName))
        messagebox.showinfo("MySQL GUI - Rushil", "Database "+NewDatabaseName+" created successfully! Click ""OK"" to continue.")
        self.MySQLQuery = StringVar()
        ExecuteQuery = self.MySQLQuery.get()
        mycursor.execute(ExecuteQuery)
        self.Query()
        Connection_2.close()

    def Query(self):
        global queryEntry
        self.screen2 = Toplevel(root)
        self.screen2.title("MySQL GUI - Rushil")
        self.screen2.geometry("395x310+466+277")
        self.screen2.configure(background="#282828")
        self.screen2.configure(highlightbackground="#d9d9d9")
        self.screen2.configure(highlightcolor="black")
        self.MySQLQuery = StringVar()
        Label(self.screen2, text="", bg="#282828").pack()
        Label(self.screen2, text="Enter your query here", bg="#282828", font=("-family {SF Pro Display} -size 14 -weight bold"), foreground="#ffffff").pack()
        Label(self.screen2, text="", bg="#282828").pack()
        Label(self.screen2, text="", bg="#282828").pack()
        queryEntry = Entry(self.screen2, textvariable=self.MySQLQuery)
        queryEntry.pack()
        Label(self.screen2, text="", bg="#282828").pack()
        Button(self.screen2, text="Enter",   width = 10, height = 1,  bg="#282828", font=("-family {SF Pro Display} -size 14 -weight bold"), foreground="#ffffff", command=self.ExecuteQueryHTML).pack()

    def ExecuteQueryHTML(self):
        print ("Running!")
        try:
            Connection_3 = mysql.connector.connect(user = "root", host = '127.0.0.1', passwd = "root", database = "test")
            mycursor = Connection_3.cursor()
            result=mycursor.fetchall()
            f=open("File.txt","a")
            myFile=csv.writer(f)
            myFile.writerows(result)
            f.close()
            print ("\nData successfully fetched!")
            os.rename("File.txt","File.html")
            print ("Opening HTML page in 3 seconds!")
            time.sleep(3)
            webbrowser.open("File.html")
            Connection_3.close()
            os.remove("File.txt")
            os.remove("File.html")
            return Connection_3
        except Error:
            print ("There's an error! Opening CLI Window Interface in 3 seconds")
            time.sleep(3)
            os.system("MySQL.py")


if __name__ == '__main__':
    vp_start_gui()
