import datetime
# import tkinter.tix
from tkinter import *
import customtkinter
from PIL import Image, ImageTk
import cv2
from deepface import DeepFace
import os
import tkinter.messagebox as msg
from connection import connect
import maildemo


class Main:
    def __init__(self, center_id):
        self.conn = connect()
        self.cr = self.conn.cursor()
        customtkinter.set_appearance_mode('light')
        customtkinter.set_default_color_theme('green')
        windowColor = '#F2BEFC'
        frameColor = '#2b2b2b'
        self.root = customtkinter.CTkToplevel()
        sw = self.root.winfo_screenwidth()
        sh = self.root.winfo_screenheight()
        # print(sw, sh)
        self.root.geometry(f"{sw}x{sh}+0+0")

        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        self.sideFrame1 = customtkinter.CTkFrame(self.root, height=sh - 100, width=int(sw / 3))
        self.sideFrame1.pack_propagate(0)
        self.sideFrame2 = customtkinter.CTkFrame(self.root, height=sh - 100, width=int(sw / 3 * 2))
        self.sideFrame2.pack_propagate(0)
        self.sideFrame1.grid(row=0, column=0, padx=10, pady=20)
        self.sideFrame2.grid(row=0, column=1, padx=10, pady=20)

        self.mainLabel2 = customtkinter.CTkButton(self.sideFrame1, text='Citizen Safety System', font=('arial', 26))
        self.mainLabel2.pack(pady=30)

        self.formFrame = customtkinter.CTkFrame(self.sideFrame1)
        self.formFrame.pack(pady=10, expand=True)
        self.mainLabel1 = customtkinter.CTkButton(self.formFrame, text='Get Details', font=('arial', 20), width=200)
        self.mainLabel1.pack(pady=20)

        # self.lb1 = Label(self.formFrame, text='Enter Vehicle Number', bg=frameColor, font=('arial', 12), fg='white')
        # self.lb1.grid(row=0, column=0)
        self.txt0 = customtkinter.CTkEntry(self.formFrame, placeholder_text='Center ID :', width=400)
        self.txt0.insert(0, center_id)
        self.txt0.configure(state='readonly')
        self.txt1 = customtkinter.CTkEntry(self.formFrame, placeholder_text='Citizen ID :', width=400)
        # self.txt1.grid(row=0, column=1, padx=10)
        self.txt0.pack(pady=10)
        self.txt1.pack(pady=10)
        # self.btn1 = customtkinter.CTkButton(self.formFrame, text='Search')
        # self.btn1.pack(pady=10)
        self.txt2 = customtkinter.CTkEntry(self.formFrame, placeholder_text='Citizen Name', width=400)
        self.txt2.pack(pady=10)
        self.txt3 = customtkinter.CTkEntry(self.formFrame, width=400)
        self.txt3.insert(0, datetime.date.today())
        self.txt3.pack(pady=10)
        self.txt4 = customtkinter.CTkEntry(self.formFrame, width=400)
        self.txt4.insert(0, str(datetime.datetime.now().time()).split('.')[0])
        self.txt4.pack(pady=10)
        customtkinter.CTkLabel(self.formFrame, text="Enter Remarks").pack(pady=4)
        self.txt5 = customtkinter.CTkTextbox(self.formFrame, width=400)
        self.txt5.pack(pady=10)
        self.btn2 = customtkinter.CTkButton(self.formFrame, text='Submit', command=self.getvalues)
        self.btn2.pack(pady=10)

        self.displayFrame = customtkinter.CTkFrame(self.sideFrame2)
        self.displayFrame.pack(pady=10, expand=True, fill='both', padx=10)

        # self.label = Label(self.displayFrame)
        # self.label.pack(anchor=NE)

        self.camLabel = Label(self.displayFrame)
        self.camLabel.pack(anchor=NW)
        # self.cap = cv2.VideoCapture(0)
        # self.show_frames()
        #
        # file = Image.open('face.gif')
        # self.file_frames = file.n_frames
        # self.im = [PhotoImage(file='face.gif', format=f'gif -index {i}') for i in range(self.file_frames)]
        # # print(self.im)
        # self.frameCount = 0
        # self.animnate()

        self.btnFrame = customtkinter.CTkFrame(self.sideFrame2, width=int(sw / 3 * 1.3) + 200)
        self.btnFrame.pack(pady=10, padx=10)
        self.btnFrame.pack_propagate(0)
        self.cameraButton = customtkinter.CTkButton(self.btnFrame, text='Open Camera', command=self.openCamera,
                                                    font=('arial', 20), width=200)
        self.cameraButton.grid(row=0, column=0, pady=20, padx=10)

        self.themeButton = customtkinter.CTkButton(self.btnFrame, text='Dark Theme', font=('arial', 20), width=200,
                                                   command=self.changeTheme)
        self.themeButton.grid(row=0, column=2, pady=20, padx=10)

        self.root.mainloop()

    def openCamera(self):
        self.cap = cv2.VideoCapture(0)
        self.show_frames()
        self.cameraButton.configure(command=self.closeCamera, text='Close Camera')
        self.imageButton = customtkinter.CTkButton(self.btnFrame, text='Capture', font=('arial', 20), width=200,
                                                   command=self.recface)
        self.imageButton.grid(row=0, column=1, pady=20, padx=10)

    def closeCamera(self):
        self.cap.release()
        cv2.destroyAllWindows()
        self.camLabel.configure(image='')
        self.cameraButton.configure(command=self.openCamera, text='Open Camera')
        self.imageButton.destroy()

    def recface(self):
        image_list = os.listdir('citizen')
        # print(image_list)
        for img in image_list:
            # print(img)
            # try:
            result = DeepFace.verify(img1_path=self.frame, img2_path=f"citizen/{img}", model_name='Facenet512')
            print(result)
            if result['verified'] == True:
                self.details(img)
                break

        # except:
        #     print('Face not Found')

    def details(self, img):
        # img2=self.recognizeFace()
        conn = connect()
        cr = conn.cursor()
        q = f"Select * from citizen where image='{img}';"
        cr.execute(q)
        data = cr.fetchall()
        # print(data)
        self.txt1.delete(0, 'end')
        self.txt2.delete(0, 'end')
        self.txt1.insert(0, data[0][0])
        self.txt2.insert(0, data[0][1])

    def animnate(self):
        self.label.configure(image=self.im[self.frameCount])
        self.frameCount += 1
        if self.frameCount == self.file_frames:
            self.frameCount = 0

        self.label.after(50, self.animnate)

    def show_frames(self):
        # Get the latest frame and convert into Image
        flag, self.frame = self.cap.read()
        if flag:
            self.frame = cv2.resize(self.frame, (720, 480))
            self.frame = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
            self.frame = cv2.flip(self.frame, 1)
            img = Image.fromarray(self.frame)

            self.frame2 = ImageTk.PhotoImage(image=img)
            self.camLabel.imgtk = self.frame2
            self.camLabel.configure(image=self.frame2)
            # Repeat after an interval to capture continiously
            self.camLabel.after(20, self.show_frames)

    def changeTheme(self):
        if self.themeButton.cget('text') == 'Dark Theme':
            customtkinter.set_appearance_mode('dark')
            self.themeButton.configure(text='Light Theme')
        else:
            customtkinter.set_appearance_mode('light')
            self.themeButton.configure(text='Dark Theme')

    def getvalues(self):
        citizenid = self.txt1.get()
        centerid = self.txt0.get()
        date = self.txt3.get()
        time = self.txt4.get()
        remarks = self.txt5.get('1.0', 'end-1c')

        conn = connect()
        cr = conn.cursor()
        q = f"insert into remarks values(null,'{citizenid}','{centerid}','{date}','{time}','{remarks}')"
        print(q)
        cr.execute(q)
        conn.commit()
        self.sendRemarks(citizenid)
        msg.showinfo("sucess", "Remarks has been added..")
        self.txt1.delete(0, 'end')
        self.txt2.delete(0, 'end')
        self.txt5.delete(0, 'end')

    def sendRemarks(self, citizen_id):
        q = f"select name, email from citizen where id='{citizen_id}'"
        self.cr.execute(q)
        citizen_data = self.cr.fetchone()
        center_id = self.txt0.get()

        q1 = f"select center.name, center.email, center.mobile, center.area, location.name from center inner join location on center.location = location.id where center.id='{center_id}'"
        self.cr.execute(q1)
        center_data = self.cr.fetchone()
        date = self.txt3.get()
        time = self.txt4.get()
        remarks = self.txt5.get('1.0', 'end-1c')

        message = f'''
            Citizen Name - {citizen_data[0]} has been identified at {time} on {date}.
            
            Here are Center Details - 
            Center Name - {center_data[0]}
            Center Mobile - {center_data[2]}
            Center Email - {center_data[1]}
            Location - {center_data[4]}
            Area - {center_data[3]}
            
            Here are Center Remarks - 
            {remarks}
        '''
        subject = "Citizen Report"

        maildemo.sendEmail(to=citizen_data[1], message=message, subject=subject)

# obj = Main(4)
