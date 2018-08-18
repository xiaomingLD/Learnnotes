# Python Os 库

`os.listdir()` 列出当前目录下的所有文件和文件夹

`os.sep` 更改操作系统中的路径分隔符

`os.getcwd()` 获取当前路径（中间会自动填上一个路径分隔符）

`os.walk（）` 循环遍历目录，返回tuple表，表中每一个tuple包含该层文件、文件夹及该层父节点

`os.path.isfile()` 是否是文件

`os.path.isdir()` 是否是文件夹

`os.path.exists()` 路径是否存在

`os.path.abspath()` 如果输入路径是相对路径，则转换为绝对路径

`os.path.dirname()` 获取指定目录的父目录路径

`os.path.pardir` 获取当前目录的父目录路径

`os.pardir()` 获取当前目录的父目录路径

`os.path.split()` 将目录和文件名分隔开，组成二元组返回

`os.remove()` 删除指定文件

`os.rmdir()` 删除空文件夹

`os.mkdir()` 新建文件夹
