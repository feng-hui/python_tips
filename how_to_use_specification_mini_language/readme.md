## 格式规范化微语言

> "格式规范"用于格式字符串中包含的替换字段中，以定义各个值的显示方式（请参阅格式字符串语法和格式化字符串文字）。它们也可以直接传递给内置的`format()`函数。

1、标准格式说明符的一般形式如下：

```
format_spec     ::=  [[fill]align][sign][#][0][width][grouping_option][.precision][type]
fill            ::=  <any character>
align           ::=  "<" | ">" | "=" | "^"
sign            ::=  "+" | "-" | " "
width           ::=  digit+
grouping_option ::=  "_" | ","
precision       ::=  digit+
type            ::=  "b" | "c" | "d" | "e" | "E" | "f" | "F" | "g" | "G" | "n" | "o" | "s" | "x" | "X" | "%"
```

使用说明如下：

* fill 表示填充字符串，可以为任意值；
* align 表示对齐方式
    * < 左对齐
    * \> 右对齐
    * ^ 居中
    * = 强制将填充放置在符号(如果有)之后但再数字之前。例如：`'{:0=10d}'.format(+2)`
    