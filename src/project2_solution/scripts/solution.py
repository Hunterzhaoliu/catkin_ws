#!/usr/bin/env python
import rospy

import numpy

import tf
import tf2_ros
import geometry_msgs.msg

def publish_transforms():
    object_transform = geometry_msgs.msg.TransformStamped()
    object_transform.header.stamp = rospy.Time.now()
    object_transform.header.frame_id = "base_frame"
    object_transform.child_frame_id = "object_frame"
    object_transform.transform.translation.x = 0.0
    object_transform.transform.translation.y = 1.0
    object_transform.transform.translation.z = 1.0
    object_quaternion = tf.transformations.quaternion_from_euler(0.79, 0.0, 0.79)
    object_transform.transform.rotation.x = object_quaternion[0]
    object_transform.transform.rotation.y = object_quaternion[1]
    object_transform.transform.rotation.z = object_quaternion[2]
    object_transform.transform.rotation.w = object_quaternion[3]
    br.sendTransform(object_transform)

    robot_transform = geometry_msgs.msg.TransformStamped()
    robot_transform.header.stamp = rospy.Time.now()
    robot_transform.header.frame_id = "base_frame"
    robot_transform.child_frame_id = "robot_frame"
    robot_transform.transform.translation.x = 0.0
    robot_transform.transform.translation.y = -1.0
    robot_transform.transform.translation.z = 0.0
    robot_quaternion = tf.transformations.quaternion_from_euler(0.0, 0.0, 1.5)
    robot_transform.transform.rotation.x = robot_quaternion[0]
    robot_transform.transform.rotation.y = robot_quaternion[1]
    robot_transform.transform.rotation.z = robot_quaternion[2]
    robot_transform.transform.rotation.w = robot_quaternion[3]
    br.sendTransform(robot_transform)

    camera_transform = geometry_msgs.msg.TransformStamped()
    camera_transform.header.stamp = rospy.Time.now()
    camera_transform.header.frame_id = "robot_frame"
    camera_transform.child_frame_id = "camera_frame"
    camera_transform.transform.translation.x = 0.0
    camera_transform.transform.translation.y = 0.1
    camera_transform.transform.translation.z = 0.1
    camera_quaternion = tf.transformations.quaternion_from_euler(0.0, -.46, 0.0)
    camera_transform.transform.rotation.x = camera_quaternion[0]
    camera_transform.transform.rotation.y = camera_quaternion[1]
    camera_transform.transform.rotation.z = camera_quaternion[2]
    camera_transform.transform.rotation.w = camera_quaternion[3]
    br.sendTransform(camera_transform)

if __name__ == '__main__':
    rospy.init_node('project2_solution')

    br = tf2_ros.TransformBroadcaster()
    rospy.sleep(0.5)

    while not rospy.is_shutdown():
        publish_transforms()
        rospy.sleep(0.05)
