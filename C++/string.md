
# string 字符串操作

Strings are objects that represent sequences of characters.

> c_str

get C string equivalent

> `char * strtok(char *str, const char* delimiters)`

参数：str, 待分割的字符串（c-string）; delimiters 分隔符字符串

> `strtok_s` 函数

strtok_s是windows下的一个分割字符串安全函数，其函数原型如下：

`char *strtok_s( char *strToken, const char *strDelimit, char **buf);`

这个函数将剩余的字符串存储在buf变量中，而不是静态变量中，从而保证了安全性。
