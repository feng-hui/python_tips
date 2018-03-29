# -*- coding: utf-8 -*-
# @author = 'Feng_hui'
# @time = '2018/3/29 20:17'
# @email = 'fengh@asto-inc.com'


def depth_first(tree_node):
    """
    深度优先算法理解模型
    递归方法
    容易出现深度递归
    """
    if tree_node is not None:
        print(tree_node.data)
    if tree_node.left_node is not None:
        return depth_first(tree_node.left_node)
    if tree_node.right_node is not None:
        return depth_first(tree_node.right_node)


def breadth_first(root):
    """广度优先算法理解模型"""
    my_queue = []
    node = root
    my_queue.append(node)
    while my_queue:
        node = my_queue.pop(0)
        print(node.elem)
        if node.lchild is not None:
            my_queue.append(node.lchild)
        if node.rchild is not None:
            my_queue.append(node.rchild)
