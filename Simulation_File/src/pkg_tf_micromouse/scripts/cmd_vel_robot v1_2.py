#!/usr/bin/env python
import rospy
import math
from std_msgs.msg import Float64
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from tf import transformations

x_loc = 0 # meter
y_loc = 0
z_ori = 0
# oriantation
    # Front , 0 = |z|
    # Back , 9.99 = |z|
    # Right , z = -w
    # left ,z = w

R_dis = 0
RF_dis = 0
FR_dis = 0
F_dis = 0
FL_dis = 0
LF_dis = 0
L_dis = 0


linear_x = 0 # m/s
angular_z = 0 # rad/s

turning = False
turnLeft = False
turnRight = False
turnBack = False
turn = False
moving = False

T0 = []
angle = 0
T1 = 0
T00 = []
T_dif = 0
T_turn = []


def read_odom(msg):
    global x_loc
    global y_loc
    global z_ori

    x_loc = msg.pose.pose.position.x
    y_loc = msg.pose.pose.position.y
    z_ori = msg.pose.pose.orientation.z
    

def read_laser(msg):
    global R_dis
    global RF_dis
    global FR_dis
    global F_dis
    global FL_dis
    global LF_dis
    global L_dis

    R_dis = msg.ranges[0]
    RF_dis = min( min(msg.ranges[72:143]), 1)
    FR_dis = msg.ranges[89]
    F_dis = msg.ranges[179]
    FL_dis = msg.ranges[269]
    LF_dis = min( min(msg.ranges[216:287]), 1)
    L_dis = msg.ranges[359]
    

def turn(side):
    global linear_x
    global angular_z
    global T_turn
    global turning
    global turnLeft
    global turnRight

    T1 = rospy.Time.now().to_sec()
    T_turn.append( T1 )

    if ( side == "L"):
        angSpeed = 0.2
    else:
        angSpeed = -0.2

    if ( len(T_turn) > 2):
        T_dif = ( T1 - T_turn[1] )
        if ( T_dif > 13):            
            if (T_dif-13 > 12 ):
                linear_x = 0.0
                turning = False
                turnLeft = False
                turnRight = False
                T_turn = []
                print("end")
            else:
                print("moving")
                angular_z = 0.0
                # linear_x = 0.1
                move_without_crash()
        else:
            print("turning L or R")
            angular_z = angSpeed
            linear_x = 0.0


def turn_back():
    global turning
    global turnBack
    global linear_x
    global angular_z
    global T_turn

    T1 = rospy.Time.now().to_sec()
    T_turn.append( T1 )

    if ( len(T_turn) > 2):
        T_dif = ( T1 - T_turn[1])

        if ( T_dif > 26):
            linear_x = 0.0
            turning = False
            turnBack = False
            T_turn = []
            print("end")

            # if (T_dif-26 > 12 ):
            #     linear_x = 0.0
            #     turning = False
            #     turnBack = False
            #     T_turn = []
            #     print("end")
            # else:
            #     print("moving")
            #     angular_z = 0.0
            #     # linear_x = 0.1
            #     move_without_crash()
        else:
            print("turning Back")
            angular_z = 0.2
            linear_x = 0.0


def move_without_crash():
    global RF_dis
    global LF_dis
    global linear_x
    global angular_z

    linear_x = 0.1
    angular_z = 0.0
    if (RF_dis < 0.09):     
        angular_z = 0.01
        if (RF_dis < 0.07):
            linear_x = 0.0
            angular_z = 0.04
        else:
            linear_x = 0.1
    elif (LF_dis < 0.09):
        angular_z = -0.01
        if (LF_dis < 0.07):
            linear_x = 0.0
            angular_z = -0.04
        else:
            linear_x = 0.1
    else:
        angular_z = 0.0


