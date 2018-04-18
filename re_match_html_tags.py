# -*- coding: utf-8 -*-
# @author = 'Feng_hui'
# @time = '2018/4/18 19:45'
# @email = 'fengh@asto-inc.com'
# 好用推荐-正则表达式中\s+的使用
# 参考地址：https://docs.python.org/3/library/re.html
# [直接在页面中搜索\s找到对应的位置有对应的解释]
import re


def remove_special_tags(value):
    """
    主要用于爬虫中抓取到的文本处理
    适用的字符包含[ \t\n\r\f\v]
    """
    assert isinstance(value, str)
    return re.sub(r'\s+', '', temp_str)


if __name__ == "__main__":
    temp_str = '上海\n          -虹桥区\n         走着走着就散了'
    print(remove_special_tags(temp_str))
