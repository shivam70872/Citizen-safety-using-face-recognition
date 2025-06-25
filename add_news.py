from tkinter import *
import tkinter.messagebox as msg
import tkinter.ttk as ttk
from connection import connect
from tkinter.filedialog import askopenfilename
import cv2
import random




class main():



    def __init__(self):
        self.root=Tk()
        self.root.geometry("900x800")

        self.mainlabel=Label(self.root, text="Add News",font=("calibri",28,"bold"))
        self.mainlabel.pack()

        self.f=Frame(self.root)
        self.f.pack(pady=20)
        font=("calibri",14)

        self.lb1=Label(self.f,text="Title",font=font)
        self.lb1.grid(row=0,column=0)

        self.txt1=Entry(self.f,width=40)
        self.txt1.grid(row=0,column=1)

        self.lb2=Label(self.f,text="Description",font=font)
        self.lb2.grid(row=1,column=0)

        self.txt2=Entry(self.f,width=40)
        self.txt2.grid(row=1,column=1)

        self.lb3=Label(self.f,text="Date(YYYY/MM/DD)",font=font)
        self.lb3.grid(row=3,column=0)

        self.txt3=Entry(self.f,width=40)
        self.txt3.grid(row=3,column=1)

        self.lb4=Label(self.f,text="Image",font=font)
        self.lb4.grid(row=4,column=0)

        self.txt4=Entry(self.f,width=40)
        self.txt4.grid(row=4,column=1)


        self.bt11 = Button(self.f, text="select", command=self.selectimage)
        self.bt11.grid(row=4, column=2, padx=20)

        self.bt1=Button(self.root,text="submit",command=self.submitform)
        self.bt1.pack()

        self.root.mainloop()

    def selectimage(self):
        # citizen_name = self.txt1.get()
        path = askopenfilename()
        # print(path)
        img = cv2.imread(path)
        # cascade = cv2.CascadeClassifier('admin/haarcascade_frontalface_default.xml')
        # face = cascade.detectMultiScale(img, 1.1, 4)
        # if len(face) == 0:
        #     msg.showwarning('Warning', 'Image is not valid')
        # else:
        msg.showinfo('Sucess', 'image is Added')
        img_name = f"{random.randint(100000, 999999)}.png"
        cv2.imwrite(f"admin/news/{img_name}", img)
        self.txt4.insert(0, img_name)

    def submitform(self):
        title = self.txt1.get()
        desc = self.txt2.get()
        date = self.txt3.get()
        image = self.txt4.get()


        if len(title) == 0 or len(desc)==0 or len(date)==0 or len(image)==0:
            msg.showwarning('warning', "please enter values")

        else:
            conn = connect()
            cr = conn.cursor()
            q = f"insert into news_article values(null,'{title}','{desc}','{date}','{image}')"
            #print(q)
            cr.execute(q)
            conn.commit()
            msg.showinfo("sucess","News has been added..")
            self.txt1.delete(0,'end')
            self.txt2.delete(0, 'end')
            self.txt3.delete(0, 'end')
            self.txt4.delete(0, 'end')

#---------------------------------------------
# x=main()

