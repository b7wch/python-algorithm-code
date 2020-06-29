#!/usr/bin/python
# -*- coding:utf-8 -*-
# 2017/12/15
import unittest


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        sl = s.split()
        for i, j in enumerate(sl):
            sl[i] = j[::-1]
        return " ".join(sl)


class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual("s'teL ekat edoCteeL tsetnoc", Solution().reverseWords("Let's take LeetCode contest"))


if __name__ == '__main__':
    unittest.main()

