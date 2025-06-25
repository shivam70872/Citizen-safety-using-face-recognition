
from tkinter import *
import center_login
import loginadmin


class Main:
    def __init__(self):
        self.root=Tk()
        self.root.title("Main Login Page")
        self.root.geometry('800x900')
        self.lb1=Label(self.root, text="Login Page",font=("calibri",30,"bold"))
        self.lb1.pack(padx=10,pady=10)

        self.fr=Frame(self.root)
        self.fr.pack(pady=20)

        self.btn1=Button(self.fr,text="Admin Login", font=("calibri", 25,"bold"),command=self.admin)
        self.btn1.grid(row=0,column=0)
        self.btn1.configure(anchor=CENTER)

        self.btn2 = Button(self.fr, text="Center Login", font=("calibri", 25,"bold"),command=self.center)
        self.btn2.grid(row=0, column=3)
        self.btn1.configure(anchor=CENTER)



        self.root.mainloop()

    def center(self):
        center_login.Main()

    def admin(self):
        loginadmin.main()

obj=Main()