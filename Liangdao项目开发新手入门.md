# 1. 摘要

本文的面向对象是没有项目开发经验的亮道新入职员工，或者已有开发经验但是刚入职，不熟悉亮道公司软件开发流程以及工具的员工

本文的目的是使读者快速熟悉亮道的软件开发工具，并且快速入门，加入亮道的软件开发项目

前期准备，阅读此文档的读者需要对以下工具有基本的了解：

* Git

Git是一种分布式版本控制系统，Git的入门可以通过以下链接 [Git入门，廖雪峰]("https://www.liaoxuefeng.com/wiki/0013739516305929606dd18361248578c67b8067c8c017b000") 学习。

# 2. 登录 phabricator

phabricator是一个开放源代码的软件开发平台，它集成了一系列开源的Web应用程序，用以帮助软件公司开发更好的软件。phabricator支持Git，Mercurial，Subversion。

1. 使用phabricator，首先需要注册一个账号，注册账号请联系公司  

  > 服务器管理员

2. 管理员帮助注册账号后，在利用Git克隆项目之前，需要先设置克隆密码，点击右上角头像，然后选中 _Settings_

![Settings](https://ld-1257319773.cos.ap-beijing.myqcloud.com/wiki/phabricator/Pha1.png)

在左侧 _AUTHENTICATION_ 下点击 _Password_ ， 并设定克隆密码

![password](https://ld-1257319773.cos.ap-beijing.myqcloud.com/wiki/phabricator/Pha2.png)

3. 加入项目

在phabricator主页的左侧点击 _Diffusion_, 可以看到项目，有的项目可能需要先加入Projects才能看到

![Diffusion](https://ld-1257319773.cos.ap-beijing.myqcloud.com/wiki/phabricator/Pha3.png)

进入想要clone的项目，点击右侧绿色的Clone按钮，可以复制远程仓库地址，在第一次复制远程仓库的过程中，需要输入phabricator的用户名和密码

![Diffusion](https://ld-1257319773.cos.ap-beijing.myqcloud.com/wiki/phabricator/pha4.gif)

4. 克隆项目

在本地建立项目文件夹，运行Git bash，键入命令 `git clone  远程仓库地址 ` 就可以克隆远程仓库到本地，不过这时候只是复制了Master分支，可以通过命令 `git branch -r` 查看所有的远程和本地分支，然后通过命令 `git checkout -b 分支名 origin/分支名` 将远程分支clone到本地

# 3. 配置和使用 Anaconda, PyCharm

## 3.1 Anaconda

Anaconda 指的是一个开源的 Python 发行版本，其包含了 conda、Python 等180多个科学包及其依赖项。Anaconda 包括 Conda、Python 以及一大堆安装好的工具包，比如：numpy、pandas、matplotlib 等

### 3.1.1 安装 Anaconda

可以在 [ Anaconda 官网 ](https://www.anaconda.com/) 上下载安装包并安装

### 3.1.2 安装 Python 工具包

安装好 Anaconda 后， 打开 Anaconda Navigator，在 Environments 中可以安装所需的 Python 工具包，首先搜索需要的工具包，然后安装

![Ana](https://ld-1257319773.cos.ap-beijing.myqcloud.com/wiki/Anaconda/ana1.gif)

## 3.2 PyCharm

PyCharm 是一种 Python IDE，带有一整套可以帮助用户在使用 Python 语言开发时提高其效率的工具，比如调试、语法高亮、Project 管理、代码跳转、智能提示、自动完成、单元测试、版本控制。此外，PyCharm 还提供了一些高级功能，以用于支持Django框架下的专业 Web 开发。

### 3.2.1 安装 PyCharm

PyCharm 的下载可以在官网 [PyCharm](http://www.jetbrains.com/pycharm/) 或者可以直接使用本地服务器中的安装包 [PyCharm](\\192.168.1.60\资料库\软件\开发软件\PyCharm) 下载并安装。

### 3.2.2 配置 PyCharm  

打开 PyCharm, 点击 Open, 定位到本地的Git库文件夹

![openproject](https://ld-1257319773.cos.ap-beijing.myqcloud.com/wiki/PyCharm/pycharm1.png)

需要对软件进行配置，点击 _File->Settings_

![openproject](https://ld-1257319773.cos.ap-beijing.myqcloud.com/wiki/PyCharm/pycharm2.png)

在弹出的对话框中选择 _Project sensoreval->Project Interpreter_， 在 Project Interpreter 的下拉菜单中选择 Anaconda 的 Python 安装目录（如果电脑中装了多个 Python 的 版本，需要自己选择，如果只安装了 Anaconda，系统一般会默认定位到 Anaconda 下边的 Python 安装目录 ）。

![openproject](https://ld-1257319773.cos.ap-beijing.myqcloud.com/wiki/PyCharm/pycharm3.png)
