
# Json

## Json 基础知识

在JSON中，只有6种数据类型：

number：和JavaScript的number完全一致；  
boolean：就是JavaScript的true或false；  
string：就是JavaScript的string；  
null：就是JavaScript的null；  
array：就是JavaScript的Array表示方式——[]；  
object：就是JavaScript的{ ... }表示方式。

JSON中字符集必须是UTF-8，为了统一解析，JSON的字符串必须用双引号""，Object的键也必须用双引号""。

序列化：把对象编程JSON格式。

var xiaoming = {  
    name: '小明',  
    age: 14,  
    gender: true,  
    height: 1.65,  
    grade: null,  
    'middle-school': '\"W3C\" Middle School',  
    skills: ['JavaScript', 'Java', 'Python', 'Lisp']  
};

变成JSON格式后：

{"name":"小明","age":14,"gender":true,"height":1.65,"grade":null,"middle-school":"\"W3C\" Middle School","skills":["JavaScript","Java","Python","Lisp"]}

---
> Python 数据写入json文件中

```
import json

with open("DataOigin.json", 'w') as f:
    json.dump(dict,f)

```

---

> json数据读取

```
import json

with open("DataOigin.json", 'r') as f:
    load_dict = json.load(f)

```
