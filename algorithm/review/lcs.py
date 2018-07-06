#!/usr/bin/python
# -*- coding:utf-8 -*-
# 2018/6/27


def lcs(a, b):
    if min(len(a), len(b)) < 1:
        return 0
    if a[-1] == b[-1]:
        return lcs(a[:-1], b[:-1]) + 1
    else:
        return max(lcs(a[:-1], b), lcs(a, b[:-1]))


print(lcs('cb', 'abcd'))
