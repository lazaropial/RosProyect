#!/usr/bin/env python

import Tkinter as tk
from Tkinter import *
import rospy
from std_msgs.msg import Int32

class App():
    def __init__(self):
        color_LightBlue = '#6DAEE5'

        self.root = tk.Tk()
        self.root.geometry("720x480")
        self.root.wm_title("Serial Communication") #Makes the title that will appear in the top left
        self.root.config(background = "#FFFFFF")
        self.background = tk.PhotoImage(file="/home/rodrigo/catkin_ws/src/beginner_tutorials/images/background.png")
        self.back = tk.Label(image=self.background)
        rospy.init_node('listener')
        self.sub = rospy.Subscriber("chatter", Int32, self.NowLoading)

        #LEFT rame and its contents
        self.leftFrame = Frame(self.root, width=300, height = 600, bg="dark blue")
        self.leftFrame.grid(row=0, column=0, padx=45, pady=68)

        Label(self.leftFrame, text="GPS Data",fg="white",bg="dark blue",font=("Arial")).grid(row=0, column=0, padx=10, pady=2)

        Instruct = Label(self.leftFrame, text="1. Altitude\n2. Latitude\n3. Longitud", bg="dark blue", fg="white")
        Instruct.grid(row=1, column=0, padx=45, pady=2)

        #MIDDLE Frame and its contents
        self.middleFrame = Frame(self.root, width=180, height = 30, bg='#6DAEE5')
        self.middleFrame.grid(row=0, column=1, padx=150, pady=0)

        Label(width=20, height = 1,text="usuario@192.168.1.99",fg="black",bg="#68A6DB",font=("Arial",11)).place(x=280, y=4)

        #RIGHT Frame and its contents
        self.rightFrame = Frame(self.root, width=300, height = 600, bg="white")
        self.rightFrame.grid(row=0, column=2, padx=0, pady=2)

        Label(self.rightFrame, text="AHRS Data:",fg="black",bg="white",font=("Arial")).grid(row=0, column=0, padx=10, pady=2)


        self.root.mainloop()


    def NowLoading(self, data):

       now = data.data
       self.back.place(x=0,y=0,relwidth=1,relheight=1)
       Increasing = Label(self.leftFrame, text=now, bg="dark blue", fg="white")
       Increasing.grid(row=2, column=0,padx=10,pady=2)

       self.root.after(1000, self, self.NowLoading)


#if __name__ == '__main__':
app = App()
