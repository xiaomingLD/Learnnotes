因此，多人协作的工作模式通常是这样：

首先，可以试图用git push origin <branch-name>推送自己的修改；

如果推送失败，则因为远程分支比你的本地更新，需要先用git pull试图合并；

如果合并有冲突，则解决冲突，并在本地提交；

没有冲突或者解决掉冲突后，再用git push origin <branch-name>推送就能成功！

如果git pull提示no tracking information，则说明本地分支和远程分支的链接关系没有创建，用命令git branch --set-upstream-to <branch-name> origin/<branch-name>。

这就是多人协作的工作模式，一旦熟悉了，就非常简单。

[Git 学习往网站](https://www.yiibai.com/git/git_basic_concepts.html)

## 命令行

### 账户设置

初始化账户:

`git config --global user.name "John Doe"`

`git config --global user.email johndoe@example.com`

检查配置 `git config --list`

查看状态 `Git status`

### git add 命令

把所有add `git add .`

### git push 命令

> git push 用于将本地分支的更新，推送到远程主机

`git push <远程主机名> <本地分支名>`


将当前分支推送到 origin 主机的对应分支 `git push origin`

如果当前分支与多个主机存在追踪关系，可以使用 `-u` 选项选定一个默认主机，这样后面就可以不加任何参数使用 `git push`, 例如 `git push -u origin master` 将本地 master 分支推送到 origin 主机，同时指定 origin 为默认主机，以后再推送就不用再加任何参数了

### git fetch 命令
> 远程跟踪分支已更新（commit），需要将这些更新取回本地

将某个远程主机的更新，全部取回本地 `git fetch`

取回主机的某个分支 `git fetch <远程主机名> <分支名>` 例如 `git fetch origin <分支名>`

### git merge 命令

> git merge 用于将两个或两个以上的开发历史合并一起

在当前分支上，合并 origin/master `git merge origin/master`

讲一个分支合并到另一个分支的步骤：
例如，将分支Samstag合并到分支daily上

1. `git checkout daily` 切换到分支daily上

2. `git merge samstag` 把samstag分支合并到当前分支daily上

3. `git branch -d samstag` 删除分支samstag

### git branch 命令

查看本地分支 `git branch`

查看远程分支 `git branch -r`

查看所有分支 `git branch -a`

从一个分支跳到另一个分支 `git checkout <branch>`

### git checkout 命令

> git checkout 命令用于切换分支或恢复工作树文件

取回远程主机的更新后，可以在此基础上，创建新的分支 `git checkout -b newBrach origin/master`

放弃修改 `git checkout .`

### git 本地密码缓存问题

~~~
unable to access ' https://git.coding.net/xxxx/xxxx.git/ ': The requested URL returned error: 403
~~~

在clone远程仓库的时候，因为第一次在输入密码的时候，输入了错误的密码，但是系统自动记住了这个错误密码，导致每次clone输入的都是错误的密码，所以每次都会出现这个错误。解决办法可以在这个[链接里](https://www.jianshu.com/p/77b0340a02f3)得到。


> 一个人在本地建立了分支，并且推送到远程仓库，别的人并不能看到这个远程分支，这时候解决办法

1. `git fetch` 命令更新remote索引
2. `git branch -a` 查看所有分支
3. `git checkout <branch>` 切换到分支


> 别人对文档进行了修改，本地fetch后，必须加入 `git merge` 才能看到别人的修改

再试一试


dfdf

<<<<<<< HEAD
2. 修改好后，按下Esc (退出编辑状态)； 接着连按两次大写字母Z，你会惊喜的发现，终于保存好退出来了！


这是除了什么事情
=======
dfdf
>>>>>>> 2c3ae1d16648d8f1825333f1d9d310763b90e91f
