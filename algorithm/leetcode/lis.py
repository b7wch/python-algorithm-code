#!/usr/bin/python
# -*- coding:utf-8 -*-
# 2018/6/22
from bisect import bisect


def basic_lis(seq):
    L = [1] * len(seq)
    for cur, val in enumerate(seq):
        for pre in range(cur):
            if seq[pre] <= val:
                L[cur] = max(L[cur], 1 + L[pre])
    return max(L)


def lis(seq):
    end = []
    for val in seq:
        idx = bisect(end, val)
        if idx == len(end):
            end.append(val)
        else:
            end[idx] = val
    print(end)
    return len(end)


# print(bisect([1, 2, 5], 3))
print(lis([1, 2, 3, 7, 5, 6, 3, 4]))
