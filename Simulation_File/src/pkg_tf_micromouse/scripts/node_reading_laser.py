#! /usr/bin/env python

import rospy

from sensor_msgs.msg import LaserScan

def clbk_laser(msg):
    # 720 / 5 = 144
    regions1 = msg.ranges[89]
    regions2 = msg.ranges[179]
    regions3 = msg.ranges[269]
    # [
    #     min(min(msg.ranges[0:143]), 10),
    #     min(min(msg.ranges[144:287]), 10),
    #     min(min(msg.ranges[288:431]), 10),
    #     min(min(msg.ranges[432:575]), 10),
    #     min(min(msg.ranges[576:713]), 10),
    # ]
    print(regions1 , regions2, regions3 )

def main():
    rospy.init_node('reading_laser')
    
    sub = rospy.Subscriber('/my_mm_robot/laser/scan', LaserScan, clbk_laser)
    
    rospy.spin()

if __name__ == '__main__':
    main()
