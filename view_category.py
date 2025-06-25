from tkinter import *
import tkinter.messagebox as msg
import tkinter.ttk as ttk
from connection import connect


class main():



    def __init__(self):

        self.root = Tk()
        self.root.geometry("800x900")

        self.mainlabel = Label(self.root, text="View Category", font=("arial",24,"bold"))
        self.mainlabel.pack(pady=20)

        self.f = Frame(self.root)
        self.f.pack(pady=10)

        self.lb11 = Label(self.f, text="Search Name", font=("arial",14))
        self.lb11.grid(row=0, column=0, padx=10)

        self.txt11 = Entry(self.f, font=("arial", 14), width=30)
        self.txt11.grid(row=0, column=1, padx=10)

        self.bt1=Button(self.f, text="Search", font=("arial", 14), command=self.search)
        self.bt1.grid(row=0, column=2, padx=10)

        self.bt2 = Button(self.f, text="Refresh", font=("arial", 14), command=self.refresh)
        self.bt2.grid(row=0, column=3, padx=10)

        self.admintable = ttk.Treeview(self.root, columns=('name','description'))
        self.admintable.pack(pady=10, padx=20, expand=True, fill='both')

        self.admintable.heading('name', text='Name')
        self.admintable.heading('description', text='Description')


        style = ttk.Style()
        style.configure('Treeview', font=('arial', 14), rowheight=40)
        style.configure('Treeview.Heading', font=('arial', 14), rowheight=40)

        self.admintable['show'] = 'headings'
        self.getValues()
        self.admintable.bind("<Double-1>", self.openupdatewindow)


        self.delbtn = Button(self.root, text='Delete', font=('arial', 14), command=self.deladmin)
        self.delbtn.pack(pady=20)


        self.root.mainloop()

    def openupdatewindow(self, event):
        rowid = self.admintable.selection()[0]
        data = self.admintable.item(rowid)
        selectedadmin = data['values']

        self.root1 = Toplevel()
        self.root1.geometry("900x800")

        self.mainlabel=Label(self.root1, text="Edit Category",font=("calibri",28,"bold"))
        self.mainlabel.pack()

        self.f=Frame(self.root1)
        self.f.pack(pady=20)
        font=("calibri",14)

        self.lb0=Label(self.f,text="Name", font=font)
        self.lb0.grid(row=0,column=0)

        self.txt0 = Entry(self.f,width=40)
        self.txt0.grid(row=0,column=1)
        self.txt0.insert(0, selectedadmin[0])
        self.txt0.config(state='readonly')


        self.lb1=Label(self.f,text="Enter Description",font=font)
        self.lb1.grid(row=1,column=0)

        self.txt1=Entry(self.f,width=40)
        self.txt1.grid(row=1,column=1)
        self.txt1.insert(0, selectedadmin[1])


        self.bt1=Button(self.root1,text="submit", command=self.updateAdmin)
        self.bt1.pack()

        self.root1.mainloop()

    def updateAdmin(self):
        name = self.txt0.get()
        description = self.txt1.get()
        q = f"update category set description='{description}' where name='{name}'"
        self.cr.execute(q)
        self.conn.commit()
        msg.showinfo('Success', "Admin has been Updated")
        self.getValues()
        self.root1.destroy()



    def deladmin(self):
        rowid = self.admintable.selection()[0]
        data = self.admintable.item(rowid)
        selectedAdmin = data['values']
        adminID = selectedAdmin[0]
        q = f"delete from category where name='{adminID}'"
        self.cr.execute(q)
        self.conn.commit()
        msg.showinfo('Success', "Category deleted Successfully")
        self.getValues()




    def refresh(self):
        self.txt11.delete(0, 'end')
        self.getValues()

    def search(self):
        text = self.txt11.get()
        q = f"select * from category where name like '%{text}%'"
        self.cr.execute(q)
        data = self.cr.fetchall()
        for k in self.admintable.get_children():
            self.admintable.delete(k)
        for i in data:
            self.admintable.insert('', index=0, values=i)

    def getValues(self):
        self.conn = connect()
        self.cr = self.conn.cursor()
        q = f"select name, description from category"
        self.cr.execute(q)
        data = self.cr.fetchall()
        for k in self.admintable.get_children():
            self.admintable.delete(k)
        for i in data:
            self.admintable.insert('', index=0, values=i)


# -------------------
# obj=main()


