from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as msg
from connection import connect

class main():
    def __init__(self):
        self.root = Tk()
        self.root.geometry('800x900')

        self.mainlabel = Label(self.root, text="View Citizen Remarks", font=("arial", 28, "bold"))
        self.mainlabel.pack(pady=20)
        self.f=Frame(self.root)
        self.f.pack(pady=10)

        self.adminTable=ttk.Treeview(self.root,columns=('id', 'citizen_id', 'center_id', 'date', 'time', 'description'))
        self.adminTable.pack(pady=10,padx=10,expand=True,fill='both')
        self.adminTable.heading('id',text='ID')
        self.adminTable.heading('citizen_id', text='Citizen Name')
        self.adminTable.heading('center_id', text='Center Name')
        self.adminTable.heading('date', text='Date')
        self.adminTable.heading('time', text='Time')
        self.adminTable.heading('description', text='Description')
        self.adminTable['show']='headings'
        style = ttk.Style()
        style.configure('Treeview', font=('arial', 12), rowheight=30)
        style.configure('Treeview.Heading', font=('arial', 12), rowheight=30)
        self.getvalues()
        self.adminTable.bind("<Double-1>", self.openUpdateWindow)


        self.root.mainloop()



    def refresh(self):
       self.tx1.delete(0, 'end')
       self.getvalues()

    def getvalues(self):
         conn = connect()
         cr = conn.cursor()
         q = f"select id, citizen_id, center_name, date, time,description from remarks"
         cr.execute(q)
         data = cr.fetchall()
         for k in self.adminTable.get_children():
          self.adminTable.delete(k)
        # print(k) TRee normally is empty but this isnt so we are just emptying it with the help of tree id
         for i in data:
           self.adminTable.insert('', index=0, values=i)#data dalte hain in tree


    def openUpdateWindow(self,event):
        rowid = self.adminTable.selection()[0]
        data = self.adminTable.item(rowid)
        selectedAdmin = data['values']

        self.root1=Toplevel()

        self.root1.geometry("800x600")
        self.mainlabel = Label(self.root1, text="UPDATE REMARKS", font=('calibri', 28, 'bold'))
        self.mainlabel.pack(pady=20)

        self.f = Frame(self.root1)
        self.f.pack(pady=10)
        font = ('calibri', 12)
        self.lb0 = Label(self.f, text="Id", font=font)
        self.tx0 = Entry(self.f, font=font, width=30)
        self.lb0.grid(row=0, column=0, pady=10, padx=10)
        self.tx0.grid(row=0, column=1, pady=10, padx=10)
        self.tx0.insert(0,selectedAdmin[0])
        self.tx0.config(state='readonly')

        self.lb1 = Label(self.f, text="Citizen Name:", font=font)
        self.tx1 = Entry(self.f, font=font, width=30)
        self.lb1.grid(row=1, column=0, pady=10, padx=10)
        self.tx1.grid(row=1, column=1, pady=10, padx=10)
        self.tx1.insert(0,selectedAdmin[1])
        self.tx1.config(state='readonly')

        self.lb2 = Label(self.f, text="Center Name:", font=font)
        self.tx2 = Entry(self.f, font=font, width=30)
        self.lb2.grid(row=2, column=0, pady=10, padx=10)
        self.tx2.grid(row=2, column=1, pady=10, padx=10)
        self.tx2.insert(0, selectedAdmin[2])
        self.tx2.config(state='readonly')

        self.lb3 = Label(self.f, text="Date", font=font)
        self.tx3 = Entry(self.f, font=font, width=30)
        self.lb3.grid(row=3, column=0, pady=10, padx=10)
        self.tx3.grid(row=3, column=1, pady=10, padx=10)
        self.tx3.insert(0, selectedAdmin[3])
        self.tx3.config(state='readonly')

        self.lb3 = Label(self.f, text="Time", font=font)
        self.tx3 = Entry(self.f, font=font, width=30)
        self.lb3.grid(row=3, column=0, pady=10, padx=10)
        self.tx3.grid(row=3, column=1, pady=10, padx=10)
        self.tx3.insert(0, selectedAdmin[3])
        self.tx3.config(state='readonly')

        self.lb3 = Label(self.f, text="Date", font=font)
        self.tx3 = Entry(self.f, font=font, width=30)
        self.lb3.grid(row=3, column=0, pady=10, padx=10)
        self.tx3.grid(row=3, column=1, pady=10, padx=10)
        self.tx3.insert(0, selectedAdmin[3])
        self.tx3.config(state='readonly')

        self.lb4 = Label(self.f, text="Time", font=font)
        self.tx4 = Entry(self.f, font=font, width=30)
        self.lb4.grid(row=4, column=0, pady=10, padx=10)
        self.tx4.grid(row=4, column=1, pady=10, padx=10)
        self.tx4.insert(0, selectedAdmin[4])
        self.tx4.config(state='readonly')

        self.lb5 = Label(self.f, text="Description", font=font)
        self.tx5 = Entry(self.f, font=font, width=30)
        self.lb5.grid(row=5, column=0, pady=10, padx=10)
        self.tx5.grid(row=5, column=1, pady=10, padx=10)
        self.tx5.insert(0, selectedAdmin[5])
        self.tx5.config(state='readonly')

        self.root1.mainloop()

obj=main()