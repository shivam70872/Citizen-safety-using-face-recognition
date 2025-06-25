from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as msg
from connection import connect


class main():

    def __init__(self):
        self.root = Tk()
        self.root.geometry("800x900")

        self.heading=Label(self.root, text="Add Location", font=("calibri", 28, "bold", "underline"))
        self.heading.pack()

        self.f=Frame(self.root)
        self.f.pack(pady=20)
        self.f.configure(height=290,width=230)


        font=("calibri",14)
        self.lb1=Label(self.f, text="Enter Name", font=font)
        self.lb1.grid(row=0,column=0)

        self.txt1 = Entry(self.f, width=40)
        self.txt1.grid(row=0, column=1)

        self.lb2 = Label(self.f, text=" Enter Description", font=font)
        self.lb2.grid(row=1, column=0)

        self.txt2 = Entry(self.f, width=40)
        self.txt2.grid(row=1, column=1)

        self.lb3 = Label(self.f, text="Select Area", font=font)
        self.lb3.grid(row=2, column=0)

        self.txt3 = ttk.Combobox(self.f, width=39, values=self.get_values())
        self.txt3.grid(row=2, column=1)


        self.lb4 = Label(self.f, text=" Enter Timings", font=font)
        self.lb4.grid(row=3, column=0)

        self.txt4 = Entry(self.f, width=40)
        self.txt4.grid(row=3, column=1)


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




    def command(self):

        name=self.txt1.get()
        description=self.txt2.get()
        area=self.txt3.get()
        timings = self.txt4.get()


        if len(name)==0 or len(description)==0:
            msg.showwarning("alert","insert values")
        else:
            conn = connect()
            cr = conn.cursor()
            q = f"insert into location values(null, '{name}','{description}', '{area}','{timings}')"
            # print(q)
            cr.execute(q)
            conn.commit()
            msg.showinfo("sucess", "location has been added..")
            self.txt1.delete(0, 'end')
            self.txt2.delete(0, 'end')
            self.txt4.delete(0, 'end')
            self.txt3.set('')




# x=main()