from tkinter import *
import tkinter.messagebox as msg
import connection
import center_dashboard


class Main:
    def __init__(self):
        self.root = Tk()
        self.root.geometry('900x800')

        self.mainLabel = Label(self.root, text="Center Login", font=('calibri', 28, 'bold'))
        self.mainLabel.pack(pady=20)

        self.f = Frame(self.root)
        self.f.pack(pady=10)

        font = ('calibri', 14)

        self.lb1 = Label(self.f, text='Enter Email', font=font)
        self.txt1 = Entry(self.f, font=font, width=30)
        self.lb1.grid(row=0, column=0, padx=10)
        self.txt1.grid(row=0, column=1, padx=10)

        self.lb2 = Label(self.f, text='Enter Password', font=font)
        self.txt2 = Entry(self.f, font=font, width=30, show='*')
        self.lb2.grid(row=1, column=0, padx=10)
        self.txt2.grid(row=1, column=1, padx=10)

        self.btn = Button(self.root, text='Submit', font=font, command=self.verifyCenter)
        self.btn.pack(pady=10)

        self.root.mainloop()

    def verifyCenter(self):
        email = self.txt1.get()
        password = self.txt2.get()
        conn = connection.connect()
        cr = conn.cursor()
        q = f"select * from center where email='{email}' and password='{password}'"
        cr.execute(q)
        data = cr.fetchall()
        if len(data) == 0:
            msg.showwarning('Warning', 'Invalid Email/Password')
        else:
            msg.showinfo("Success", "Login Successful")
            self.root.destroy()
            center_dashboard.Main(data[0][0])


# obj = Main()
