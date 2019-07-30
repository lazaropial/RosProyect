#!/usr/bin/env python

import rospy
from std_msgs.msg import Int32

def talker():
	talker_topic = rospy.Publisher('chatter', Int32, queue_size = 20) 
	rospy.init_node('talker', anonymous = True) 
	rate = rospy.Rate(10) 
	hello_str = 1
	while not rospy.is_shutdown(): 
		rospy.loginfo(hello_str)
		talker_topic.publish(hello_str)
		hello_str = hello_str + 1
		rate.sleep()

if __name__ == '__main__':	
	try:				
		talker()
	except rospy.ROSInterruptException:		
		pass
