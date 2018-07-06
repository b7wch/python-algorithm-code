#!/usr/bin/python
# -*- coding:utf-8 -*-
# 2018/6/26

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def __init__(self):
        self.num_of_sum = 0

    def pathSum(self, root, path_sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """

        self.num_of_sum = 0
        self.dfs(root, path_sum)
        return self.num_of_sum

    # 操作意图：
    # 深度优先遍历，目的在于扫描所有二叉树内的子节点，
    # 然后在递归调用中调用sum_try函数针对每个子节点向下求和
    def dfs(self, root, target):
        if not root:
            return
        self.sum_try(root, target)
        # 递归分解，进入向下递归操作，递归操作根据二叉树结构分为左右两步
        self.dfs(root.left, target)
        self.dfs(root.right, target)
        # 子树递归操作结束，向上退出

    def sum_try(self, node, target):
        if not node:
            return
        if node.val == target:
            self.num_of_sum += 1
        self.sum_try(node.left, target - node.val)
        self.sum_try(node.right, target - node.val)
