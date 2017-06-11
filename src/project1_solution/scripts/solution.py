#!/usr/bin/env python
import rospy

from std_msgs.msg import Int16
from project1_solution.msg import TwoInts

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + 'I heard %s', data)

    pub = rospy.Publisher('sum', Int16, queue_size = 10)

    rate = rospy.Rate(0.5)

    #while not rospy.is_shutdown():
    final_sum = data.a + data.b
    rospy.loginfo('sum = ' + str(final_sum))
    pub.publish(final_sum)
    rate.sleep()

def solution():
    rospy.init_node('solution', anonymous = True)

    #Subscribe to two_ints topic and publishes to sum topic
    rospy.Subscriber('two_ints', TwoInts, callback)

    rospy.spin()

if __name__ == '__main__':
    try:
        solution()
    except rospy.ROSInterruptException:
        pass
