cmake_minimum_required(VERSION 2.8.3)
project(mdr_ask_action)

find_package(catkin REQUIRED COMPONENTS
  actionlib
  actionlib_msgs
  genmsg
  message_generation
  roslint
  rospy
)

catkin_python_setup()
roslint_python()

add_action_files(DIRECTORY ros/action
  FILES
  Ask.action
)

generate_messages(
  DEPENDENCIES
  actionlib_msgs
)

catkin_package(
 CATKIN_DEPENDS
   actionlib_msgs
   message_runtime
   std_msgs
)

include_directories(
  ${catkin_INCLUDE_DIRS}
)

install(PROGRAMS
  ros/scripts/ask
  ros/scripts/ask_client_test
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}/scripts
)
