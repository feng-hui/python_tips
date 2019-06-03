#!/usr/bin/python3
# -*- coding:utf-8 -*- 
# @author FH
# @email: capricorn1203@126.com
# @time: 2019/6/3 13:26
from functools import lru_cache
import time


@lru_cache(maxsize=512)
def fib(number: int) -> int:
    if number == 0:
        return 0
    if number == 1:
        return 1
    return fib(number - 1) + fib(number - 2)


start_time = time.time()
result = fib(40)
print(f'Result: {result}')
print(f'Duration: {time.time() - start_time}s')
