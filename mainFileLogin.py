
from tkinter import *
import center_login
import adminlogin
from PIL import Image,ImageTk

class Main:
    def __init__(self):
        self.root=Tk()
        self.root.title("Main Login Page")
        self.root.state("zoomed")
        self.root.configure(bg="skyblue")
        self.lb1=Label(self.root , text="Login Page" ,font="calibri 25 bold" , fg ="blue")
        self.lb1.pack(padx=10,pady=10)

        self.fr=Frame(self.root)
        self.fr.pack(pady=20)

        self.btn1=Button(self.fr,text="Admin Login", font="calibri 25 bold",command=self.admin, fg ="brown",bg="white",activeforeground="skyblue")
        self.btn1.grid(row=0,column=0)
        self.btn1.configure(anchor=CENTER)

        self.btn2 = Button(self.fr, text="Center Login", font="calibri 25 bold", fg="brown", bg="white",
                           activeforeground="skyblue",command=self.center)
        self.btn2.grid(row=0, column=3)
        self.btn1.configure(anchor=CENTER)

        img = Image.open('images/pre.jpg')
        width = int(self.root.winfo_screenwidth())
        height = int(self.root.winfo_screenheight())
        print(width, height)
        img = img.resize((width, height))
        bg = ImageTk.PhotoImage(img)

        canvas = Canvas(self.root, width=self.root.winfo_width(), height=self.root.winfo_height())
        canvas.pack(fill='both', expand=True)

        canvas.create_image(0, 0, image=bg, anchor='nw')

        self.root.mainloop()

    def center(self):
        center_login.Main()

    def admin(self):
        adminlogin.Main()

if __name__ == '__main__':
    Main()