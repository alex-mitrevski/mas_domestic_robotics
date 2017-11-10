cmake_minimum_required(VERSION 2.8.3)
project(mdr_storing_groceries)

find_package(catkin REQUIRED COMPONENTS
  rospy
  roslint
  std_msgs
  mdr_rosplan_interface
)

catkin_python_setup()

catkin_package()

include_directories(
  ${catkin_INCLUDE_DIRS}
)

roslint_python()
