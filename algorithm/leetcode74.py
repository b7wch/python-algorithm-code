#!/usr/bin/python
# -*- coding:utf-8 -*-
# 2018/6/26

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        elif not matrix[0]:
            return False

        def devide_search(ls, target, n):
            if not ls:
                return False
            middle = n // 2
            if target == ls[middle]:
                return True
            if target > ls[middle]:
                return devide_search(ls[middle + 1:], target, n - middle - 1)
            else:
                return devide_search(ls[:middle], target, middle)

        if target > matrix[-1][-1]:
            return False
        for each in matrix:
            if target > each[-1]:
                continue
            return devide_search(each, target, len(each))
        return False


matrix = [
    [1, 3, 5, 7],
    [10, 11, 16, 20],
    [23, 30, 34, 50]
]

print(Solution().searchMatrix(matrix, 3))
