from tkinter import *
import tkinter.messagebox as msg
import tkinter.ttk as ttk
from connection import connect


class main():



    def __init__(self):

        self.root = Tk()
        self.root.geometry("800x900")

        self.mainlabel = Label(self.root, text="View Center", font=("arial",24,"bold"))
        self.mainlabel.pack(pady=20)

        self.f = Frame(self.root)
        self.f.pack(pady=10)

        self.lb11 = Label(self.f, text="Search Name", font=("arial",14))
        self.lb11.grid(row=0, column=0, padx=10)

        self.txt11 = Entry(self.f, font=("arial", 14), width=30)
        self.txt11.grid(row=0, column=1, padx=10)

        self.bt1=Button(self.f, text="Search", font=("arial", 14), command=self.searchadmin)
        self.bt1.grid(row=0, column=2, padx=10)

        self.bt2 = Button(self.f, text="Refresh", font=("arial", 14), command=self.refresh)
        self.bt2.grid(row=0, column=3, padx=10)

        self.admintable = ttk.Treeview(self.root, columns=('id', 'name', 'email', 'mobile', 'incharge name', 'location', 'area','status'))
        self.admintable.pack(pady=10, padx=20, expand=True, fill='both')

        self.admintable.heading('id', text='ID')
        self.admintable.heading('name', text='Name')
        self.admintable.heading('email', text='Email')
        self.admintable.heading('mobile', text='Mobile')
        self.admintable.heading('incharge name', text='INCHARGE NAME')
        self.admintable.heading('location', text='LOCATION')
        self.admintable.heading('area', text='AREA')
        self.admintable.heading('status', text='STATUS')

        style = ttk.Style()
        style.configure('Treeview', font=('arial', 14), rowheight=40)
        style.configure('Treeview.Heading', font=('arial', 14), rowheight=40)

        self.admintable['show'] = 'headings'
        self.getValues()
        self.admintable.bind("<Double-1>", self.updatestatus1)


        self.root.mainloop()


    def updatestatus1(self, event):
        rowid = self.admintable.selection()[0]
        data = self.admintable.item(rowid)
        selectedadmin = data['values']
        adminID = selectedadmin[0]
        status = selectedadmin[-1]
        if int(status) == 0:
            self.status = 1
        else:
            self.status = 0

        q = f"update center set status='{self.status}' where id='{adminID}'"
        self.cr.execute(q)
        self.conn.commit()
        msg.showinfo('Success', "Status has been Updated")
        self.getValues()


    def refresh(self):
        self.txt11.delete(0, 'end')
        self.getValues()

    def searchadmin(self):
        text = self.txt11.get()
        q = f"select * from center where name like '%{text}%'"
        self.cr.execute(q)
        data = self.cr.fetchall()
        for k in self.admintable.get_children():
            self.admintable.delete(k)
        for i in data:
            self.admintable.insert('', index=0, values=i)

    def getValues(self):
        self.conn = connect()
        self.cr = self.conn.cursor()
        q = f"select id, name, email, mobile, incharge_name, location, area, status from center"
        self.cr.execute(q)
        data = self.cr.fetchall()
        for k in self.admintable.get_children():
            self.admintable.delete(k)
        for i in data:
            self.admintable.insert('', index=0, values=i)


# -------------------
#x = main()


