#!/usr/bin/python3
# -*- coding:utf-8 -*- 
# @author FH
# @email: capricorn1203@126.com
# @time: 2019/6/13 19:43Pip
from ddt import ddt, file_data
import unittest


@ddt
class TestLog(unittest.TestCase):

    @file_data('yy.yml')
    def test_login(self, *args, **kwargs):
        print(args)
        print(kwargs)

    @file_data('ss.json')
    def test_json(self, *args, **kwargs):
        print(args)
        print(kwargs)


if __name__ == "__main__":
    unittest.main()
