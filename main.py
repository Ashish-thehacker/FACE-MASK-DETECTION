from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from student import Student
from face_camera import Face_Camera
from attendance import Attendance
import os

class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face_Recogonition_System")

        bg1=Image.open(r"Images_GUI\bg3.jpg")
        bg1=bg1.resize((1366,768),Image.ANTIALIAS)
        self.photobg1=ImageTk.PhotoImage(bg1)

        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0,y=0,width=1366,height=768)


        title_lb1 = Label(bg_img,text="Attendance Managment System By System Zombies",font=("Chiller",30,"bold"),bg="Black",fg="white")
        title_lb1.place(x=0,y=0,width=1366,height=45)

        std_img_btn=Image.open(r"Images_GUI\std1.jpg")
        std_img_btn=std_img_btn.resize((250,250),Image.ANTIALIAS)
        self.std_img1=ImageTk.PhotoImage(std_img_btn)

        std_b1 = Button(bg_img,command=self.student_pannels,image=self.std_img1,cursor="hand2")
        std_b1.place(x=50,y=250,width=250,height=250)

        std_b1_1 = Button(bg_img,command=self.student_pannels,text="Student Pannel",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        std_b1_1.place(x=50,y=500,width=250,height=45)

        det_img_btn=Image.open(r"Images_GUI\det1.jpg")
        det_img_btn=det_img_btn.resize((250,250),Image.ANTIALIAS)
        self.det_img1=ImageTk.PhotoImage(det_img_btn)

        det_b1 = Button(bg_img,command=self.face_rec,image=self.det_img1,cursor="hand2",)
        det_b1.place(x=320,y=250,width=250,height=250)

        det_b1_1 = Button(bg_img,command=self.face_rec,text="Face Detector",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        det_b1_1.place(x=320,y=500,width=250,height=45)

        att_img_btn=Image.open(r"Images_GUI/att.jpg")
        att_img_btn=att_img_btn.resize((250,250),Image.ANTIALIAS)
        self.att_img1=ImageTk.PhotoImage(att_img_btn)

        att_b1 = Button(bg_img,command=self.attendance_pannel,image=self.att_img1,cursor="hand2",)
        att_b1.place(x=590,y=250,width=250,height=250)

        att_b1_1 = Button(bg_img,command=self.attendance_pannel,text="Attendance",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        att_b1_1.place(x=590,y=500,width=250,height=45)

        hlp_img_btn=Image.open(r"Images_GUI/arduino.jpg")
        hlp_img_btn=hlp_img_btn.resize((180,180),Image.ANTIALIAS)
        self.hlp_img1=ImageTk.PhotoImage(hlp_img_btn)

        hlp_b1 = Button(bg_img,command=self.ard_fun,image=self.hlp_img1,cursor="hand2",)
        hlp_b1.place(x=860,y=250,width=250,height=250)

        hlp_b1_1 = Button(bg_img,command=self.ard_fun,text="Arduino",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        hlp_b1_1.place(x=860,y=500,width=250,height=45)

        

        exi_img_btn=Image.open(r"Images_GUI/exi.jpg")
        exi_img_btn=exi_img_btn.resize((90,90),Image.ANTIALIAS)
        self.exi_img1=ImageTk.PhotoImage(exi_img_btn)

        exi_b1 = Button(bg_img,command=self.Close,image=self.exi_img1,cursor="hand2",)
        exi_b1.place(x=1200,y=620,width=90,height=90)

        exi_b1_1 = Button(bg_img,command=self.Close,text="Exit",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        exi_b1_1.place(x=1200,y=703,width=90,height=45)


    def open_img(self):
        os.startfile("dataset")

    def student_pannels(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    
    def face_rec(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Camera(self.new_window)
    
    def attendance_pannel(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)


    def ard_fun(self):
        self.new_window=Toplevel(self.root)
        self.app=mask_temp.detect_video(self.new_window)

    


    def Close(self):
        root.destroy()
    
    





if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()
