#!/usr/bin/python
# -*- coding:utf-8 -*-
# 2018/6/26

class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 0 or num == 1:
            return False
        while num % 2 == 0:
            num /= 2
        while num % 3 == 0:
            num /= 3
        while num % 5 == 0:
            num /= 5
        if num == 1:
            return True
        else:
            return False


print(Solution().isUgly(8))
