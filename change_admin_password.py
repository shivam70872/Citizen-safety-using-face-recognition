import tkinter
import tkinter.ttk
import tkinter.messagebox
import connection

class Main:
    def log(self):
        email = self.tx1.get()
        password = self.tx2.get()
        newPass = self.tx3.get()
        cr = connection.conn.cursor()
        q = f"select * from admin where '{email}'=email and '{password}'=password "
        cr.execute(q)
        data=cr.fetchall()
        connection.conn.commit()
        if len(data) == 0:
            tkinter.messagebox.showwarning("Warning", "plaese type correct details")
        else:
            q = f"update admin set password='{newPass}' where email='{email}'"
            cr.execute(q)
            connection.conn.commit()
            tkinter.messagebox.showinfo("Success", "Password Changed successfully")
            self.root.destroy()
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.state("zoomed")
        self.lb = tkinter.Label(self.root,text="Change Password", font=("calibri", 20, "bold"))
        self.lb.pack(pady=10)
        self.f = tkinter.Frame(self.root)
        self.f.pack(pady=10)
        self.lb1 = tkinter.Label(self.f, text="Enter Email", font=("calibri",10))
        self.tx1 = tkinter.Entry(self.f, width=30)
        self.lb1.grid(row=0,column=0,padx=10,pady=10)
        self.tx1.grid(row=0,column=1,padx=10,pady=10)
        self.lb2 = tkinter.Label(self.f, text="Enter Old password", font=("calibri", 10))
        self.tx2 = tkinter.Entry(self.f, width=30)
        self.lb2.grid(row=1, column=0, padx=10, pady=10)
        self.tx2.grid(row=1, column=1, padx=10, pady=10)

        self.lb3 = tkinter.Label(self.f, text="Enter New password", font=("calibri", 10))
        self.tx3 = tkinter.Entry(self.f, width=30)
        self.lb3.grid(row=2, column=0, padx=10, pady=10)
        self.tx3.grid(row=2, column=1, padx=10, pady=10)
        self.bt1 = tkinter.Button(self.f,text="Submit",font=("calibri",10),command=self.log)
        self.bt1.grid(row =3, column=2,pady=10,padx=10 )

        self.root.mainloop()


obj = Main()

