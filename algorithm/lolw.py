#!/usr/bin/python
# -*- coding:utf-8 -*-
# 2017/12/15
import unittest


class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        length = len(s)
        i, j, f = 0, 0, 0
        for x in range(length-1, -1, -1):
            if s[x] and not f:
                j = x
                f = 1
            if not s[x] and f:
                i = x
        return j - i + 1


class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(5, Solution().lengthOfLastWord("Hello World"))


if __name__ == '__main__':
    unittest.main()
