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

### git 常见问题
---
> git 本地密码缓存问题

git 会存储用户的用户名，储存方式有三种方式：

* 缓存cache
* 保存在硬盘store
* 保存在钥匙串 osxkeychain

如果第一次输入了错误的密码，系统会记住错误的密码，之后在拉取或者推送的时候会出现错误提示：

~~~
unable to access ' https://git.coding.net/xxxx/xxxx.git/ ': The requested URL returned error: 403
~~~

解决办法可以在这个[链接里](https://www.jianshu.com/p/77b0340a02f3)得到。

1. 可以通过 `git help -a | grep credential` 命令查看系统支持的crendential

2.  通过 `git config -- list` 查看自己的 git 的全局配置，其中可以看到 `credential.helper = ` 自己电脑中的配置

解决办法：

1. 清空配置

找到 /Users/xxx/.gitconfig 文件，清除里面的 credential 命令， 清除之后可以通过 `git config credential.helper` 查看当前的credential是否已经被清空

2. 一个电脑上可能存在多个.gitconfig文件，可以通过命令 `git config --show-origin --get credential.helper` 查看 credential.helper 所在的文件目录，找到配置文件后打开，进行步骤 1  的操作即可

重新配置：

* 配置成 store `git  config --global  credential.helper store`




---
> 一个人在本地建立了分支，并且推送到远程仓库，别的人并不能看到这个远程分支，这时候解决办法

1. `git fetch` 命令更新remote索引
2. `git branch -a` 查看所有分支
3. `git checkout <branch>` 切换到分支

---
> 别人对文档进行了修改，本地fetch后，必须加入 `git merge` 才能看到别人的修改

---
> 一些情况下，自动跳入要求加备注的栏，不能退出

1. 按 c 开始编辑

2. 修改好后，按下Esc (退出编辑状态)； 接着连按两次大写字母Z，你会惊喜的发现，终于保存好退出来了！

---
> 查看远程仓库是不是有新的分支

`git remote update origin`

---
> 远程仓库的一个分支已被删除，但是本地还是可以看到远程有这个分支，怎么把？

1. ` git remote show origin` 可以查看remote地址，远程分支情况
2. `git remote prune origin` 可以删除本地远程不存在的分支

---
> git 删除远程仓库的一个分支

`git push origin :<远程仓库分支名> `  远程仓库分支名前面的 ： 是删除的意思

---
> 把一个分支合并到另一个分支上，可以合并分支上的提交，然后再合并 `git merge --squash abc`


---
> 把notepad++ 作为 `git commit` 的默认编辑器

`git config --global core.editor "'D:\Notepad++\notepad++.exe' -multiInst -notabbar -nosession -noPlugin '$*'"` 要注意改变程序地址 !!!

---
> Git push 到远程仓库时不能推送，出现冲突，怎么解决

1. `git fetch` 拉取远程分支
2. `git merge`
3. 会出现 conflict 命令，然后进入解决冲突模式
4. 可以通过 `git checkout <文件路径加文件名> --ours` 命令保存自己的改动或者通过 `git checkout <文件路径加文件名> --theirs` 命令保存对方的
5. git commit 提交
6. git push 推送到远程仓库

---
