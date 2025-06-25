from tkinter import *
import faceDemo
import add_citizen
import view_citizen
import changecenter_password


class Main:
    def __init__(self, center_id):
        self.root = Tk()
        self.root.geometry('800x900')
        print(center_id)

        self.rootmenu = Menu(self.root)
        self.root.configure(menu=self.rootmenu)
        self.profilesubmenu = Menu(self.rootmenu, tearoff=0)
        self.rootmenu.add_cascade(label='Profile', menu=self.profilesubmenu)
        self.profilesubmenu.add_command(label='Change password', command=lambda: changecenter_password.Main())
        self.profilesubmenu.add_command(label='Logout', command=lambda: self.root.destroy())

        self.citizensubmenu = Menu(self.rootmenu, tearoff=0)
        self.rootmenu.add_cascade(label='Manage Citizen', menu=self.citizensubmenu)
        self.citizensubmenu.add_command(label='Add Citizen', command=lambda: add_citizen.main())
        self.citizensubmenu.add_command(label='View Citizen', command=lambda: view_citizen.main())

        self.citizensubmenu.add_command(label='Detect Citizens', command=lambda: faceDemo.Main(center_id))

        self.mainlabel = Label(self.root, text='Center Dashboard', font=('arial', 24, 'bold', 'italic', 'underline'))
        self.mainlabel.pack(pady=20)

        self.root.mainloop()


# -------------------------------------------------


# obj = Main(2)
