# -*- coding: utf-8 -*-
# @author = 'Feng_hui'
# @time = '2018/3/3 19:08'
# @email = 'fengh@asto-inc.com'


def annotated(x: int, y: int) -> bool:
    """
    What are Type Hints in python3.5
    https://stackoverflow.com/questions/32557920/what-are-type-hints-in-python-3-5
    """
    return x < y


print(annotated(1, 3))
