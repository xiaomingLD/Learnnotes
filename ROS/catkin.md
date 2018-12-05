# Create catkin Workspace

1. $ mkdir -p catkin_ws/src
2. $ cd catkin_ws
3. $ catkin_make
4. $ source devel/setup.bash

# Building Packages in a catkin Workspace

1. $ cd catkin_ws/src
2. $ catkin_create_pkg <package name> <dependency>

# Building a catkin workspace and sourcing the setup file

1. $ cd catkin_ws
2. $ catkin_make

# To add the workspace to your ROS enironment you need to source the generated setup file:

$ source catkin_ws/devel/setup.bash

 
