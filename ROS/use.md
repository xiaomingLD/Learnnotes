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
