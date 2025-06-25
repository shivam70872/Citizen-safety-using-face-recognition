from tkinter import *
import tkinter.messagebox as msg
import tkinter.ttk as ttk
from connection import connect, verifyEmail, verifyMobile
from tkinter.filedialog import askopenfilename
import cv2
import random


class main():

    def __init__(self):
        self.root = Tk()
        self.root.geometry("900x800")

        self.mainlabel = Label(self.root, text="Add Citizen", font=("calibri", 28, "bold"))
        self.mainlabel.pack()

        self.f = Frame(self.root)
        self.f.pack(pady=20)
        font = ("calibri", 14)

        self.lb1 = Label(self.f, text="Name", font=font)
        self.lb1.grid(row=0, column=0)

        self.txt1 = Entry(self.f, width=40)
        self.txt1.grid(row=0, column=1)

        self.lb2 = Label(self.f, text="Mobile", font=font)
        self.lb2.grid(row=1, column=0)

        self.txt2 = Entry(self.f, width=40)
        self.txt2.grid(row=1, column=1)

        self.lb3 = Label(self.f, text="Email", font=font)
        self.lb3.grid(row=3, column=0)

        self.txt3 = Entry(self.f, width=40)
        self.txt3.grid(row=3, column=1)

        self.lb4 = Label(self.f, text="Date Of Birth (YYYY/MM/DD)", font=font)
        self.lb4.grid(row=4, column=0)

        self.txt4 = Entry(self.f, width=40)
        self.txt4.grid(row=4, column=1)

        self.lb5 = Label(self.f, text="Address", font=font, )
        self.lb5.grid(row=5, column=0)

        self.txt5 = Entry(self.f, width=40)
        self.txt5.grid(row=5, column=1)

        self.lb6 = Label(self.f, text="Aadhar", font=font, )
        self.lb6.grid(row=6, column=0)

        self.txt6 = Entry(self.f, width=40)
        self.txt6.grid(row=6, column=1)

        self.lb7 = Label(self.f, text="Image", font=font, )
        self.lb7.grid(row=7, column=0)

        self.txt7 = Entry(self.f, width=40)
        self.txt7.grid(row=7, column=1)

        self.bt11 = Button(self.f, text="select", command=self.selectimage)
        self.bt11.grid(row=7, column=2, padx=20)

        self.bt1 = Button(self.root, text="submit", command=self.submitform)
        self.bt1.pack()

        self.root.mainloop()

    def selectimage(self):
        citizen_name = self.txt1.get()
        path = askopenfilename()
        # print(path)
        img = cv2.imread(path)
        cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        face = cascade.detectMultiScale(img, 1.1, 4)
        if len(face) == 0:
            msg.showwarning('Warning', 'Image is not valid')
        else:
            msg.showinfo('Sucess', 'image is valid')
            img_name = f"{citizen_name}_{random.randint(100, 999)}.png"
            cv2.imwrite(f"citizen/{img_name}", img)
            self.txt7.insert(0, img_name)

    def submitform(self):
        name = self.txt1.get()
        mobile = self.txt2.get()
        email = self.txt3.get()
        dob = self.txt4.get()
        address = self.txt5.get()
        aadhar = self.txt6.get()
        image = self.txt7.get()

        if len(name) == 0 or len(mobile) == 0 or len(email) == 0 or len(dob) == 0 or len(address) == 0 or len(
                aadhar) == 0 or len(image) == 0:
            msg.showwarning('warning', "please enter values")
        else:

            if verifyMobile(mobile) == 'Invalid' or verifyEmail(email) == 'Invalid':
                msg.showwarning('Warning', "Invalid Email or Mobile Number")
            else:


                conn = connect()
                cr = conn.cursor()
                q = f"insert into citizen values(null,'{name}','{mobile}','{email}','{dob}','{address}','{aadhar}','{image}')"
                # print(q)
                cr.execute(q)
                conn.commit()
                msg.showinfo("sucess", "Admin has been added..")
                self.txt1.delete(0, 'end')
                self.txt2.delete(0, 'end')
                self.txt3.delete(0, 'end')
                self.txt4.delete(0, 'end')
                self.txt5.delete(0, 'end')
                self.txt6.delete(0, 'end')
                self.txt7.delete(0, 'end')

# ---------------------------------------------
# x=main()
