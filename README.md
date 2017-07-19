# catkin_ws

Robotics workspace

## Setup Instructions on Ubuntu 16.04
1. `catkin_make` in catkin_ws
2. `source devel/setup.bash`

## Project 1 ROSS Nodes and Topics
Learning how to use nodes to subscribe and publish to topics.

### Run Instructions
1. `roscore`
2. In a new terminal `rosrun two_int_talker two_int_talker.py`
3. In a new terminal `rosrun project1_solution solution.py`

![alt text](https://user-images.githubusercontent.com/2585159/27008301-b083b68c-4e33-11e7-9f70-24aceda23a25.png)

## Project 2 Transforms
Learning how to create transforms of objects in different coordinate frames.

### Run Instructions
1. `roscore`
2. In a new terminal `rosrun rviz rviz`
3. In a new terminal `rosrun marker_publisher marker_publisher`
4. In a new terminal `rosrun project2_solution solution.py`

![alt text](https://user-images.githubusercontent.com/2585159/27256895-82133fc4-5389-11e7-9f92-eb91e33b1ea3.png)

## Project 3 Forward Kinematics
Learning how to compute coordinate transforms between the world_link to other links using q values and revolute joints.

### Run Instructions
1. `roscore`
2. In a new terminal `rosparam set robot_description --textfile kuka_lwr_arm.urdf`
3. In the same terminal `rosrun robot_sim robot_sim_bringup`
4. In a new terminal `rosrun robot_mover mover`
5. In a new terminal `rosrun forward_kinematics solution.py`
6. In a new terminal `rosrun rviz rviz`

![alt text](https://user-images.githubusercontent.com/24757872/27772884-acb29b1e-5f30-11e7-9bab-ed3402e1c2d6.png)

## Project 4 Cartesian Control
Learn how to compute joint (q) velocity given initial base to end effector transform and desired base to end effector transform.

### Run Instructions
1. `roscore`
2. In a new terminal in home directory `rosparam set robot_description --textfile kuka_lwr_arm.urdf`
3. In the same terminal `rosrun robot_sim robot_sim_bringup`
4. In a new terminal `rosrun robot_state_publisher robot_state_publisher`
5. In a new terminal `rosrun cartesian_control marker_control.py`
6. In a new terminal `rosrun cartesian_control cartesian_control.py`
7. In a new termianl `rosrun rviz rviz`
8. In rviz change Fixed Frame to world link_name
9. In rviz click Add and select RobotModel
10. In rviz click Add and select "InteractiveMarkers"
