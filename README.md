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

