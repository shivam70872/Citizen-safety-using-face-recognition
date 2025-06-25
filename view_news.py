from tkinter import *
import tkinter.messagebox as msg
import tkinter.ttk as ttk
from connection import connect
import cv2
from tkinter.filedialog import askopenfilename
import random

class main():



    def __init__(self):

        self.root = Tk()
        self.root.geometry("800x900")

        self.mainlabel = Label(self.root, text="View News", font=("arial",24,"bold"))
        self.mainlabel.pack(pady=20)

        self.f = Frame(self.root)
        self.f.pack(pady=10)

        self.lb11 = Label(self.f, text="Search Title", font=("arial",14))
        self.lb11.grid(row=0, column=0, padx=10)

        self.txt11 = Entry(self.f, font=("arial", 14), width=30)
        self.txt11.grid(row=0, column=1, padx=10)

        self.bt1=Button(self.f, text="Search", font=("arial", 14), command=self.search)
        self.bt1.grid(row=0, column=2, padx=10)

        self.bt2 = Button(self.f, text="Refresh", font=("arial", 14), command=self.refresh)
        self.bt2.grid(row=0, column=3, padx=10)

        self.admintable = ttk.Treeview(self.root, columns=('ID', 'Title', 'Description', 'date', 'image'))
        self.admintable.pack(pady=10, padx=20, expand=True, fill='both')

        self.admintable.heading('ID', text='ID')
        self.admintable.heading('Title', text='TITLE')
        self.admintable.heading('Description', text='DESCRIPTION')
        self.admintable.heading('date', text='DATE')
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

        self.mainlabel=Label(self.root1, text="Edit News",font=("calibri",28,"bold"))
        self.mainlabel.pack()

        self.f=Frame(self.root1)
        self.f.pack(pady=20)
        font=("calibri",14)

        self.lb0=Label(self.f,text="ID", font=font)
        self.lb0.grid(row=0,column=0)

        self.txt0 = Entry(self.f,width=40)
        self.txt0.grid(row=0,column=1)
        self.txt0.insert(0, selectedadmin[0])
        self.txt0.config(state='readonly')


        self.lb1=Label(self.f,text="Enter Title",font=font)
        self.lb1.grid(row=1,column=0)

        self.txt1=Entry(self.f,width=40)
        self.txt1.grid(row=1,column=1)
        self.txt1.insert(0, selectedadmin[1])

        self.lb2 = Label(self.f, text="Enter Description", font=font)
        self.lb2.grid(row=2, column=0)

        self.txt2 = Entry(self.f, width=40)
        self.txt2.grid(row=2, column=1)
        self.txt2.insert(0, selectedadmin[2])

        self.lb3 = Label(self.f, text="Enter Date", font=font)
        self.lb3.grid(row=3, column=0)

        self.txt3 = Entry(self.f, width=40)
        self.txt3.grid(row=3, column=1)
        self.txt3.insert(0, selectedadmin[3])

        self.lb4 = Label(self.f, text="select Image", font=font)
        self.lb4.grid(row=4, column=0)

        self.txt4 = Entry(self.f, width=40, state='readonly')
        self.txt4.grid(row=4, column=1)
        self.txt4.insert(0, selectedadmin[4])




        self.bt1=Button(self.root1,text="submit", command=self.updateAdmin)
        self.bt1.pack()

        self.root1.mainloop()

    def updateAdmin(self):
        id = self.txt0.get()
        Title = self.txt1.get()
        desc = self.txt2.get()
        date = self.txt3.get()
        image = self.txt4.get()
        q = f"update news_article set title='{Title}', description='{desc}', date='{date}', image='{image}' where id='{id}'"
        self.cr.execute(q)
        self.conn.commit()
        msg.showinfo('Success', "News has been Updated")
        self.getValues()
        self.root1.destroy()






    def deladmin(self):
        rowid = self.admintable.selection()[0]
        data = self.admintable.item(rowid)
        selectedAdmin = data['values']
        adminID = selectedAdmin[0]

        q = f"delete from news_article where id='{adminID}'"
        self.cr.execute(q)
        self.conn.commit()
        msg.showinfo('Success', "News deleted Successfully")
        self.getValues()




    def refresh(self):
        self.txt11.delete(0, 'end')
        self.getValues()

    def search(self):
        text = self.txt11.get()
        q = f"select * from news_article where title like '%{text}%'"
        self.cr.execute(q)
        data = self.cr.fetchall()
        for k in self.admintable.get_children():
            self.admintable.delete(k)
        for i in data:
            self.admintable.insert('', index=0, values=i)

    def getValues(self):
        self.conn = connect()
        self.cr = self.conn.cursor()
        q = f"select id, title, description, date, image from news_article"
        self.cr.execute(q)
        data = self.cr.fetchall()
        for k in self.admintable.get_children():
            self.admintable.delete(k)
        for i in data:
            self.admintable.insert('', index=0, values=i)


# -------------------
# obj=main()


