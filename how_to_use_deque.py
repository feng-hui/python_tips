#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @time   : 18-5-31 下午4:40
# @author : Feng_Hui
# @email  : capricorn1203@126.com
from collections import deque


def send_message(the_month, the_day, the_info):
    """按照给定的月份、日期和信息，经过一定的规则输出对应的数字"""
    dq = deque([['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'],
                ['J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R'],
                ['S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '*']])
    dq.rotate(the_month - 1)
    dq1 = deque(dq[0])
    dq1.rotate(the_day - 1)
    dq2 = deque(dq[1])
    dq2.rotate(the_day - 1)
    dq3 = deque(dq[2])
    dq3.rotate(the_day - 1)
    first_list = [{each_num[0][1]: '{0}{1}'.format(each_num[1], each_num[0][0])}
                  for each_num in zip(enumerate(dq1), [1] * 9)]
    second_list = [{each_num[0][1]: '{0}{1}'.format(each_num[1], each_num[0][0])}
                   for each_num in zip(enumerate(dq2), [2] * 9)]
    third_list = [{each_num[0][1]: '{0}{1}'.format(each_num[1], each_num[0][0])}
                  for each_num in zip(enumerate(dq3), [3] * 9)]
    info_list = first_list + second_list + third_list
    info_dict = {}
    for each_info in info_list:
        for key, value in each_info.items():
            info_dict[key] = value
    # print(info_dict)
    the_info = the_info.replace(' ', '*')
    # print(the_info)
    ret_info = [info_dict.get(each_word, '') for each_word in the_info]
    return ' '.join(ret_info)


if __name__ == "__main__":
    print(send_message(2, 14, 'I LOVE YOU'))
    # try:
    #     my_date = input('请输入月份和日期，并以空格作为分隔：')
    #     month = int(my_date.split(' ')[0])
    #     day = int(my_date.split(' ')[-1])
    #     assert 1 <= month <= 12, '输入的月份不合法'
    #     assert 1 <= day <= 31, '输入的日期不合法'
    #     my_info = input('请输入需要传递的信息：')
    #     print(send_message(month, day, my_info))
    # except Exception as e:
    #     print(e)

