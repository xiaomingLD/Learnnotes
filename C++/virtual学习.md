
* 定义一个函数为虚函数，不代表函数为不被实现的函数，定义他为虚函数是为了允许用基类的指针来调用子类的这个函数。定义一个虚函数为纯虚函数，才代表函数没有被实现。定义纯虚函数是为了实现一个接口，起到一个规范的作用，规范继承这个类的程序员必须实现这个函数。

* 虚函数只能借助于指针或者引用来达到多态的效果。


# 纯虚函数

> 定义

纯虚函数是在基类中声明的虚函数，它在基类中没有定义，但要求任何派生类都定义自己的实现方式。在基类中实现纯虚函数的方法是在函数原型后面加"=0"。

* 含有纯虚函数的类为抽象类，不能实例化创建对象

> 意义

使派生类仅仅是继承函数的接口。

> 注意

•   抽象类只能作为基类来使用，其纯虚函数的实现由派生类给出。如果派生类中没有重新定义纯虚函数，而只是继承基类的纯虚函数，则这个派生类仍然还是一个抽象类。如果派生类中给出了基类纯虚函数的实现，则该派生类就不再是抽象类了，它是一个可以建立对象的具体的类。

•   抽象类是不能定义对象的。

---------------------

本文来自 hackbuteer1 的CSDN 博客 ，全文地址请点击：https://blog.csdn.net/Hackbuteer1/article/details/7558868?utm_source=copy


# C++ virtual

## virtual 继承

虚继承的目的是令某个类作出声明，承诺愿意共享它的基类。共享的基类子对象称为虚基类

## 析构函数 virtual 函数
