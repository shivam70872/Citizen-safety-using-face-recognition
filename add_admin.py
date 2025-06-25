from tkinter import *
import tkinter.messagebox as msg
import tkinter.ttk as ttk
from connection import connect, verifyMobile, verifyEmail





class main():



    def __init__(self):
        self.root=Tk()
        self.root.geometry("900x800")

        self.mainlabel=Label(self.root, text="Add Admin",font=("calibri",28,"bold"))
        self.mainlabel.pack()

        self.f=Frame(self.root)
        self.f.pack(pady=20)
        font=("calibri",14)

        self.lb1=Label(self.f,text="Name",font=font)
        self.lb1.grid(row=0,column=0)

        self.txt1=Entry(self.f,width=40)
        self.txt1.grid(row=0,column=1)

        self.lb2=Label(self.f,text="Email",font=font)
        self.lb2.grid(row=1,column=0)

        self.txt2=Entry(self.f,width=40)
        self.txt2.grid(row=1,column=1)

        self.lb3=Label(self.f,text="Mobile",font=font)
        self.lb3.grid(row=3,column=0)

        self.txt3=Entry(self.f,width=40)
        self.txt3.grid(row=3,column=1)

        self.lb4=Label(self.f,text="role",font=font)
        self.lb4.grid(row=4,column=0)

        self.txt4=ttk.Combobox(self.f,values=["admin","super admin"],state="readonly", width=39)
        self.txt4.grid(row=4,column=1)

        self.lb5=Label(self.f,text="Password",font=font,)
        self.lb5.grid(row=5,column=0)

        self.txt5=Entry(self.f,width=40,show="*")
        self.txt5.grid(row=5,column=1)

        self.bt1=Button(self.root,text="submit",command=self.submitform)
        self.bt1.pack()

        self.root.mainloop()

    def submitform(self):
        name = self.txt1.get()
        email = self.txt2.get()
        mobile = self.txt3.get()
        role = self.txt4.get()
        password = self.txt5.get()


        if len(name) == 0 or len(email)==0 or len(mobile)==0 or len(role)==0 or len(password)==0:
            msg.showwarning('warning', "please enter values")
        else:

            if verifyMobile(mobile) == 'Invalid' or verifyEmail(email) == 'Invalid':
                msg.showwarning('Warning', "Invalid Email or Mobile Number")
            else:

                conn = connect()
                cr = conn.cursor()
                q = f"insert into admin values(null,'{name}','{email}','{mobile}','{role}','{password}')"
                #print(q)
                cr.execute(q)
                conn.commit()
                msg.showinfo("sucess","Admin has been added..")
                self.txt1.delete(0,'end')
                self.txt2.delete(0, 'end')
                self.txt3.delete(0, 'end')
                self.txt5.delete(0, 'end')
                self.txt4.set('')

#---------------------------------------------
#x=main()

