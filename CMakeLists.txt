cmake_minimum_required(VERSION 2.8.3)
project(roscloud_teleop_demo)

find_package(catkin REQUIRED COMPONENTS
  rospy
  std_msgs
)

catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES roscloud
#  CATKIN_DEPENDS rospy std_msgs
#  DEPENDS system_lib
)

include_directories(
  ${catkin_INCLUDE_DIRS}
)

# catkin_add_nosetests(test)
