Ubuntu


Four main repositories are:

* Main - Canonical-supported free and open-source software
* Universe - Community-maintained free and open-source software
* Restricted - Proprietary drivers for devices
* Multiverse - Software restricted by copyright or legal issues

> 共享文件夹

[问题链接](https://blog.csdn.net/u014665013/article/details/69221524)

> 打开命令行快捷键

`ctrl + alt + t`

> 创建文件夹

`mkdir`

> 查看当前文件夹下文件

`ls`

---

> roscore

使用 ros 时，先在一个窗口中输入 roscore， 启动 ros 环境，然后再打开另外的 命令窗口，运行 ros 其他命令。

---

> .bag 文件转化为 pcd 文件

```

rosrun pcl_ros bag_to_pcd <input_file.bag> <topic> <output_directory>

```

其中的 topic 可以通过以下命令来查看

```
rosbag info <filename.bag>

```

---

> Ros 的一些基本概念

* Nodes

A node is an executable that uses ROS to communicate with other nodes.

* Messages

ROS data type used when subscribing or publishing to a topic.

* Topics

Nodes can publish messages to a topic as well as subscribe to a topic to receive messages.

* Master

Name service for ROS (i.e. helps nodes find each other)

* rosout

ROS equivalent of stdout/stderr

* roscore

Master + rosout + parameter server (parameter server will be introduced later)


# ROS

* 分布式
* 进程管理 进程 节点
* 进程间通信

分布式好处
扩展性好，复用率高

* Gazebo

Slam

## ROS 开发 IDE

RoboWare

RoboWare Studio

ROS 工程结构

catkin 用来编译ROS程序
catkin 工作空间用来组织和管理功能包

> CMakeLists.txt

规定catkin编译的规则 例如：源文件，依赖项，目标文件

> package.xml

定义package的属性

自定义通信格式
消息 message

> Metapackage

他依赖了很多其他的软件包， Stack 功能包集

> ROS 通信架构

Master

管理进程，节点管理器，管理节点之间的通信

roscore: 节点管理器
rosout 日志输出 系统有什么输出
parameter server 参数服务器


> 通信方式

* Topic
* Service
* Parameter Service
* Actionlib



> Topic 异步通信方式

ROS中的异步通讯方式
Node 通过 publish-subscribe机制通信

异步

Message，topic内容的数据类型  类的概念 定义在 *.msg 文件中

基本msg包括
bool，int8， int16，int32，int64

> Service 同步通信方式


 srv 

Service 通信的数据格式，定义在 *.srv 文件中

 Parameter Server

> Action

当一个过程执行时间太长时，长时间的任务，可抢占的任务

*.action 文件

工具
仿真 Gazebo


## Client Library
提供ROS编程的库，CLient Library 类似API


roscpp 执行效率很高

topic，service，param，timer的接口









 



















