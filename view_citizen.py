from tkinter import *
import tkinter.messagebox as msg
import tkinter.ttk as ttk
from connection import connect


class main():

    def __init__(self):

        self.root = Tk()
        self.root.geometry("800x900")

        self.mainlabel = Label(self.root, text="View Citizens", font=("arial", 24, "bold"))
        self.mainlabel.pack(pady=20)

        self.f = Frame(self.root)
        self.f.pack(pady=10)

        self.lb11 = Label(self.f, text="Search Name", font=("arial", 14))
        self.lb11.grid(row=0, column=0, padx=10)

        self.txt11 = Entry(self.f, font=("arial", 14), width=30)
        self.txt11.grid(row=0, column=1, padx=10)

        self.bt1 = Button(self.f, text="Search", font=("arial", 14), command=self.searchadmin)
        self.bt1.grid(row=0, column=2, padx=10)

        self.bt2 = Button(self.f, text="Refresh", font=("arial", 14), command=self.refresh)
        self.bt2.grid(row=0, column=3, padx=10)

        self.admintable = ttk.Treeview(self.root, columns=(
        'id', 'name', 'mobile', 'email', 'date of birth', 'address', 'aadhar', 'image'))
        self.admintable.pack(pady=10, padx=20, expand=True, fill='both')

        self.admintable.heading('id', text='ID')
        self.admintable.heading('name', text='Name')
        self.admintable.heading('mobile', text='MOBILE')
        self.admintable.heading('email', text='EMAIL')
        self.admintable.heading('date of birth', text='DATE OF BIRTH')
        self.admintable.heading('address', text='ADDRESS')
        self.admintable.heading('aadhar', text='AADHAR')
        self.admintable.heading('image', text='IMAGE')

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

        self.mainlabel = Label(self.root1, text="Update Citizen", font=("calibri", 28, "bold"))
        self.mainlabel.pack()

        self.f = Frame(self.root1)
        self.f.pack(pady=20)
        font = ("calibri", 14)

        self.lb0 = Label(self.f, text="Citizen ID", font=font)
        self.lb0.grid(row=0, column=0)

        self.txt0 = Entry(self.f, width=40)
        self.txt0.grid(row=0, column=1)
        self.txt0.insert(0, selectedadmin[0])
        self.txt0.config(state='readonly')

        self.lb1 = Label(self.f, text="Enter Name", font=font)
        self.lb1.grid(row=1, column=0)

        self.txt1 = Entry(self.f, width=40)
        self.txt1.grid(row=1, column=1)
        self.txt1.insert(0, selectedadmin[1])

        self.lb2 = Label(self.f, text="Enter Mobile", font=font)
        self.lb2.grid(row=2, column=0)

        self.txt2 = Entry(self.f, width=40)
        self.txt2.grid(row=2, column=1)
        self.txt2.insert(0, selectedadmin[2])

        self.lb3 = Label(self.f, text="Enter Email", font=font, )
        self.lb3.grid(row=3, column=0)

        self.txt3 = Entry(self.f, width=40)
        self.txt3.grid(row=3, column=1)
        self.txt3.insert(0, selectedadmin[3])

        self.lb4 = Label(self.f, text="Enter Date of Birth", font=font)
        self.lb4.grid(row=4, column=0)

        self.txt4 = Entry(self.f, width=40)
        self.txt4.grid(row=4, column=1)
        self.txt4.insert(0, selectedadmin[4])

        self.lb5 = Label(self.f, text="Enter Address", font=font)
        self.lb5.grid(row=5, column=0)

        self.txt5 = Entry(self.f, width=40)
        self.txt5.grid(row=5, column=1)
        self.txt5.insert(0, selectedadmin[5])

        self.lb6 = Label(self.f, text="Enter Aadhar", font=font)
        self.lb6.grid(row=6, column=0)

        self.txt6 = Entry(self.f, width=40)
        self.txt6.grid(row=6, column=1)
        self.txt6.insert(0, selectedadmin[6])

        self.lb7 = Label(self.f, text="Enter Image", font=font)
        self.lb7.grid(row=7, column=0)

        self.txt7 = Entry(self.f, width=40)
        self.txt7.grid(row=7, column=1)
        self.txt7.insert(0, selectedadmin[7])

        self.bt1 = Button(self.root1, text="submit", command=self.updateAdmin)
        self.bt1.pack()

        self.root1.mainloop()

    def updateAdmin(self):
        id = self.txt0.get()
        name = self.txt1.get()
        mobile = self.txt2.get()
        email = self.txt3.get()
        dob = self.txt4.get()
        address = self.txt5.get()
        aadhar = self.txt6.get()
        image = self.txt7.get()
        q = f"update citizen set name='{name}', mobile='{mobile}', email='{email}', dob='{dob}', address='{address}', aadhar='{aadhar}', image='{image}' where id='{id}'"
        self.cr.execute(q)
        self.conn.commit()
        msg.showinfo('Success', "Admin has been Updated")
        self.getValues()
        self.root1.destroy()

    def refresh(self):
        self.txt11.delete(0, 'end')
        self.getValues()

    def searchadmin(self):
        text = self.txt11.get()
        q = f"select * from citizen where name like '%{text}%'"
        self.cr.execute(q)
        data = self.cr.fetchall()
        for k in self.admintable.get_children():
            self.admintable.delete(k)
        for i in data:
            self.admintable.insert('', index=0, values=i)

    def deladmin(self):
        rowid = self.admintable.selection()[0]
        data = self.admintable.item(rowid)
        selectedAdmin = data['values']
        adminID = selectedAdmin[0]
        q = f"delete from citizen where id='{adminID}'"
        self.cr.execute(q)
        self.conn.commit()
        msg.showinfo('Success', "Citizen deleted Successfully")
        self.getValues()

    def getValues(self):
        self.conn = connect()
        self.cr = self.conn.cursor()
        q = f"select id, name, mobile, email, dob, address, aadhar, image from citizen"
        self.cr.execute(q)
        data = self.cr.fetchall()
        for k in self.admintable.get_children():
            self.admintable.delete(k)
        for i in data:
            self.admintable.insert('', index=0, values=i)

# -------------------
# x = main()
