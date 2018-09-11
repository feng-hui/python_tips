#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @time   : 18-9-11 下午4:43
# @author : Feng_Hui
# @email  : capricorn1203@126.com
import numpy as np


class NumpyExample(object):

    @staticmethod
    def typical_example():
        """
        typical example
        """

        a = np.arange(15).reshape(3, 5)
        print('NumPy数组(ndarray):\n', a)
        print('数组轴(维度)的个数：', a.ndim)
        print('数组的维度(整数的元组)：', a.shape)
        print('数组元素的总数：', a.size)
        print('数组元素的类型：', a.dtype)
        print('数组元素的字节大小：', a.itemsize)
        # print(a.data)

    @staticmethod
    def how_to_create_array():

        # 一维数组
        array_ex1 = np.array([2, 3, 4, 5])
        print('一维数组: ', array_ex1)

        # 二维数组
        array_ex2 = np.array([2, 3, 4, 5, 6, 7]).reshape(2, 3)
        print('二维数组: \n', array_ex2)

        # 三维数组
        array_ex3 = np.arange(24).reshape(2, 3, 4)
        print('三维数组: \n', array_ex3)


if __name__ == "__main__":
    numpy_example = NumpyExample()
    numpy_example.typical_example()
    numpy_example.how_to_create_array()
