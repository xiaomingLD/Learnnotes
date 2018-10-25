class noncopyable的基本思想是把构造函数和析构函数设置protected权限，这样子类可以调用，但是外面的类不能调用，那么当子类需要定义构造函数的时候不至于通不过编译。但是最关键的是noncopyable把复制构造函数和复制赋值函数做成了private，这就意味着除非子类定义自己的copy构造和赋值函数，否则在子类没有定义的情况下，外面的调用者是不能够通过赋值和copy构造等手段来产生一个新的子类对象的。

```

#ifndef BOOST_NONCOPYABLE_HPP_INCLUDED
#define BOOST_NONCOPYABLE_HPP_INCLUDED

namespace boost {

//  Private copy constructor and copy assignment ensure classes derived from
//  class noncopyable cannot be copied.

//  Contributed by Dave Abrahams

namespace noncopyable_  // protection from unintended ADL
{
  class noncopyable
  {
   protected:
      noncopyable() {}
      ~noncopyable() {}
   private:  // emphasize the following members are private
      noncopyable( const noncopyable& );
      const noncopyable& operator=( const noncopyable& );
  };
}

typedef noncopyable_::noncopyable noncopyable;

} // namespace boost

#endif  // BOOST_NONCOPYABLE_HPP_INCLUDED

```

---------------------
作者：huang_xw
来源：CSDN
原文：https://blog.csdn.net/huang_xw/article/details/8248960
版权声明：本文为博主原创文章，转载请附上博文链接！
