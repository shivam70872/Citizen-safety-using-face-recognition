from tkinter import *
import add_admin
import view_admin
import add_category
import view_category
import add_area
import view_area
import add_location
import view_location
import add_citizen
import view_citizen
import view_center
import add_news
import view_news
import change_password


class Main:
    def __init__(self):
        self.root = Tk()
        self.root.geometry('800x900')

        self.rootmenu = Menu(self.root)
        self.root.configure(menu=self.rootmenu)
        self.profilesubmenu = Menu(self.rootmenu, tearoff=0)
        self.rootmenu.add_cascade(label='Profile', menu=self.profilesubmenu)
        self.profilesubmenu.add_command(label='Change password', command=lambda : change_password.Main())
        self.profilesubmenu.add_command(label='Logout', command=lambda: self.root.destroy())

        self.adminsubmenu = Menu(self.rootmenu, tearoff=0)
        self.rootmenu.add_cascade(label='Manage Admin', menu=self.adminsubmenu)
        self.adminsubmenu.add_command(label='Add Admin', command=lambda: add_admin.main())
        self.adminsubmenu.add_command(label='View Admin', command=lambda: view_admin.main())

        self.categorysubmenu = Menu(self.rootmenu, tearoff=0)
        self.rootmenu.add_cascade(label='Manage Category', menu=self.categorysubmenu)
        self.categorysubmenu.add_command(label='Add Category', command=lambda: add_category.page())
        self.categorysubmenu.add_command(label='View Category', command=lambda: view_category.main())

        self.areasubmenu = Menu(self.rootmenu, tearoff=0)
        self.rootmenu.add_cascade(label='Manage Area', menu=self.areasubmenu)
        self.areasubmenu.add_command(label='Add Area', command=lambda: add_area.main())
        self.areasubmenu.add_command(label='View Area', command=lambda: view_area.main())

        self.locationsubmenu = Menu(self.rootmenu, tearoff=0)
        self.rootmenu.add_cascade(label='Manage Location', menu=self.locationsubmenu)
        self.locationsubmenu.add_command(label='Add Location', command=lambda: add_location.main())
        self.locationsubmenu.add_command(label='View Location', command=lambda: view_location.main())

        self.citizensubmenu = Menu(self.rootmenu, tearoff=0)
        self.rootmenu.add_cascade(label='Manage Citizen', menu=self.citizensubmenu)
        self.citizensubmenu.add_command(label='Add Citizen', command=lambda: add_citizen.main())
        self.citizensubmenu.add_command(label='View Citizen', command=lambda: view_citizen.main())

        self.centersubmenu = Menu(self.rootmenu, tearoff=0)
        self.rootmenu.add_cascade(label='Manage center', menu=self.centersubmenu)
        self.centersubmenu.add_command(label='View center', command=lambda: view_center.main())

        self.newssubmenu = Menu(self.rootmenu, tearoff=0)
        self.rootmenu.add_cascade(label='Manage news', menu=self.newssubmenu)
        self.newssubmenu.add_command(label='Add news', command=lambda: add_news.main())
        self.newssubmenu.add_command(label='View news', command=lambda: view_news.main())

        self.mainlabel = Label(self.root, text='Admin Dashboard', font=('arial', 24, 'bold', 'italic', 'underline'))
        self.mainlabel.pack(pady=20)

        self.root.mainloop()
# -------------------------------------------------


#obj = Main()
