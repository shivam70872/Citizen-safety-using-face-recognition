from tkinter import *
import tkinter.messagebox as msg
from connection import connect
import admin_dashboard


class main():
    def __init__(self):
        self.root = Tk()
        self.root.geometry('800x900')

        self.mainlabel = Label(self.root, text='Login', font=('ariel', 24, 'bold', 'underline'))
        self.mainlabel.pack(pady=20)

        self.f = Frame(self.root)
        self.f.pack(pady=10)

        self.lb1 = Label(self.f, text="Enter Email", font=('ariel', 14))
        self.lb1.grid(row=0, column=0)

        self.txt1 = Entry(self.f, font=('ariel', 14), width=30)
        self.txt1.grid(row=0, column=1)

        self.lb2 = Label(self.f, text="Enter password", font=('ariel', 14))
        self.lb2.grid(row=1, column=0)

        self.txt2 = Entry(self.f, font=('ariel', 14), show="*", width=30)
        self.txt2.grid(row=1, column=1)

        self.btn = Button(self.root, text='Submit', command=self.verifyadmin)
        self.btn.pack(pady=10)

        self.root.mainloop()

    def verifyadmin(self):
        email = self.txt1.get()
        password = self.txt2.get()
        conn = connect()
        cr = conn.cursor()
        q = f"select * from admin where email='{email}' and password='{password}'"
        cr.execute(q)
        data = cr.fetchall()
        if len(data) == 0:
            msg.showwarning('alert', 'Invalid Email/Password')

            self.txt2.delete(0, 'end')
        else:
            msg.showinfo('Sucess', 'Login Sucessful')
            self.txt1.delete(0, 'end')
            self.txt2.delete(0, 'end')
            self.root.destroy()
            admin_dashboard.Main()


#x = main()
