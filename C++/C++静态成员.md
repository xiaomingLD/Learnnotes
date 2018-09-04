# C++ 中如何定义一个全局变量

两种方式：

1. 传统方式 extern

```
extern int number;

```
2. static 方式

_把变量声明放在类大括号之内，变量定义语句放在类体之外_
```
class Object
{
  public:
    static int number;
}

```
