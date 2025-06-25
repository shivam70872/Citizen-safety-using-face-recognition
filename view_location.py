from tkinter import *
import tkinter.messagebox as msg
import tkinter.ttk as ttk
from connection import connect


class main():



    def __init__(self):

        self.root = Tk()
        self.root.geometry("800x900")

        self.mainlabel = Label(self.root, text="View Location", font=("arial",24,"bold"))
        self.mainlabel.pack(pady=20)

        self.f = Frame(self.root)
        self.f.pack(pady=10)

        self.lb11 = Label(self.f, text="Search Name", font=("arial",14))
        self.lb11.grid(row=0, column=0, padx=10)

        self.txt11 = Entry(self.f, font=("arial", 14), width=30)
        self.txt11.grid(row=0, column=1, padx=10)

        self.bt1=Button(self.f, text="Search", font=("arial", 14), command= self.searchadmin)
        self.bt1.grid(row=0, column=2, padx=10)

        self.bt2 = Button(self.f, text="Refresh", font=("arial", 14), command= self.refresh)
        self.bt2.grid(row=0, column=3, padx=10)

        self.admintable = ttk.Treeview(self.root, columns=('id', 'name', 'description', 'area', 'timings'))
        self.admintable.pack(pady=10, padx=20, expand=True, fill='both')

        self.admintable.heading('id', text='ID')
        self.admintable.heading('name', text='Name')
        self.admintable.heading('description', text='Description')
        self.admintable.heading('area', text='Area')
        self.admintable.heading('timings', text='Timings')

        style = ttk.Style()
        style.configure('Treeview', font=('arial', 14), rowheight=40)
        style.configure('Treeview.Heading', font=('arial', 14), rowheight=40)

        self.admintable['show'] = 'headings'
        self.getValues()
        self.admintable.bind("<Double-1>", self.openupdatewindow)


        self.delbtn = Button(self.root, text='Delete', font=('arial', 14), command= self.deladmin)
        self.delbtn.pack(pady=20)


        self.root.mainloop()


    def openupdatewindow(self, event):
        rowid = self.admintable.selection()[0]
        data = self.admintable.item(rowid)
        selectedadmin = data['values']

        self.root1 = Toplevel()
        self.root1.geometry("900x800")

        self.mainlabel=Label(self.root1, text="Update Location",font=("calibri",28,"bold"))
        self.mainlabel.pack()

        self.f=Frame(self.root1)
        self.f.pack(pady=20)
        font = ("calibri",14)

        self.lb0=Label(self.f,text="ID", font=font)
        self.lb0.grid(row=0,column=0)

        self.txt0 = Entry(self.f,width=40)
        self.txt0.grid(row=0,column=1)
        self.txt0.insert(0, selectedadmin[0])
        self.txt0.config(state='readonly')


        self.lb1=Label(self.f,text="Enter Name",font=font)
        self.lb1.grid(row=1,column=0)

        self.txt1=Entry(self.f,width=40)
        self.txt1.grid(row=1,column=1)
        self.txt1.insert(0, selectedadmin[1])


        self.lb2=Label(self.f,text="Enter Description",font=font)
        self.lb2.grid(row=2,column=0)

        self.txt2=Entry(self.f,width=40)
        self.txt2.grid(row=2,column=1)
        self.txt2.insert(0, selectedadmin[2])

        self.lb3 = Label(self.f, text="Selet Area", font=font)
        self.lb3.grid(row=3, column=0)

        self.txt3 = ttk.Combobox(self.f, values=self.get_values1(), state="readonly", width=40)
        self.txt3.grid(row=3, column=1)
        self.txt3.set(selectedadmin[3])

        self.lb4 = Label(self.f, text="timings", font=font, )
        self.lb4.grid(row=4, column=0)

        self.txt4 = Entry(self.f, width=40)
        self.txt4.grid(row=4, column=1)
        self.txt4.insert(0, selectedadmin[4])

        self.bt1=Button(self.root1,text="submit", command=self.updateAdmin)
        self.bt1.pack()

        self.root1.mainloop()


    def updateAdmin(self):
        id = self.txt0.get()
        name = self.txt1.get()
        description = self.txt2.get()
        timings = self.txt4.get()
        area = self.txt3.get()
        q = f"update location set name='{name}', description='{description}', timings='{timings}',area='{area}' where id='{id}'"
        self.cr.execute(q)
        self.conn.commit()
        msg.showinfo('Success', "Location has been Updated")
        self.getValues()
        self.root1.destroy()


    def deladmin(self):
        rowid = self.admintable.selection()[0]
        data = self.admintable.item(rowid)
        selectedAdmin = data['values']
        adminID = selectedAdmin[0]
        q = f"delete from location where id='{adminID}'"
        self.cr.execute(q)
        self.conn.commit()
        msg.showinfo('Success', "Location deleted Successfully")
        self.getValues()


    def refresh(self):
        self.txt11.delete(0, 'end')
        self.getValues()

    def searchadmin(self):
        text = self.txt11.get()
        q = f"select * from location where name like '%{text}%'"
        self.cr.execute(q)
        data = self.cr.fetchall()
        for k in self.admintable.get_children():
            self.admintable.delete(k)
        for i in data:
            self.admintable.insert('', index=0, values=i)


    def getValues(self):
        self.conn = connect()
        self.cr = self.conn.cursor()
        q = f"select id, name, description, area, timings from location"
        self.cr.execute(q)
        data = self.cr.fetchall()
        for k in self.admintable.get_children():
            self.admintable.delete(k)
        for i in data:
            self.admintable.insert('', index=0, values=i)

    def get_values1(self):
        conn = connect()
        cr = conn.cursor()
        q = f"select name from area"
        cr.execute(q)
        result = cr.fetchall()
        lst=[]
        for i in result:
            lst.append(i[0])
        return lst


# -------------------
# x = main()


