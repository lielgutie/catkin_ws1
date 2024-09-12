#!/usr/bin/env python

import rospy
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from actionlib import SimpleActionClient

def goal_callback(msg):
    position = msg.target_pose.pose.position
    orientation = msg.target_pose.pose.orientation
    rospy.loginfo("Received Goal:")
    rospy.loginfo("Position: x={}, y={}".format(position.x, position.y))
    rospy.loginfo("Orientation: x={}, y={}, z={}, w={}".format(
        orientation.x, orientation.y, orientation.z, orientation.w))

def main():
    rospy.init_node('goal_echo_node', anonymous=True)
    
    # Subscribe to the 2D Nav Goal topic
    rospy.Subscriber('/move_base_simple/goal', MoveBaseGoal, goal_callback)

    rospy.spin()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
