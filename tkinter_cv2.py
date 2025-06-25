from tkinter import *
import cv2
from PIL import Image, ImageTk

class Main:
    def __init__(self):
        self.root = Tk()
        self.root.geometry('800x800')
        self.root.title('Tkinter and OpenCv')

        self.f = Frame(self.root)
        self.f.pack(pady=20)

        self.bt1 = Button(self.f, text='Start', font=('arial', 14), command=self.startvideo)
        self.bt2 = Button(self.f, text='Stop', font=('arial', 14), command=self.stopvideo)
        self.bt1.grid(row=0, column=0, pady=20, padx=10)
        self.bt2.grid(row=0, column=1, pady=20, padx=10)

        self.lb = Label(self.root)
        self.lb.pack()


        self.root.mainloop()

    def startvideo(self):
        self.video = cv2.VideoCapture(0)
        self.playvideo()
    def playvideo(self):
        frame = self.video.read()[1]
        cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

        face = cascade.detectMultiScale(frame, 1.1, 4)
        # print(face)
        for x, y, w, h in face:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)


        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = cv2.flip(frame, 1)
        img = Image.fromarray(frame)

        imgTk = ImageTk.PhotoImage(image=img)
        self.lb.imgTk = imgTk
        self.lb.configure(image=imgTk)
        self.lb.after(20, self.playvideo)



    def stopvideo(self):
        self.video.release()
        cv2.destroyAllWindows()
        self.lb.configure(image='')

obj = Main()