from tkinter import *
import tkinter.messagebox as msg
import tkinter.ttk as ttk
from connection import connect




class main():



    def __init__(self):
        self.root=Tk()
        self.root.geometry("900x800")

        self.mainlabel=Label(self.root, text="Add Area",font=("calibri",28,"bold"))
        self.mainlabel.pack()

        self.f=Frame(self.root)
        self.f.pack(pady=20)
        font=("calibri",14)

        self.lb1=Label(self.f,text="Name",font=font)
        self.lb1.grid(row=0,column=0)

        self.txt1=Entry(self.f,width=40)
        self.txt1.grid(row=0,column=1)

        self.lb2=Label(self.f,text="City",font=font)
        self.lb2.grid(row=1,column=0)

        self.txt2=Entry(self.f,width=40)
        self.txt2.grid(row=1,column=1)

        self.lb3=Label(self.f,text="State",font=font)
        self.lb3.grid(row=2,column=0)

        self.txt3 = ttk.Combobox(self.f, values=['Andhra Pradesh', 'Arunachal Pradesh', 'Assam', 'Bihar', 'Chhattisgarh', 'Goa', 'Gujarat', 'Haryana', 'Himachal Pradesh', 'Jammu and Kashmir', 'Jharkhand', 'Karnataka', 'Kerala', 'Madhya Pradesh', 'Maharashtra', 'Manipur', 'Meghalaya', 'Mizoram', 'Nagaland', 'Odisha', 'Punjab', 'Rajasthan', 'Sikkim', 'Tamil Nadu', 'Telangana', 'Tripura', 'Uttar Pradesh', 'West Bengal'], state="readonly", width=40)
        self.txt3.grid(row=2, column=1)

        self.lb4=Label(self.f,text="Landmark",font=font)
        self.lb4.grid(row=3,column=0)

        self.txt4=Entry(self.f, width=40)
        self.txt4.grid(row=3,column=1)



        self.bt1=Button(self.root,text="submit",command=self.submitform)
        self.bt1.pack()

        self.root.mainloop()

    def submitform(self):
        name = self.txt1.get()
        city = self.txt2.get()
        state = self.txt3.get()
        landmark = self.txt4.get()



        if len(name) == 0 or len(city)==0 or len(state)==0 or len(landmark)==0:
            msg.showwarning('warning', "please enter values")

        else:
            conn = connect()
            cr = conn.cursor()
            q = f"insert into area values('{name}','{city}','{state}','{landmark}')"
            #print(q)
            cr.execute(q)
            conn.commit()
            msg.showinfo("sucess","Area has been added..")
            self.txt1.delete(0,'end')
            self.txt2.delete(0, 'end')
            self.txt4.delete(0, 'end')
            self.txt3.set('')

#---------------------------------------------
# x=main()

