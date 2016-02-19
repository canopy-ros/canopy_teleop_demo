#!/usr/bin/env python

import rospy
import mavros
from mavros_msgs.msg import OverrideRCIn
from sensor_msgs.msg import Joy

class Controller(object):
    def __init__(self):
        self.pub = rospy.Publisher('/mavros/rc/override', OverrideRCIn,
            queue_size=10)
        self.sub = rospy.Subscriber('/joy', Joy, self.callback)

    def callback(self, data):
        pitch = -data.axes[0] * 500 + 1500
        forward = -data.axes[1] * 500 + 1500
        throttle = data.axes[2] * 500 + 1500
        msg = OverrideRCIn()
        msg.channels[0] = pitch
        msg.channels[1] = forward
        msg.channels[2] = throttle
        msg.channels[3] = 1500
        self.pub.publish(msg) 

if __name__ == "__main__":
    rospy.init_node("controller", anonymous=False)
    c = Controller()
    rospy.spin()