def move():
    global RF_dis
    global F_dis
    global LF_dis
    global moving
    global turning
    global turnRight
    global turnLeft
    global turnBack

    global linear_x
    global angular_z
    global T0
    global T00
    global angle
    global T_dif


    if (L_dis > 0.12 and turnRight ==False and turnBack ==False):
        turning = True
        turnLeft = True
    elif ( R_dis > 0.12 and turnLeft ==False and turnBack ==False):
        turning = True
        turnRight = True
    elif ( F_dis < 0.08 and turnRight ==False and turnLeft ==False):
        turning = True
        turnBack = True

    if (turning == False ):
        print("linear")
        moving = True
        linear_x = 0.1
        angular_z = 0.0
        if (RF_dis < 0.09):     
            angular_z = 0.01
            if (RF_dis < 0.07):
                linear_x = 0.0
                angular_z = 0.04
            else:
                linear_x = 0.1
        elif (LF_dis < 0.09):
            angular_z = -0.01
            if (LF_dis < 0.07):
                linear_x = 0.0
                angular_z = -0.04
            else:
                linear_x = 0.1
        else:
            angular_z = 0.0

    else:        
        linear_x = 0.0
        angular_z = 0.0

        if ( moving ==True and turning ==True):
            T1 = rospy.Time.now().to_sec()
            T0.append( T1 )
            
            if (len(T0) > 2):
                T_dif = ( T1 - T0[1] )

                if (T_dif > 4.8):                
                    linear_x = 0.0
                    T0 = []
                    moving = False
                else:
                    print("turning point")
                    # linear_x = 0.1
                    move_without_crash()
                    angular_z = 0.0
        elif ( moving ==False and turning ==True):
            if (turnLeft == True):
                turn("L")
            elif (turnRight == True):
                turn("R")
            elif (turnBack == True):
                turn_back()


            

    # if (F_dis < 0.08 and FL_dis < 0.115 and FR_dis < 0.115):
    #     turning = True
    #     if (R_dis > 0.12 and turnLeft ==False and turnBack ==False):
    #         turnRight = True
    #     elif (L_dis > 0.12 and turnRight ==False and turnBack ==False):
    #         turnLeft = True
    #     elif (turnRight ==False and turnBack ==False):
    #         turnBack = True
    #     else:
    #         print("not turning")

    # if (turning == False):
    #     linear_x = 0.2
    #     angular_z = 0.0
    #     if (RF_dis < 0.09):     
    #         angular_z = 0.01
    #         if (RF_dis < 0.07):
    #             linear_x = 0.0
    #             angular_z = 0.04
    #         else:
    #             linear_x = 0.2
    #     elif (LF_dis < 0.09):
    #         angular_z = -0.01
    #         if (LF_dis < 0.07):
    #             linear_x = 0.0
    #             angular_z = -0.04
    #         else:
    #             linear_x = 0.2
    #     else:
    #         angular_z = 0.0
    # else:
    #     linear_x = 0.0
    #     angular_z = 0.0
    #     T1 = rospy.Time.now().to_sec()
    #     T0.append( T1 )
    #     # print(T0)
    #     if (turnRight ==True):
    #         print("turnRight True")
    #         angular_z = - 0.2
    #         if (len(T0) > 2):
    #             angle = 0.2*( T1 - T0[1] )
    #         if (angle > 2.4):
    #             angular_z = 0.0
    #             turnRight = False
    #             turning = False
    #             T0 = []
    #             angle = 0
    #             print("--------------------------------------------------")

    #     elif (turnLeft ==True):
    #         print("turnLeft True")
    #         angular_z = 0.2
    #         if (len(T0) > 2):
    #             angle = 0.2*( T1 - T0[1] )
    #         if (angle > 2.4):
    #             angular_z = 0.0
    #             turnLeft = False
    #             turning = False
    #             T0 = []
    #             angle = 0
    #             print("--------------------------------------------------")

    #     elif (turnBack ==True):
    #         print("turnBack True")
    #         angular_z = 0.2
    #         if (len(T0) > 2):
    #             angle = 0.2*( T1 - T0[1] )                
    #         if (angle > 5):
    #             angular_z = 0.0
    #             turnBack = False
    #             turning = False
    #             T0 = []
    #             angle = 0
    #             print("--------------------------------------------------")
            

    #     else:
    #         print("turning error")
    

def main():
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    sub_odom = rospy.Subscriber('/odom', Odometry, read_odom) 
    sub_laser = rospy.Subscriber('/my_mm_robot/laser/scan', LaserScan, read_laser)  
    rospy.init_node('robot', anonymous=True)
    rate = rospy.Rate(50) # 40hz

    while not rospy.is_shutdown():

        move()

        msg1 = Twist()        
        msg1.linear.x = linear_x
        msg1.angular.z = angular_z
        pub.publish(msg1)

        # print( "linear_x", linear_x )
        # print( "angular_z", angular_z )

        rate.sleep()


if __name__ == '__main__':
    main()
