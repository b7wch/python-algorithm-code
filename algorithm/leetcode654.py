#!/usr/bin/python
# -*- coding:utf-8 -*-
# 2018/6/26

# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """

        def devide_by_max(nus):
            if not nus:
                return None
            max_num = max(nus)
            index = 0
            for i, j in enumerate(nus):
                if j == max_num:
                    index = i
            root = TreeNode(max_num)
            print(root.val)
            root.left = devide_by_max(nus[:index])
            root.right = devide_by_max(nus[index+1:])
            return root

        return devide_by_max(nums)

root = Solution().constructMaximumBinaryTree([3, 2, 1, 6, 0, 5])
print(root)
