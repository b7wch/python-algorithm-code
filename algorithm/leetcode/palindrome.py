#!/usr/bin/python
# -*- coding:utf-8 -*-
# 2017/12/13
import unittest


def validate(s, length):
    if length == 0 or length == 1:
        return True
    j = length - 1
    if s[0] == s[j]:
        if length >= 2:
            return validate(s[1:-1], len(s[1:-1]))
        else:
            return True
    else:
        return False


class Test(unittest.TestCase):
    def test1(self):
        self.assertTrue(validate('121', len('121')))

    def test2(self):
        self.assertTrue(validate('12121', len('12121')))

    def test3(self):
        self.assertFalse(validate('12', len('12')))

    def test4(self):
        self.assertTrue(validate('1221', len('1221')))

if __name__ == '__main__':
    unittest.main()
