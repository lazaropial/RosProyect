#!/usr/bin/env python

import Tkinter as tk
from Tkinter import *
import rospy
from std_msgs.msg import Int32

class App():
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("700x394")
        self.root.wm_title("Serial Communication") #Makes the title that will appear in the top left
        self.root.config(background = "#FFFFFF")
        rospy.init_node('listener')
        self.sub = rospy.Subscriber("chatter", Int32, self.NowLoading)
        self.label = tk.Label(text="")

        #Left Frame and its contents
        self.leftFrame = Frame(self.root, width=300, height = 600, bg="white")
        self.leftFrame.grid(row=0, column=0, padx=10, pady=2)

        Label(self.leftFrame, text="Instructions",fg="black",bg="white",font=("Arial")).grid(row=0, column=0, padx=10, pady=2)

        Instruct = Label(self.leftFrame, text="1. Run the Interface\n2. Run the Node that increase the value\n")
        Instruct.grid(row=1, column=0, padx=10, pady=2)

        #Right Frame and its contents
        self.rightFrame = Frame(self.root, width=300, height = 600, bg="white")
        self.rightFrame.grid(row=0, column=1, padx=10, pady=2)

        Label(self.rightFrame, text="Datos:",fg="black",bg="white",font=("Arial")).grid(row=0, column=0, padx=10, pady=2)


        self.root.mainloop()


    def NowLoading(self, data):

       now = data.data
       Increasing = Label(self.rightFrame, text=now, bg="white", fg="black")
       Increasing.grid(row=1, column=0,padx=10,pady=2)

       self.root.after(1000, self, self.NowLoading)


#if __name__ == '__main__':
app = App()
