# python_tips
various different python tips(各种不同的python小技巧)

# 注意
所有的程序全部基于python3，不兼容python2

# common_time
通过time库获取各种不同类型的时间

# common_datetime
通过datetime库获取各种不同类型的时间

# type_hint
python里的类型暗示，3.5版本之后才可以使用

# pdb_library
python里的pdb库，主要用于断点测试、单步调试等功能

设置断点：pdb.set_trace()

单步调试 下一行：n

单步调试 打印变量值：p + 变量名

单步调试 添加断点：b + 行数

单步调试 显示调试位置：l

单步调试 进入调用函数内部：s

单步调试 返回进入函数的返回语句：r

单步调试 随时结束调试：q

# how_to_use_generator

yield的主要作用是把一个函数变成一个生成器对象，通过生成器的send方法可以与生成器进行交互，交互之前必须执行next方法，否则生成器不会开始执行，
执行一次返回一次迭代值，下次执行的时候从yield的下一个语句进行执行。

# how_to_use_deque

如何使用双端队列deque，以及deque数据移动的方法
