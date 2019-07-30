#!/usr/bin/env python

import Tkinter as tk
import rospy
from std_msgs.msg import Int32

class App():
    def __init__(self):
        self.root = tk.Tk()

        rospy.init_node('listener')
        self.sub = rospy.Subscriber("chatter", Int32, self.NowLoading)

        self.label = tk.Label(text="")
        self.label.pack()
        self.root.mainloop()


    def NowLoading(self, data):
	   #rospy.loginfo("The value is: %i", Garcia.data)
       #now = str(se
       now = data.data
       self.label.configure(text=now)
       self.root.after(1000, self, self.NowLoading)


#if __name__ == '__main__':              
app = App()
