#!/usr/bin/python3
# -*- coding:utf-8 -*- 
# @author FH
# @email: capricorn1203@126.com
# @time: 2019/2/1 11:01
import datetime


# 01、按位置访问参数

print('\n01、按位置访问参数')

print('{0}, {1}, {2}'.format('a', 'b', 'c'))

print('{}, {}, {}'.format('a', 'b', 'c'))  # Python Version 3.1+

print('{2}, {1}, {0}'.format('a', 'b', 'c'))

print('{2}, {1}, {0}'.format(*'abc'))

print('{0}{1}{0}'.format('abc=a,', 'abc,'))


# 02、按名称访问参数
print('\n02、按名称访问参数')

print('Coordinates: {latitude}, {longitude}'.format(latitude='37.24N', longitude='-115.81w'))

coord = {'latitude': '37.24N', 'longitude': '-115.81w'}
print('Coordinates: {latitude}, {longitude}'.format(**coord))

# 03、访问参数的属性
print('\n03、访问参数的属性')

c = 3 - 5j
print('The complex number {0} is formed from the real part {0.real} '
      'and the imaginary party {0.imag}'.format(c))


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return 'Point {self.x}, {self.y}'.format(self=self)


print(str(Point(3, 4)))

# 04、访问参数的项
print('\n04、访问参数的项')

coord = (3, 5)
print('X: {0[0]}, Y: {0[1]}'.format(coord))

# 05、替换%s和%r
print('\n05、替换%s和%r')

print("repr(): show quotes {!r}, str() doesn't: {!s}.".format('test1', 'test2'))

# 06、对齐文本并指定宽度
print('\n06、对齐文本并指定宽度')

print('{:<30}'.format('left aligned.'))
print('{:>30}'.format('right aligned.'))
print('{:^30}'.format('centered.'))
print('{:*^30}'.format('centered.'))  # 使用*作为填充

# 07、替换%+f，%-f，和%f并且指定符号
print('\n07、替换%+f，%-f，和%f并且指定符号')

print('{:+f} {:+f}'.format(3.14, -3.14))  # + 不改变结果，原封不动显示对象的结果
print('{: f} {: f}'.format(3.14, -3.14))  # 空格会在正数前显示，负数不受影响
print('{:-f} {:-f}'.format(3.14, -3.14))  # 只显示一个-，与%f相同
print('{:f} {:f}'.format(3.14, -3.14))  # 只显示一个-，与%f相同

# 08、替换%x和%o并根据进制转换值
print('\n08、替换%x和%o并根据进制转换值')

print('int: {0:d}, hex: {0:x}, oct: {0:o}, bin: {0:b}'.format(42))

print('int: {0:d}, hex: {0:#x}, oct: {0:#o}, bin: {0:#b}'.format(42))

print('int: {0:d}, hex: {0:#x}, oct: {0:#o}, bin: {0:#b}'.format(42000))
print('int: {0:d}, hex: {0:#X}, oct: {0:#o}, bin: {0:#b}'.format(42000))

# 09、使用,作为千位分隔符
print('\n09、使用,作为千位分隔符')
print('{:,}'.format(1234567890))

# 10、使用指定类型格式化
print('\n10、使用指定类型格式化')

d = datetime.datetime(2010, 7, 4, 12, 15, 58)
print('{:%Y-%m-%d %H:%M:%S}'.format(d))

# 11、嵌套参数和更复杂的例子
print('\n11、嵌套参数和更复杂的例子')

for align, text in zip(['<', '^', '>'], ['left', 'center', 'right']):
    print('{:{fill}{align}16s}'.format(text, fill=align, align=align))

octets = [192, 168, 0, 1]
print('{:02X}{:02X}{:02X}{:02X}'.format(*octets))

# print(int(_, 16))  # 命令行在执行完上述命令后可执行这一条输出上一条结果的16进制值
print(int('C0A80001', 16))

width = 5
for num in range(5, 12):
    for base in 'dXob':
        print('{0:{width}{base}}'.format(num, width=width, base=base), end=' ')
    print()
