#!/usr/bin/python
# -*- coding:utf-8 -*-
# 2017/12/15

# !/usr/bin/python
# -*- coding:utf-8 -*-
# 2017/12/15
import unittest


class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        nl = len(needle)
        hl = len(haystack)
        if needle == haystack:
            return 0
        if not haystack or nl > hl:
            return -1
        for i, _ in enumerate(haystack):
            if i + nl > hl:
                return -1
            if haystack[i:i + nl] == needle:
                return i
        return -1


class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(2, Solution().strStr("hello", "ll"))

    def test_2(self):
        self.assertEqual(-1, Solution().strStr("", "a"))

    def test_3(self):
        self.assertEqual(9, Solution().strStr("mississippi", "pi"))


if __name__ == '__main__':
    unittest.main()
