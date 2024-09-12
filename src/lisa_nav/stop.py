#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import Bool

class EmergencyStopNode:
    def __init__(self):
        rospy.init_node('emergency_stop_node', anonymous=True)

        # Publisher to the cmd_vel topic to stop the robot
        self.cmd_vel_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)

        # Subscriber to the emergency stop signal
        self.emergency_stop_sub = rospy.Subscriber('/emergency_stop', Bool, self.emergency_stop_callback)

        rospy.loginfo("Emergency Stop Node Initialized")

    def emergency_stop_callback(self, msg):
        if msg.data:
            rospy.logwarn("Emergency Stop Triggered! Stopping the robot.")
            self.stop_robot()

    def stop_robot(self):
        # Publish zero velocities to stop the robot
        stop_twist = Twist()
        stop_twist.linear.x = 0.0
        stop_twist.linear.y = 0.0
        stop_twist.linear.z = 0.0
        stop_twist.angular.x = 0.0
        stop_twist.angular.y = 0.0
        stop_twist.angular.z = 0.0

        self.cmd_vel_pub.publish(stop_twist)

if __name__ == '__main__':
    try:
        EmergencyStopNode()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
