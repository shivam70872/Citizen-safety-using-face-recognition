import tkinter
import tkinter.ttk
import tkinter.messagebox
from connection import connect

class Main:
    def log(self):
        email = self.tx1.get()
        password = self.tx2.get()
        newPass = self.tx3.get()
        conn = connect()
        cr = conn.cursor()
        q = f"select * from admin where '{email}'=email and '{password}'=password "
        cr.execute(q)
        data = cr.fetchall()
        conn.commit()
        if len(data) == 0:
            tkinter.messagebox.showwarning("Warning", "please type correct details")
        else:
            q = f"update admin set password='{newPass}' where email='{email}'"
            cr.execute(q)
            conn.commit()
            tkinter.messagebox.showinfo("Success", "Password Changed successfully")
            self.root.destroy()
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.geometry('800x900')
        self.lb = tkinter.Label(self.root,text="Change Password", font=("arial", 30, "bold"))
        self.lb.pack(pady=10)
        self.f = tkinter.Frame(self.root)
        self.f.pack(pady=10)
        self.lb1 = tkinter.Label(self.f, text="Enter Email")
        self.tx1 = tkinter.Entry(self.f, width=30)
        self.lb1.grid(row=0, column=0, pady=10)
        self.tx1.grid(row=0, column=1, pady=10)
        self.lb2 = tkinter.Label(self.f, text="Enter Old password")
        self.tx2 = tkinter.Entry(self.f, width=30)
        self.lb2.grid(row=1, column=0, pady=10)
        self.tx2.grid(row=1, column=1, pady=10)

        self.lb3 = tkinter.Label(self.f, text="Enter New password")
        self.tx3 = tkinter.Entry(self.f, width=30)
        self.lb3.grid(row=2, column=0, pady=10)
        self.tx3.grid(row=2, column=1, pady=10)
        self.bt1 = tkinter.Button(self.f, text="Submit", command=self.log)
        self.bt1.grid(row=3, column=1, pady=10)

        self.root.mainloop()


# obj = Main()

