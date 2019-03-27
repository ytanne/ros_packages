#! /usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan
from nav_msgs.msg import Odometry

def callback(msg):
    print(msg)

rospy.init_node('scan_values')
sub = rospy.Subscriber('/scan', LaserScan, callback)
sub = rospy.Subscriber('/odom', Odometry, callback)
rospy.spin()