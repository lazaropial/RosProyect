# RosProyect
Important notes

For the raspberry pi:
We are using ubiquity robotics operating system instead of rasbian due to it already has ROS installed
## Every time that the raspberry pi boots for the very fist time do the following:

You must enable the following **repositories**:
```
UNIVERSE: sudo add-apt-repository universe
MULTIVERSE:sudo add-apt-repository multiverse
RESTRICTED: sudo add-apt-repository restricted
```
Configure the locals:
```
export LC_ALL="en_US.UTF-8"
export LC_CTYPE="en_US.UTF-8"
sudo dpkg-reconfigure locales
```
A window will appear, just ignore everything and lick "ok"

To install openCV for python in the raspberry pi follow the steps from:
> https://github.com/tizianofiorenzani/how_do_drones_work/blob/master/opencv/OPENCV_INSTALL.txt

Run video.py example
To stream the video through ssh run the following command:
```
  ssh -X user@ip_user 
 ```
 then run the opencv video example, and you should be able to see the video
 
for reference to implement Tkinter in ROS:
> https://github.com/Choitek/mmmros-tutorials/blob/master/mmm_teleop/teleop_node.py

# In case you want to use joy_node with an xbox control(in our case)
You need to install the joy_node. You can copy and paste into your terminal:
> http://wiki.ros.org/joy/Tutorials/ConfiguringALinuxJoystick

Be careful at the moment you type the distribution, e.g. kinetic, melodic, indigo, etc
> $ sudo apt-get install ros-indigo-joy
