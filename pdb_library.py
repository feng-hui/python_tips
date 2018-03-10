# -*- coding: utf-8 -*-
# @author = 'Feng_hui'
# @time = '2018/3/10 16:32'
# @email = 'fengh@asto-inc.com'
# @remarks = "单步调试库pdb的使用"
import pdb
import sys


def add(num1=0, num2=0):
    """参数值想加"""
    num1 = num1 if isinstance(num1, int) else int(num1)
    num2 = num2 if isinstance(num2, int) else int(num2)
    return num1 + num2


def sub(num1=0, num2=0):
    """参数值相减"""
    num1 = num1 if isinstance(num1, int) else int(num1)
    num2 = num2 if isinstance(num2, int) else int(num2)
    return num1 - num2


if __name__ == "__main__":
    addition = add(sys.argv[1], sys.argv[2])
    pdb.set_trace()
    print('参数1和参数2相加的结果为：'.format(str(addition)))
    pdb.set_trace()
    minus = sub(sys.argv[1], sys.argv[2])
    print('参数1和参数2相减的结果为：'.format(str(minus)))
