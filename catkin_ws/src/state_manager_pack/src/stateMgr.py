#!/usr/bin/env python3

import rospy
from std_msgs.msg import String


def callback(data):
    rospy.loginfo('get')
    rospy.loginfo(rospy.get_caller_id() + 'Find %s', data.data)
    

def listeningState():
    rospy.init_node('ttt', anonymous=True)
    rospy.loginfo('start listening')
    
    rospy.Subscriber('statemanager', String, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listeningState()
