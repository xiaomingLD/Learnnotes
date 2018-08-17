
# Markdown学习笔记

## 区块引用

> 区块引用 Blockquotes, 在引用的文字前加入>

区块引用也支持嵌套

>>在要嵌套的文字前加入两个 >>


引用的区块内也可以使用其他的Markdown语法，包括标题、列表、代码区块等

> ## 这是一个标题。
>
> 1.   这是第一行列表项。
> 2.   这是第二行列表项。
>
> 给出一些例子代码：
>
>     return shell_exec("echo $input | $markdown_script");

## 列表

Markdown 支持有序列表和无序列表

无序列表使用星号、加号或是减号作为列表标记：

*   Red
*   Green
*   Blue

等同于：

+   Red
+   Green
+   Blue

也等同于：

-   Red
-   Green
-   Blue

有序列表则使用数字接着一个英文句点：

1.  Bird
2.  McHale
3.  Parish

列表项目标记通常是放在最左边，也可以缩进，但是最多3个空格

*   Lorem ipsum dolor sit amet, consectetuer adipiscing elit.
    Aliquam hendrerit mi posuere lectus. Vestibulum enim wisi, viverra nec, fringilla in, laoreet vitae, risus.

*   Donec sit amet nisl. Aliquam semper ipsum sit amet velit.
    Suspendisse id sem consectetuer libero luctus adipiscing.

## 分隔线

可以在一行中用三个以上的星号、减号、底线来建立一个分隔线

***

****

---

## 区段元素

### 链接

This is [an example](http://example.com/ "Title") inline link.

[This link](http://example.net/) has no title attribute.

如果你是要链接到同样主机的资源，你可以使用相对路径：

See my [About](/about/) page for details.

## 强调

Markdown 使用星号（``*``）和底线（_）作为标记强调字词的符号，被 * 或 _ 包围的字词会被转成用 <em> 标签包围，用两个 * 或 _ 包起来的话，则会被转成 <strong>，例如：
