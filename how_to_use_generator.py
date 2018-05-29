#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @time   : 18-5-29 下午11:20
# @author : Feng_Hui
# @email  : capricorn1203@126.com


def custom_generator():
    value = yield 1
    yield value


if __name__ == "__main__":
    # 执行send方法与生成器交互之前需要执行next方法
    my_gen = custom_generator()
    print(next(my_gen))
    print(my_gen.send(2))
