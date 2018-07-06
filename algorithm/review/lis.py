#!/usr/bin/python
# -*- coding:utf-8 -*-
# 2018/6/27


def lis(ls):
    length = len(ls)
    L = [1 for _ in range(length)]
    for cur, val in enumerate(ls):
        for i in range(cur):
            if ls[i] <= cur:
                L[cur] = max(L[cur], L[i] + 1)
    return max(L)


print(lis([1, 7, 2, 3, 5, 6]))
