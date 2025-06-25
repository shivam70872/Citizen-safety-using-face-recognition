from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as msg
from connection import connect, verifyMobile, verifyEmail


class main():

    def __init__(self):
        self.root=Tk()
        self.root.geometry("800x900")

        self.heading=Label(self.root,text="Register Your Center",font=("calibri",28,"bold","underline"))
        self.heading.pack()

        self.f=Frame(self.root)
        self.f.pack(pady=20)


        font=("calibri",14)
        self.lb1=Label(self.f, text="Enter Name", font=font)
        self.lb1.grid(row=0,column=0)

        self.txt1 = Entry(self.f, width=40)
        self.txt1.grid(row=0, column=1)

        self.lb2 = Label(self.f, text=" Enter Email", font=font)
        self.lb2.grid(row=1, column=0)

        self.txt2 = Entry(self.f, width=40)
        self.txt2.grid(row=1, column=1)

        self.lb3 = Label(self.f, text=" Enter Mobile", font=font)
        self.lb3.grid(row=2, column=0)

        self.txt3 = Entry(self.f, width=40)
        self.txt3.grid(row=2, column=1)

        self.lb4 = Label(self.f, text=" Enter Incharge Name", font=font)
        self.lb4.grid(row=3, column=0)

        self.txt4 = Entry(self.f, width=40)
        self.txt4.grid(row=3, column=1)

        self.lb5 = Label(self.f, text=" Enter Password", font=font)
        self.lb5.grid(row=4, column=0)

        self.txt5 = Entry(self.f, width=40, show='*')
        self.txt5.grid(row=4, column=1)

        self.lb6 = Label(self.f, text="Select Location", font=font)
        self.lb6.grid(row=5, column=0)

        self.txt6 = ttk.Combobox(self.f, width=40, values=self.get_values1(), state="readonly")
        self.txt6.grid(row=5, column=1)

        self.lb7 = Label(self.f, text="Select Area", font=font)
        self.lb7.grid(row=6, column=0)

        self.txt7 = ttk.Combobox(self.f, width=40, values=self.get_values(), state="readonly")
        self.txt7.grid(row=6, column=1)

        self.status = 0


        self.bt=Button(self.root, text="Submit", command=self.command)
        self.bt.pack()





        self.root.mainloop()

    def get_values(self):
        conn = connect()
        cr = conn.cursor()
        q = f"select name from area"
        cr.execute(q)
        result = cr.fetchall()
        lst=[]
        for i in result:
            lst.append(i[0])
        return lst


    def get_values1(self):
        conn = connect()
        cr = conn.cursor()
        q = f"select id,name from location"
        cr.execute(q)
        self.result = cr.fetchall()
        lst=[]
        for i in self.result:
            lst.append(i[1])
        return lst




    def command(self):

        name = self.txt1.get()
        email = self.txt2.get()
        mobile = self.txt3.get()
        incharge_name = self.txt4.get()
        password = self.txt5.get()
        location_name = self.txt6.get()

        area = self.txt7.get()

        for i in self.result:
            if i[1] == location_name:
                location_id = i[0]



        if len(name)==0 or len(email)==0 or len(mobile)==0 or len(incharge_name)==0 or len(password)==0 or len(location_name)==0 or len(area)==0:
            msg.showwarning("alert","insert values")

        else:

            if verifyMobile(mobile) == 'Invalid' or verifyEmail(email) == 'Invalid':
                msg.showwarning('Warning', "Invalid Email or Mobile Number")
            else:

                conn = connect()
                cr = conn.cursor()
                q = f"insert into center values(null, '{name}','{email}', '{mobile}','{incharge_name}','{location_id}','{area}','{password}', '{self.status}')"
                # print(q)
                cr.execute(q)
                conn.commit()
                msg.showinfo("sucess", "location has been added..")
                self.txt1.delete(0, 'end')
                self.txt2.delete(0, 'end')
                self.txt3.delete(0, 'end')
                self.txt4.delete(0, 'end')
                self.txt5.delete(0, 'end')
                self.txt6.set('')
                self.txt7.set('')




# -----------------
#x=main()